from abc import ABCMeta, abstractmethod


class IPersonalInformationRequest:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getInfo(self, client_id):
        raise NotImplementedError

    @abstractmethod
    def modify(self, PersonalInfo):
        raise NotImplementedError
