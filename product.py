#-*- coding: utf-8 -*-
from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for, flash, request, jsonify
)
from DAOs.db import init_db, get_db

bp = Blueprint('product', __name__, url_prefix='/product')


@bp.route('/product_info/')
@bp.route('/product_info/<int:product_id>')
def product_info(product_id):
    db = get_db()
    product = db.execute('SELECT * FROM product WHERE product_id = ?', (product_id,)).fetchone()
    return render_template('product/product_info.html', product=product)


