from DAOs import db


class PaymentDAO:
    def __init__(self):
        self.db = db.get_db()

    def getPaymentInfo(self, paymentNum):
        return self.db.execute('SELECT * FROM payment  WHERE id=?', (paymentNum,)).fetchone()

    def addPaymentIfo(self, price, shippingFee, name, phone, address, discount):
        return self.db.execute('INSERT INTO payment (price, name, phone, address, discount) VALUES (?, ?, ?, ?, ?)',
                               (price, name, phone, address, discount))

