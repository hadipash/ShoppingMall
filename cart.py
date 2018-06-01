#-*- coding: utf-8 -*-
from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, flash, request, jsonify
)
from DAOs.db import init_db, get_db

bp = Blueprint('cart', __name__, url_prefix='/cart')


@bp.route('/cart_list', methods=('GET', 'POST'))
def cart_list():
    username = session['user_id']
    db = get_db()

    cur = db.execute(
        'SELECT price FROM product WHERE product_id IN '
        '(SELECT product_id FROM cart_list WHERE user_id = ?)', (username,)
    )
    totalprice = 0
    for row in cur.fetchall():
        totalprice += row[0]
    cur = db.execute(
        'SELECT name, price, product_id FROM product WHERE product_id IN '
        '(SELECT product_id FROM cart_list WHERE user_id = ?)', (username,)
    )
    lists = [dict(name=row[0], price=row[1], id=row[2]) for row in cur.fetchall()]
    return render_template('cart/cart_list.html', lists=lists, totalprice=totalprice)


@bp.route('/delete_item', methods=('GET', 'POST'))
def delete_item():
    username = session['user_id']
    id = request.data
    db = get_db()
    db.execute('DELETE FROM cart_list WHERE product_id = ? and user_id = ?', (id, username,))
    db.commit()

    return jsonify(
        result = "success"
    )

# def purchase_item():
# return render_template('purchase/purchase.html', productInfo=productInfo)
