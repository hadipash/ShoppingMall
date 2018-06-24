from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from controls.ManageAccount import ManageAccount

bp = Blueprint('account', __name__)


@bp.route('/account', methods=('GET', 'POST'))
def displayAndEditInfo():
    controller = ManageAccount()

    if request.method == 'POST':
        if request.form['submit'] == 'Save':
            error = None

            if not request.form['name']:
                error = 'Name is required'
            elif not request.form['email']:
                error = 'Email address is required'
            elif not request.form['phone']:
                error = 'Phone number is required'
            elif not request.form['address']:
                error = 'Address is required'
            elif request.form['new_password']:
                if (len(request.form['new_password']) < 8 or
                        not any(i.isdigit() for i in request.form['new_password']) or
                        not any(i.isalpha() for i in request.form['new_password'])):
                    error = 'Password must be at least 8 characters long and contain at least one letter and one digit'

            if error is not None:
                flash(error)
            else:
                try:
                    controller.editPersonalInfo(g.user['id'], request.form)
                    flash('Saved')
                except ValueError:
                    flash('Invalid password')

        elif request.form['submit'] == 'Delete Account':
            controller.deleteAccount(g.user['id'])
            return redirect(url_for('auth.logout', message='Your Account Was Deleted'))

    return render_template('account/account.html', user=controller.requestPersonalInfo(g.user['id']))
