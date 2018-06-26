from DAOs import db


class ProductDAO:
    def __init__(self):
        self.db = db.get_db()

    def getDc_rate(self, category):
        return self.db.execute('SELECT * FROM product WHERE category = ? ORDER BY dc_rate DESC ', (categoru,)).fetchmany(3)

    def getSales_num(self, category):
        return self.db.execute('SELECT * FROM product WHERE  category= ? ORDER BY sales_num DESC', (category,)).fetchmany(3)

    def getCategory(self, category, sortBy, asc):
        if sortBy == 0:
            order = 'sales_num'
        elif sortBy == 1:
            order = 'price*(100.0-dc_rate)/100.0'
        elif sortBy == 2:
            order = 'registration_date'
        elif sortBy == 3:
            order = 'product_rating'
        else:
            return None

        if asc:
            order = order + ' ASC'
        else:
            order = order + ' DESC'

        products = self.db.execute('SELECT * FROM product WHERE category = ? ORDER BY ' + order, (category,)).fetchall()
        return products

    def getProductByName(self, productName, sortBy, asc):
        if sortBy == 0:
            order = 'sales_num'
        elif sortBy == 1:
            order = 'price*(100.0-dc_rate)/100.0'
        elif sortBy == 2:
            order = 'registration_date'
        elif sortBy == 3:
            order = 'product_rating'
        else:
            return None

        if asc:
            order = order + ' ASC'
        else:
            order = order + ' DESC'

        products = self.db.execute('SELECT * FROM product WHERE name LIKE ? ORDER BY ' + order, ('%' + productName + '%',)).fetchall()

        return products

    def getProductByID(self, product_id):
        return self.db.execute('SELECT * FROM product WHERE product_id=?', (product_id,)).fetchone()
