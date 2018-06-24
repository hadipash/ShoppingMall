from DAOs.DeiveryStatus import DeliveryStatus
from DAOs.DeliveryDAO import DeliveryDAO
from DAOs.ProductDAO import ProductDAO


class ManageOrder:
    def __init__(self):
        self.__order = DeliveryDAO()
        self.__product = ProductDAO()

    def confrimDelivery(self, order_id):
        self.__order.setStatus(order_id, DeliveryStatus.DELIVERED)

    def getDeliveryInfo(self, order_id):
        self.__order.getDelivery(order_id)

    def getDeliveries(self, client_id):
        orders = []
        order_list = self.__order.getDeliveries(client_id)

        for ordr in order_list:
            order = dict(self.__order.getDelivery(ordr['order_id']))  # placed_order table
            order['last_status'] = DeliveryStatus.getStringValue(order['last_status'])
            order['products'] = []

            product_list = self.__order.getProductList(ordr['order_id'])  # product_order table
            for product in product_list:
                order['products'].append(dict(self.__product.getProductByID(product['product_id'])))
                order['products'][-1].update({'quantity': product['quantity']})

            orders.append(order)

        return orders

    def addDelivery(self, delivery):
        self.__order.addDelivery(delivery)

    def timeOut(self, order_id):
        self.confrimDelivery(order_id)
