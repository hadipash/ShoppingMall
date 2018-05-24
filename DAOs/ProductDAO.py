from DAOs import db


class ProductDAO:
    def __init__(self):
        self.db = db.get_db()

    def __enter__(self):
        return self

    def getDc_rate(self):
        return self.db.execute('SELECT * FROM product ORDER BY dc_rate DESC LIMIT 3', (self.product_id,)).fetchmany(3)

    def getSales_num(self):
        return self.db.execute('SELECT * FROM product ORDER BY sales_num DESC LIMIT 3', (self.product_id,)).fetchmany(3)

    def getCategory(self):
        return self.db.execute('SELECT * FROM product WHERE category = ?', (self.product_id,)).fetchall()

    def getName(self):
        return self.db.execute('SELECT * FROM product WHERE name = ?', (self.product_id,)).fetchone()
