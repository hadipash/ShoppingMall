from abc import ABCMeta, abstractmethod


class IOrderManage:
    __metaclass__ = ABCMeta

    @abstractmethod
    def purchaseRequest(self, paymentInfo):
        raise NotImplementedError
