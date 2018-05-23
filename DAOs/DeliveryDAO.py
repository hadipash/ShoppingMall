from DAOs import db


class DeliveryDAO:
    def __init__(self):
        self.db = db.get_db()

    def __enter__(self):
        return self

    def get_delivery(self, order_id):
        return self.db.execute('SELECT * FROM delivery WHERE order_id=?', (order_id,)).fetchone()
