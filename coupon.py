from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, flash
)

from DAOs.db import get_db

bp = Blueprint('coupon', __name__, url_prefix='/coupon')


@bp.route('/coupon_list', methods=('GET', 'POST'))
def coupon_list():
    username = session.get('user_id')
    db = get_db()
    cur = db.execute('SELECT * FROM coupon ORDER BY coupon_id DESC')
    lists = [dict(name=row[1], discount=row[2]) for row in cur.fetchall()]

    return render_template('coupon/coupon_list.html', lists=lists)
