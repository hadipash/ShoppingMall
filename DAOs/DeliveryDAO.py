from DAOs import db


class DeliveryDAO:
    def __init__(self):
        self.db = db.get_db()

    def getDelivery(self, order_id):
        return self.db.execute('SELECT * FROM placed_order WHERE order_id=?', (order_id,)).fetchone()

    def getDeliveries(self, client_id):
        return self.db.execute('SELECT order_id,dc_price FROM client_order WHERE client_id=?', (client_id,)).fetchall()

    def getProductList(self, order_id):
        return self.db.execute('SELECT product_id, quantity FROM product_order WHERE order_id=?', (order_id,)) \
            .fetchall()

    def getTrackHistory(self, track_number):
        return self.db.execute('SELECT location, hub_date FROM delivery_history WHERE track_number=? '
                               'ORDER BY hub_date ASC', (track_number,)).fetchall()

    def removeDelivery(self, order_id):
        pass

    def addDelivery(self, delivery):
        pass

    def setStatus(self, order_id, status):
        self.db.execute('UPDATE placed_order SET last_status=? WHERE order_id=?', (status, order_id))
        self.db.commit()
