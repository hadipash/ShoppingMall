from DAOs.DeliveryDAO import DeliveryDAO


class ManageOrder:
    __order = None

    def __init__(self):
        self.__order = DeliveryDAO()

    def confrimDelivery(self, order_id):
        pass

    def getDeliveryInfo(self, client_id):
        pass

    def timeOut(self, order_id):
        pass
