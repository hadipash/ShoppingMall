from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from controls.ManageAccount import ManageAccount

bp = Blueprint('account', __name__)


@bp.route('/account', methods=('GET', 'POST'))
def display_info():
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

            if error is not None:
                flash(error)
            else:
                controller = ManageAccount()
                controller.editPersonalInfo(g.user['id'], request.form)
                flash('Saved')

        elif request.form['submit'] == 'Delete Account':
            controller = ManageAccount()
            controller.deleteAccount(g.user['id'])
            return redirect(url_for('auth.logout', message='Your Account Was Deleted'))

    return render_template('account/account.html', user=ManageAccount().requestPersonalInfo(g.user['id']))
