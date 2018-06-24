from flask import (
    Blueprint, g, render_template
)

from controls.ManageOrder import ManageOrder

bp = Blueprint('orders', __name__)


@bp.route('/orders', methods=('GET', 'POST'))
def display_orders():
    controller = ManageOrder()

    return render_template('orders/orders.html', orders=controller.getDeliveries(g.user['id']))
