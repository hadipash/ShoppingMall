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


@bp.route('/add_item', methods=['POST'])
def add_item():
    username = session['user_id']
    id = request.data
    db = get_db()
    db.execute('INSERT INTO cart_list (user_id, product_id, quantity) VALUES(?,?,1)',(username, id))
    db.commit()
    return jsonify(
        result = "success"
    )