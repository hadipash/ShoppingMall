from DAOs.ProductDAO import ProductDAO
from interfaces.ISearchRequest import ISearchRequest


class SearchManager(ISearchRequest):

    def __init__(self):
        self.__product = ProductDAO()

    def searchCategory(self, category, sortBy=0, asc=False):
        products = self.__product.getCategory(category, sortBy, asc)
        return products

    def searchName(self, productName, sortBy=0, asc=False):
        products = self.__product.getProductByName(productName, sortBy, asc)
        return products

    def searchHotdeal(self, salesNum, category):
        print("TODO")

    def searchSale(self, salesNum, category):
        print("TODO")

