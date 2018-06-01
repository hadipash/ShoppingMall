#-*- coding: utf-8 -*-
from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, flash
)

from DAOs.db import get_db

bp = Blueprint('coupon', __name__, url_prefix='/coupon')


@bp.route('/add_coupon', methods=['POST'])
def add_coupon():
    userid = 1

    db = get_db()

    db.execute('DELETE FROM coupon_list')

    db.execute('INSERT into coupon_list(user_id,coupon_id) values(?,?)',
               [userid, request.form['coupon_id']])
    db.commit()

    print('coupon ', request.form['coupon_id'], ' added!')
    return redirect('coupon/coupon_list')
@bp.route('/coupon_list')
def coupon_list():
    db = get_db()
    couponlist = db.execute('SELECT * FROM coupon').fetchall()

    return render_template('coupon/coupon_list.html', lists=couponlist)