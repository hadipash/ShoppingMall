from abc import ABCMeta, abstractmethod


class ISearchRequest:
    __metaclass__ = ABCMeta

    @abstractmethod
    def searchCategory(self, category, sortBy, asc):
        raise NotImplementedError

    @abstractmethod
    def searchName(self, productName, sortBy, asc):
        raise NotImplementedError

    @abstractmethod
    def searchHotdeal(self, salesNum, category):
        raise NotImplementedError

    @abstractmethod
    def searchSale(self, salesNum, category):
        raise NotImplementedError