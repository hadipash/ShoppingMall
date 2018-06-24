from flask import (
    Blueprint, render_template, request
)

from controls.ManageOrder import ManageOrder

bp = Blueprint('track_delivery', __name__)


@bp.route('/orders/history', methods=['GET'])
def display_history():
    controller = ManageOrder()
    return render_template('orders/track_delivery.html', delivery=controller.getTrackHistory(request.args['order_id']))
