from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, flash
)

from DAOs.db import get_db

bp = Blueprint('cart', __name__, url_prefix='/cart')


@bp.route('/cart_list', methods=('GET', 'POST'))
def cart_list():
    username = session.get('user_id')
    db = get_db()

    cur = db.execute(
       'SELECT name, price FROM product WHERE product_id = '
       '(SELECT product_id FROM cart_list WHERE user_id = ?)', (username,)
    )
    lists = [dict(name=row[0], price=row[1]) for row in cur.fetchall()]

    return render_template('cart/cart_list.html', lists=lists)

