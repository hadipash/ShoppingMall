#-*- coding: utf-8 -*-
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
                'SELECT * FROM product WHERE name like ? ORDER BY sales_num DESC', ('%' + product_name + '%',)
            ).fetchall()

            return render_template('search/product_name.html', product_name=product_name, products=products)
    return render_template('search/product_name.html')


@bp.route('/category/')
@bp.route('/category/<category>')
def category(category=None):
    if category is not None:
        db = get_db()

        products = db.execute(
            'SELECT * FROM product WHERE category = ? ORDER BY sales_num DESC', (category,)
        ).fetchall()

        return render_template('search/category.html', category=category, products=products)
    return render_template('search/category.html', category=category, products=None)


@bp.route('/searchHOTDEAL/')
@bp.route('/searchHOTDEAL/<category>')
def searchHOTDEAL(category=None):
    db = get_db()

    if category is not None:

        products = db.execute(
            'SELECT * FROM product WHERE category = ? ORDER BY sales_num DESC', (category,)
        ).fetchmany(3)

        return render_template('search/searchHOTDEAL.html',  category=category, products=products)

    products = db.execute(
        'SELECT * FROM product WHERE sales_num >10 ORDER BY sales_num DESC  '
    ).fetchall()
    return render_template('search/searchHOTDEAL.html', category=category, products=products)

@bp.route('/searchDC/')
@bp.route('/searchDC/<category>')
def searchDC(category=None):
    db = get_db()
    if category is not None:

        products = db.execute(
            'SELECT * FROM product WHERE category = ? ORDER BY dc_rate DESC', (category,)
        ).fetchmany(3)

        return render_template('search/searchDC.html',  category=category, products=products)
    products = db.execute(
        'SELECT * FROM product WHERE dc_rate >10 ORDER BY dc_rate DESC  '
    ).fetchall()
    return render_template('search/searchDC.html', category=category, products=products)