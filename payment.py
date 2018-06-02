# -*- coding: utf-8 -*-
from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, flash
)

from DAOs.db import get_db

bp = Blueprint('payment', __name__, url_prefix='/payment')


@bp.route('/result', methods=['post'])
def result():
    db = get_db()

    db.execute('INSERT INTO payment (price, shippingFee, name, phone, address, discount) VALUES(?,?,?,?,?,?)',
               (request.form['price'],0, request.form['name'], request.form['phone'], request.form['address'],0))
    return render_template('payment/payment_result.html')


@bp.route('/product')
def product():
    pass


@bp.route('/cart', methods=('GET', 'POST'))
def cart():
    price_sum = request.form['totalprice']
    username = session.get('user_id')
    db = get_db()
    # cartlist 들고와서 product돌면서 가격더해서 가격에 넣고 price*quantity의합

    # form으로 넘겨받으면 2를쓰고 db로 바로쓰면1
    cartlist1 = db.execute('SELECT a.price, a.dc_rate,a.product_id, b.quantity,a.stock FROM product a, cart_list b '
                          'WHERE a.product_id = b.product_id AND user_id = ?', (username,)).fetchall()
    # cartlist2 = request.form['cartlist']
    price_sum1 = 0
    # price_sum2 = request.form['totalprice']

    for curlist in cartlist1:
        price_sum1 += curlist[0] * (100 - curlist[1]) / 100 *curlist[3]

    # if request.method == 'POST':
    #     #     print(request.form['price'])

    clientinfos = db.execute('SELECT name,phone,address,mileage FROM client WHERE id = ?', (username,)).fetchall()


    couponlist = db.execute('SELECT a.name, a.coupon_id, a.discount FROM coupon a, coupon_list b '
                            'WHERE a.coupon_id=b.coupon_id AND user_id = ?',(username,)).fetchall()
    # 쿠폰리스트에서 쿠폰들고오고 적용

    #할인된가격 = (가격 -마일리지)* (1-0.쿠폰할인율)
    coupon_info = None;

    # lists = [dict(name=row[0], phone=row[1], addresss=row[2], mileage=row[3]) for row in client_info]
    return render_template('payment/payment.html', coupon_list = couponlist, cart_list = cartlist1,client_infos=clientinfos, price_sum=price_sum)
