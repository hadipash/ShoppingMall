from flask import Blueprint, render_template, g
from DAOs.ClientDAO import ClientDAO

bp = Blueprint('account', __name__)


@bp.route('/account', methods=('GET', 'POST'))
def display_info():
    return render_template('account/account.html', user=ClientDAO().getPersonalInfo(g.user['id']))
