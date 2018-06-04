from DAOs.DeliveryDAO import DeliveryDAO
from DAOs.DeiveryStatus import DeliveryStatus


class ManageOrder:
    __order = None

    def __init__(self):
        self.__order = DeliveryDAO()

    def confrimDelivery(self, order_id):
        self.__order.setStatus(order_id, DeliveryStatus.DELIVERED)

    def getDeliveryInfo(self, order_id):
        self.__order.getDelivery(order_id)

    def getDeliveries(self, client_id):
        self.__order.getDeliveries(client_id)

    def addDelivery(self, delivery):
        self.__order.addDelivery(delivery)

    def timeOut(self, order_id):
        self.confrimDelivery(order_id)
