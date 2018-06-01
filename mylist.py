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

#def access_item():
    #return render_template('purchase/purchase.html')
