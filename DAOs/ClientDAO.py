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
        self.db.commit()

    def getPersonalInfo(self, client_id):
        return self.db.execute('SELECT * FROM client WHERE id=?', (client_id,)).fetchone()

    def updatePersonalInfo(self, client_id, new_info):
        print("Client ID:")
        print(client_id)
        for key in new_info:
            if key != "submit" and new_info[key] != "":
                test = new_info[key]
                self.db.execute('UPDATE client SET ' + key + '=? WHERE id=?', (new_info[key], client_id))
        self.db.commit()

    def removeClient(self, client_id):
        self.db.execute('DELETE FROM client WHERE id=?', (client_id,))
        self.db.commit()

    def getCartList(self, client_id):
        return self.db.execute('SELECT * FROM cart_list WHERE user_id=?', (client_id,)).fetchall()

    def addCartItem(self, client_id, product_id, quantity):
        self.db.execute('INSERT INTO cart_list (user_id, product_id, quantity) VALUES (?, ?, ?)',
                        (client_id, product_id, quantity))
        self.db.commit()

    def delCartItem(self, client_id, product_id):
        self.db.execute('DELETE FROM cart_list WHERE user_id=? AND product_id=?', (client_id, product_id))
        self.db.commit()

    def getCouponList(self, client_id):
        return self.db.execute('SELECT * FROM coupon_list WHERE user_id=?', (client_id,)).fetchall()

    def addCoupon(self, client_id, coupon_id):
        self.db.execute('INSERT INTO coupon_list (user_id, coupon_id) VALUES (?, ?)', (client_id, coupon_id))
        self.db.commit()

    def delCoupon(self, client_id, coupon_id):
        self.db.execute('DELETE FROM coupon_list WHERE user_id=? AND coupon_id=?', (client_id, coupon_id))
        self.db.commit()

    def getMyList(self, client_id):
        return self.db.execute('SELECT * FROM my_list WHERE user_id=?', (client_id,)).fetchall()

    def addMyListItem(self, client_id, product_id):
        self.db.execute('INSERT INTO my_list (user_id, product_id) VALUES (?, ?)', (client_id, product_id))
        self.db.commit()

    def delMyListItem(self, client_id, product_id):
        self.db.execute('DELETE FROM my_list WHERE user_id=? AND product_id=?', (client_id, product_id))
        self.db.commit()
