from DAOs import db


class RefundDAO:
    def __init__(self):
        self.db = db.get_db()

    def getRefundInfo(self, refundNum):
        return self.db.execute('SELECT * FROM refund  WHERE id=?', (refundNum,)).fetchone()

    def addRefundtIfo(self, paymentNum, refundAdr):
        return self.db.execute('INSERT INTO refund (refundNum, refundAdr) VALUES (?, ?)', (paymentNum, refundAdr))
