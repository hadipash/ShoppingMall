from DAOs import db


class DeliveryDAO:
    def __init__(self, order_id):
        self.db = db.get_db()
        self.order_id = order_id

    def __enter__(self):
        return self

    def get_delivery(self):
        return self.db.execute('SELECT * FROM delivery WHERE order_id=?', (self.order_id,)).fetchone()
