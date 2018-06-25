from flask import (
    Blueprint, g, render_template, request
)

from controls.ManageOrder import ManageOrder

bp = Blueprint('orders', __name__)


@bp.route('/orders', methods=('GET', 'POST'))
def display_orders():
    controller = ManageOrder()

    if request.method == 'POST' and request.form['submit'] == 'Confirm Delivery':
        controller.confrimDelivery(request.form["order_id"])

    return render_template('orders/orders.html', orders=controller.getDeliveries(g.user['id']))
