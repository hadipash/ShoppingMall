# -*- coding: utf-8 -*-
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from DAOs.db import get_db
from controls.SearchManager import SearchManager


bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/product_name', methods=('GET', 'POST'))
def product_name():
    if request.method == 'POST':
        product_name = request.form['product_name']
        search_manager = SearchManager()
        products = search_manager.searchName(product_name)
        return render_template('search/product_name.html', product_name=product_name, products=products)
    return render_template('search/product_name.html')


@bp.route('/category/')
@bp.route('/category/<category>')
def category(category=None):
    if category is not None:
        search_manager = SearchManager()
        products = search_manager.searchCategory(category)
        return render_template('search/category.html', category=category, products=products)
    return render_template('search/category.html', category=category, products=None)


@bp.route('/searchHOTDEAL/')
@bp.route('/searchHOTDEAL/<category>')
def searchHOTDEAL(category=None):
    db = get_db()

    if category is not None:
        search_manager = SearchManager()
        products = search_manager.searchHotdeal(category)
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
        search_manager = SearchManager()
        products = search_manager.searchSale(category)
        return render_template('search/searchDC.html',  category=category, products=products)
    products = db.execute(
        'SELECT * FROM product WHERE dc_rate >10 ORDER BY dc_rate DESC  '
    ).fetchall()
    return render_template('search/searchDC.html', category=category, products=products)


@bp.route('/sort_by_name', methods=('GET', 'POST'))
def sort_by_name():
    if request.method == 'POST':
        product_name = request.form['product_name']
        sort_type = request.form['sort_type']
        asc_or_desc = request.form['asc_or_desc']

        if sort_type == 'sales':
            sortBy = 0
        elif sort_type == 'price':
            sortBy = 1
        elif sort_type == 'date':
            sortBy = 2
        elif sort_type == 'rating':
            sortBy = 3

        if asc_or_desc == 'ascending':
            asc = True
        else:
            asc = False

        search_manager = SearchManager()
        products = search_manager.searchName(product_name, sortBy, asc)
        return render_template('search/product_name.html', product_name=product_name, products=products, sort_type=sort_type, asc=asc)
    return render_template('search/product_name.html')


@bp.route('/sort_by_category', methods=('GET', 'POST'))
def sort_by_category():
    if request.method == 'POST':
        category = request.form['category']
        sort_type = request.form['sort_type']
        asc_or_desc = request.form['asc_or_desc']

        if sort_type == 'sales':
            sortBy = 0
        elif sort_type == 'price':
            sortBy = 1
        elif sort_type == 'date':
            sortBy = 2
        elif sort_type == 'rating':
            sortBy = 3

        if asc_or_desc == 'ascending':
            asc = True
        else:
            asc = False

        search_manager = SearchManager()
        products = search_manager.searchCategory(category, sortBy, asc)
        return render_template('search/category.html', category=category, products=products, sort_type=sort_type, asc=asc)
    return render_template('search/category.html')
