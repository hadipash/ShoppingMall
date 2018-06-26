from DAOs import db


class PaymentDAO:
    def __init__(self):
        self.db = db.get_db()

    def getPaymentInfoByOrderID(self, order_id):
        payment_id = self.db.execute('SELECT payment_id FROM payment_order WHERE order_id=?', (order_id,)).fetchone()
        return self.getPaymentInfo(payment_id['payment_id'])

    def getPaymentInfo(self, payment_id):
        return self.db.execute('SELECT * FROM payment WHERE payment_id=?', (payment_id,)).fetchone()

    def addPaymentIfo(self, price, name, phone, address, discount):
        return self.db.execute('INSERT INTO payment (price, name, phone, address, discount) VALUES (?, ?, ?, ?, ?)',
                               (price, name, phone, address, discount))

    def getPaymentDetails(self, payment_id):
        return self.db.execute('SELECT product_id, price, quantity, total_sum '
                               'FROM payment_detail WHERE payment_id=?', (payment_id,)).fetchall()
