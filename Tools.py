class  addTools:

    __name = ""
    __quantity = 0
    __price = 0
    __description = ""

    def __init__(self, name, quantity, price, description):
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__description = description

    def getName(self):
        return self.__name

    def getQuantity(self):
        return self.__quantity

    def getPrice(self):
        return self.__price

    def getDescription(self):
        return self.__description
