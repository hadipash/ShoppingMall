from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, flash
)

from DAOs.db import init_db, get_db, close_db

bp = Blueprint('mylist', __name__, url_prefix='/mylist')


@bp.route('/my_list', methods=('GET', 'POST'))
def my_list():
    username = session['user_id']
    close_db()
    init_db()

    cur = g.db.execute(
       'SELECT name FROM product WHERE product_id IN '
       '(SELECT product_id FROM my_list WHERE user_id = ?)', (username,)
    )
    lists = [dict(name=row[0]) for row in cur.fetchall()]

    return render_template('cart/my_list.html', lists=lists)


def delete_item(id):
    db = get_db()
    db.execute('DELETE FROM my_list WHERE id = ?', (id,))
    db.commit()
    return redirect('cart/cart_list.html')

#def access_item():
    #return render_template('purchase/purchase.html')
