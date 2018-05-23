from DAOs import db


class CouponDAO:
    def __init__(self, coupon_id):
        self.db = db.get_db()
        self.coupon_id = coupon_id

    def __enter__(self):
        return self

    def get_coupon_list(self):
        return self.db.execute('SELECT * FROM coupon', (self.coupon_id,)).fetchall()