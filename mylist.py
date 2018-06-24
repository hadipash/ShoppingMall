#-*- coding: utf-8 -*-
from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, flash, jsonify
)

from DAOs.db import init_db, get_db, close_db

bp = Blueprint('mylist', __name__, url_prefix='/mylist')


@bp.route('/my_list', methods=('GET', 'POST'))
def my_list():
    username = session['user_id']
    db = get_db()

    cur = db.execute(
       'SELECT name, product_id FROM product WHERE product_id IN '
       '(SELECT product_id FROM my_list WHERE user_id = ?)', (username,)
    )
    lists = [dict(name=row[0], id=row[1]) for row in cur.fetchall()]

    return render_template('cart/my_list.html', lists=lists)


@bp.route('/delete_item', methods=('GET', 'POST'))
def delete_item():
    username= session['user_id']
    id = request.data
    db = get_db()
    db.execute('DELETE FROM my_list WHERE product_id = ? and user_id = ?', (id, username,))
    db.commit()
    return jsonify(
        result="success"
    )


@bp.route('/add_item', methods=['POST'])
def add_item():
    username = session['user_id']
    Data = request.json

    db = get_db()
    item = db.execute('SELECT product_id FROM my_list WHERE user_id=? and product_id=?', (username, Data['ID'])).fetchone()
    if item is None :
        db.execute('INSERT INTO my_list (user_id, product_id) VALUES(?,?)', (username, Data['ID']),)
        db.commit()
        msg = "찜한 목록에 추가되었습니다"
    else :
        msg = "찜한 목록에 이미 존재하는 제품입니다"
    return jsonify(
        result="success",
        msg=msg
    )
