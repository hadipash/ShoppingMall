#-*- coding: utf-8 -*-
from flask import (
    Blueprint, render_template, session, request, jsonify
)
from DAOs.db import get_db

bp = Blueprint('cart', __name__, url_prefix='/cart')


@bp.route('/cart_list', methods=('GET', 'POST'))
def cart_list():
    username = session['user_id']
    db = get_db()

    cur = db.execute(
        'SELECT A.price, A.dc_rate, B.quantity FROM product A '
        'LEFT JOIN cart_list B ON A.product_id = B.product_id WHERE B.user_id = ?', (username,)
    )
    totalprice = 0
    for row in cur.fetchall():
        totalprice += round(row[0]*((100.0 - row[1])/100.0), 2)*row[2]
    cur = db.execute(
        'SELECT A.name, A.price, A.product_id, A.dc_rate, B.quantity FROM product A '
        'LEFT JOIN cart_list B ON A.product_id = B.product_id WHERE B.user_id = ?', (username,)
    )
    lists = [dict(name=row[0], price=row[1], id=row[2], dc=row[3], quantity=row[4]) for row in cur.fetchall()]
    return render_template('cart/cart_list.html', lists=lists, totalprice=totalprice)


@bp.route('/delete_item', methods=['POST'])
def delete_item():
    username = session['user_id']
    id = int(request.data)
    db = get_db()
    cur = db.execute('DELETE FROM cart_list WHERE product_id = ? and user_id = ?', (id, username,))
    db.commit()
    return jsonify(
        result = "success"
    )


@bp.route('/add_item', methods=['POST'])
def add_item():
    username = session['user_id']
    Data = request.json

    db = get_db()
    item = db.execute('SELECT product_id, quantity FROM cart_list WHERE user_id=? and product_id=?', (username, Data['ID'])).fetchone()
    if item is None :
        db.execute('INSERT INTO cart_list (user_id, product_id, quantity) VALUES(?,?,?)',(username, Data['ID'], Data['AMT']))
        db.commit()
        msg = "장바구니에 추가되었습니다"
    else :
        msg = "장바구니에 이미 존재하는 제품입니다"
    return jsonify(
        result="success",
        msg=msg
    )
