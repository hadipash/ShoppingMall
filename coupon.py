#-*- coding: utf-8 -*-
from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, flash
)

from DAOs.db import get_db

bp = Blueprint('coupon', __name__, url_prefix='/coupon')


@bp.route('/add_coupon', methods=['POST'])
def add_coupon():
    username = session.get('user_id')
    db = get_db()
    selectcoupon = request.form['coupon_id']
    mycoupon_list = db.execute('SELECT coupon_id FROM coupon_list WHERE user_id=?', [username]).fetchall()
    coupon_name = db.execute('SELECT name FROM coupon WHERE coupon_id=?', [selectcoupon]).fetchone()
    for coupon in mycoupon_list :
        if int(coupon[0]) == int(request.form['coupon_id']):
            flash(coupon_name[0] + '  쿠폰은 이미 가지고 있거나 사용하셨습니다.')
            return redirect('coupon/coupon_list')

    db.execute('INSERT into coupon_list(user_id,coupon_id) values(?,?)',(username, selectcoupon))
    db.commit()

    flash(coupon_name[0] + '  쿠폰을 획득하셨습니다.')
    print('coupon', selectcoupon, ' added!')
    return redirect('coupon/coupon_list')
@bp.route('/coupon_list')
def coupon_list():
    db = get_db()
    couponlist = db.execute('SELECT * FROM coupon').fetchall()

    return render_template('coupon/coupon_list.html', lists=couponlist)