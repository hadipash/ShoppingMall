from DAOs import db


class CouponDAO:
    def __init__(self):
        self.db = db.get_db()

    def __enter__(self):
        return self

    def get_coupon_list(self):
        return self.db.execute('SELECT * FROM coupon').fetchall()
