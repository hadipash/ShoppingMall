from flask import Blueprint, render_template

bp = Blueprint('orders', __name__)


@bp.route('/orders')
def display_orders():
    return render_template('orders/orders.html', orders=None)
