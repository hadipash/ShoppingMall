import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from DAOs.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute('SELECT * FROM client WHERE id=?', (user_id,)).fetchone()


@bp.route('/login', methods=('GET', 'POST'))
def login():
    """Log in a registered user by adding the user id to the session."""
    error = None
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']

        db = get_db()
        user = db.execute('SELECT * FROM client WHERE email=?', (email,)).fetchone()

        if user is None:
            error = 'Invalid email'
        elif password != user['password']:
            error = 'Invalid password'
        else:
            session.clear()
            session['user_id'] = user['id']
            flash('Welcome, ' + user['name'])
            return render_template('base.html')
    return render_template('auth/login.html', error=error)


@bp.route('/logout')
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for('index'))
