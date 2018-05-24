from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from DAOs.db import get_db


bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/product_name', methods=('GET', 'POST'))
def product_name():
    if request.method == 'POST':
        product_name = request.form['product_name']
        db = get_db()
        error = None

        if not product_name:
            error = 'Product name is required'

        if error is None:
            products = db.execute(
                'SELECT * FROM product WHERE name = ?', (product_name,)
            ).fetchall()

            return render_template('search/product_name.html', products=products)
    return render_template('search/product_name.html', products=None)


@bp.route('/category', methods=('GET', 'POST'))
def category():
    return render_template('search/category.html', products=None)

