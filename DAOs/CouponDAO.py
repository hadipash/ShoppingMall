from DAOs import db


class CouponDAO:
    def __init__(self):
        self.db = db.get_db()

    def get_coupon_list(self):
        return self.db.execute('SELECT * FROM coupon').fetchall()
