from DAOs.DeiveryStatus import DeliveryStatus
from DAOs.DeliveryDAO import DeliveryDAO
from DAOs.ProductDAO import ProductDAO
from DAOs.PaymentDAO import PaymentDAO


class ManageOrder:
    def __init__(self):
        self.__order = DeliveryDAO()
        self.__product = ProductDAO()
        self.__payment = PaymentDAO()

    def confrimDelivery(self, order_id):
        self.__order.setStatus(order_id, DeliveryStatus.CONFIRMED.value)

    def getDeliveryInfo(self, order_id):
        return self.__order.getDelivery(order_id)

    def getDeliveries(self, client_id):
        orders = []
        order_list = self.__order.getDeliveries(client_id)

        for ordr in order_list:
            order = dict(self.getDeliveryInfo(ordr['order_id']))  # placed_order table
            order['last_status'] = DeliveryStatus.getStringValue(order['last_status'])

            order.update(dict(self.__payment.getPaymentInfoByOrderID(order['order_id'])))
            payment_details = self.__payment.getPaymentDetails(order['payment_id'])
            order['products'] = []
            for payment in payment_details:
                product = dict(self.__product.getProductNameByID(payment['product_id']))
                product.update(dict(payment))
                order['products'].append(product)

            orders.append(order)

        return orders

    def getTrackHistory(self, order_id):
        delivery = dict(self.getDeliveryInfo(order_id))
        delivery['last_status'] = DeliveryStatus.getStringValue(delivery['last_status'])
        delivery['history'] = dict(self.__order.getTrackHistory(delivery['track_number']))

        return delivery

    def addDelivery(self, client_id, payment_id):
        self.__order.addDelivery(client_id, payment_id)

    def timeOut(self, order_id):
        self.confrimDelivery(order_id)
