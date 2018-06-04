from DAOs import db


class DeliveryDAO:
    def __init__(self):
        self.db = db.get_db()

    def getDelivery(self, order_id):
        return self.db.execute('SELECT * FROM delivery WHERE order_id=?', (order_id,)).fetchone()

    def removeDelivery(self, order_id):
        pass

    def addDelivery(self, delivery):
        pass
