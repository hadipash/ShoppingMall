from DAOs import db


class DeliveryDAO:
    def __init__(self):
        self.db = db.get_db()

    def getDelivery(self, order_id):
        return self.db.execute('SELECT * FROM placed_order WHERE order_id=?', (order_id,)).fetchone()

    def getDeliveries(self, client_id):
        return self.db.execute('SELECT order_id FROM client_order WHERE client_id=?', (client_id,)).fetchall()

    def getProductList(self, order_id):
        return self.db.execute('SELECT product_id, quantity FROM product_order WHERE order_id=?', (order_id,)) \
            .fetchall()

    def removeDelivery(self, order_id):
        pass

    def addDelivery(self, delivery):
        pass

    def setStatus(self, order_id, status):
        pass
