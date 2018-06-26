from abc import ABCMeta, abstractmethod


class IDeliveryStatusRequest:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getDeliveryStatus(self, track_number):
        raise NotImplementedError
