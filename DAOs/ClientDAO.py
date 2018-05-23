from DAOs import db


class ClientDAO:
    def __init__(self):
        self.db = db.get_db()

    def __enter__(self):
        return self

    def getEmail(self, client_id):
        return self.db.execute('SELECT email FROM client WHERE id=?', (client_id,)).fetchone()

    def getPhoneNum(self, client_id):
        return self.db.execute('SELECT phone FROM client WHERE id=?', (client_id,)).fetchone()

    def getMileage(self, client_id):
        return self.db.execute('SELECT mileage FROM client WHERE id=?', (client_id,)).fetchone()

    def setMileage(self, client_id, mileage):
        self.db.execute('UPDATE client SET mileage=? WHERE id=?', (mileage, client_id))

    def getPersonalInfo(self, client_id):
        return self.db.execute('SELECT * FROM client WHERE id=?', (client_id,))

    def updatePersonalInfo(self, client_id, new_val):
        for key in new_val:
            statement = 'UPDATE client SET ' + key + '=' + new_val[key] + ' WHERE id=?'
            self.db.execute(statement, (client_id,))

    def removeClient(self, client_id):
        self.db.execute('DELETE FROM client WHERE id=?', (client_id,))

    def getCartList(self, client_id):
        return self.db.execute('SELECT * FROM cart_list WHERE user_id=?', (client_id,))

    def addCartItem(self, client_id, product_id, quantity):
        self.db.execute('INSERT INTO cart_list (user_id, product_id, quantity) VALUES (?, ?, ?)',
                        (client_id, product_id, quantity))

    def getCouponList(self, client_id):
        return self.db.execute('SELECT * FROM coupon_list WHERE user_id=?', (client_id,))

    def addCoupon(self, client_id, coupon_id, quantity):
        self.db.execute('INSERT INTO coupon_list (user_id, coupon_id, quantity) VALUES (?, ?, ?)',
                        (client_id, coupon_id, quantity))

    def getMyList(self, client_id):
        return self.db.execute('SELECT * FROM my_list WHERE user_id=?', (client_id,))

    def addMyListItem(self, client_id, product_id):
        self.db.execute('INSERT INTO my_list (user_id, product_id) VALUES (?, ?)',
                        (client_id, product_id))
