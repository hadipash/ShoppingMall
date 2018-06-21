#-*- coding: utf-8 -*-
from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, flash, request, jsonify
)
from DAOs.db import init_db, get_db

bp = Blueprint('product', __name__, url_prefix='/product')


@bp.route('/product_detail', methods=['POST'])
def product_detail():
    id = request.form['product_id']
    db = get_db()

    item = db.execute('SELECT name, price, product_id, dc_rate FROM product WHERE product_id = ?', (id,)).fetchone()

    return render_template('product/product_detail.html', item=item)


@bp.route('/product_info/')
@bp.route('/product_info/<int:product_id>')
def product_info(product_id):
    db = get_db()
    product = db.execute('SELECT * FROM product WHERE product_id = ?', (product_id,)).fetchone()
    return render_template('product/product_info.html', product=product)


@bp.route('/add_item', methods=['POST'])
def add_item():
    username = session['user_id']
    Data = request.json

    msg = ""
    db = get_db()
    item = db.execute('SELECT product_id, quantity FROM cart_list WHERE user_id=? and product_id=?', (username, Data['ID'])).fetchone()
    if item is None :
        db.execute('INSERT INTO cart_list (user_id, product_id, quantity) VALUES(?,?,?)',(username, Data['ID'], Data['AMT']))
        db.commit()
        msg = "장바구니에 추가되었습니다"
    else :
        print(item[1])
        msg = "장바구니에 이미 "+ str(item[1]) +"개 존재하는 제품입니다"
    return jsonify(
        result="success",
        msg=msg
    )