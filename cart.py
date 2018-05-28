from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, flash
)
import click
from DAOs.db import init_db, get_db

bp = Blueprint('cart', __name__, url_prefix='/cart')


@bp.route('/cart_list', methods=('GET', 'POST'))
def cart_list():
    username = session['user_id']
    init_db()

    cur = g.db.execute(
       'SELECT name, price FROM product WHERE product_id IN '
       '(SELECT product_id FROM cart_list WHERE user_id = ?)', (username,)
    )
    totalprice = 0
    for row in cur.fetchall():
        totalprice += row[1]
    cur = g.db.execute(
        'SELECT name, price FROM product WHERE product_id IN '
        '(SELECT product_id FROM cart_list WHERE user_id = ?)', (username,)
    )
    lists = [dict(name=row[0], price=row[1]) for row in cur.fetchall()]
    return render_template('cart/cart_list.html', lists=lists, totalprice=totalprice)


def delete_item(id):
    db = get_db()
    db.execute('DELETE FROM cart_list WHERE id = ?', (id,))
    db.commit()
    return redirect('cart_list')

#def purchase_item():
    #return render_template('purchase/purchase.html', productInfo=productInfo)