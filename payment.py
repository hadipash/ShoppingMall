# -*- coding: utf-8 -*-
from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, flash
)

from DAOs.db import get_db

bp = Blueprint('payment', __name__, url_prefix='/payment')


@bp.route('/result', methods=['post'])
def result():
    db = get_db()
    username = session.get('user_id')
    amount = int(request.form['amount'])
    product_id = request.form['product_id']

    cur_payment_num=db.execute('SELECT exists(select * from payment where paymentNum = 1)').fetchall()[0][0]
    if cur_payment_num == 1:
        cur_payment_num = int(db.execute('SELECT paymentNum FROM payment ORDER BY paymentNum DESC LIMIT 1').fetchone()[0])+1
    else :
        cur_payment_num = 1

    cur_order_id = db.execute('SELECT exists(select * from placed_order where order_id = 1)').fetchall()[0][0]
    if cur_order_id == 1:
        cur_order_id = int(db.execute('SELECT order_id FROM placed_order ORDER BY order_id DESC LIMIT 1').fetchone()[0])+1
    else :
        cur_order_id = 1

    cur_track_number = db.execute('SELECT exists(select * from placed_order where track_number = 1)').fetchall()[0][0]
    if cur_track_number == 1:
        cur_track_number = int(db.execute('SELECT track_number FROM placed_order ORDER BY track_number DESC LIMIT 1').fetchone()[0])+1
    else:
        cur_track_number = 1

    # 카트거치고옴
    if amount == 0:
        cart_list = db.execute('SELECT a.price, a.dc_rate,a.product_id, b.quantity,a.stock FROM product a, cart_list b '
                               'WHERE a.product_id = b.product_id AND user_id = ?', (username,)).fetchall()

        for products in cart_list:
            if products[4]-products[3] < 0:
                return render_template('payment/payment_result.html', payment_success=False)
        db.execute('INSERT INTO placed_order(track_number, delivery_company, last_status) VALUES(?, ?, ?)',(cur_track_number,"LOGEN",0) )
        db.execute('INSERT INTO payment (price, name, phone, address, discount) VALUES(?, ?, ?, ?, ?)',
                   (request.form['price'], request.form['name'], request.form['phone'],
                    request.form['address'], request.form['dc_price']))
        db.commit()
        for products in cart_list:
            db.execute('INSERT INTO payment_detail (payment_id,product_id,quantity,price) VALUES(?,?,?,?)',(cur_payment_num,products[2],products[3],products[0] * ((100.0-products[2])/100.0)))
            db.execute('INSERT INTO product_order (order_id,product_id,quantity) VALUES(?,?,?)',(cur_order_id,products[2],products[3]))
            db.execute('UPDATE product SET stock = ? WHERE product_id = ?',
                       (products[4] - products[3], products[2]))
        db.execute('DELETE FROM cart_list WHERE user_id = ?', (username,))
    # 카트안거침
    else:
        product_info= db.execute('SELECT stock,price,dc_rate FROM product WHERE product_id = ?', (product_id,)).fetchone()
        stock = product_info[0]

        price = product_info[1] * ((100.0-product_info[2])/100.0)

        if stock < amount:
            return render_template('payment/payment_result.html', payment_success=False)

        db.execute('INSERT INTO placed_order(track_number, delivery_company, last_status) VALUES(?, ?, ?)',(cur_track_number,"LOGEN",1) )
        db.execute('INSERT INTO payment (price, name, phone, address, discount) VALUES(?, ?, ?, ?, ?)',
                   (request.form['price'], request.form['name'], request.form['phone'],
                    request.form['address'], request.form['dc_price']))
        db.commit()

        db.execute('INSERT INTO product_order (order_id,product_id,quantity) VALUES(?,?,?)',(cur_order_id,product_id,amount))
        db.execute('INSERT INTO payment_detail (payment_id,product_id,quantity,price) VALUES(?,?,?,?)',(cur_payment_num,product_id,amount,price))
        db.execute('DELETE FROM my_list WHERE user_id = ? AND product_id = ? ',(username,product_id))
        db.execute('UPDATE product SET stock = stock - ?, sales_num = sales_num + ? '
                   'WHERE product_id = ?', (amount, amount, product_id))

    mileage_used = int(request.form['mileage_used'])
    mileage_add = int(float(request.form['dc_price']))*10
    mileage = int(request.form['mileage']) - mileage_used + mileage_add
    db.execute('UPDATE client SET mileage = ? WHERE id = ?', (mileage, username))
    coupon_id = int(request.form['coupon_id'])
    if coupon_id is not 0:
        db.execute('UPDATE coupon_list SET used = ? WHERE user_id = ? AND coupon_id = ? ', (1, username, coupon_id))
    db.execute('INSERT INTO client_order(client_id,order_id,dc_price) VALUES(?,?,?)',(username,cur_order_id,request.form['dc_price']))


    db.commit()

    return render_template('payment/payment_result.html', payment_success=True, **locals())


@bp.route('/product')
def product():
    pass


@bp.route('/cart', methods=['POST'])
def cart():
    price_sum = float(request.form['price'])
    amount = request.form['amount']
    product_id = request.form['product_id']
    username = session.get('user_id')
    db = get_db()

    client_info = db.execute('SELECT name,phone,address,mileage FROM client WHERE id = ?', (username,)).fetchall()[0]

    coupon_list = db.execute('SELECT a.name, a.coupon_id, a.discount FROM coupon a, coupon_list b '
                             'WHERE a.coupon_id=b.coupon_id AND user_id = ? AND b.used=0', (username,)).fetchall()
    dc_sum = 0.0
    select_coupon = 0
    discount = request.form.get('discount')

    mileage = 0
    coupon_discount = 0
    if discount is not None:
        mileage = int(request.form['mileage'])
        select_coupon = int(request.form['coupon_list'])
        if select_coupon != 0:
            coupon_discount = db.execute('SELECT discount FROM coupon '
                                         'WHERE coupon_id = ?', [select_coupon]).fetchone()[0]
        dc_sum = price_sum - (price_sum-mileage*0.001) * (100-coupon_discount)/100

    return render_template('payment/payment.html', **locals())
