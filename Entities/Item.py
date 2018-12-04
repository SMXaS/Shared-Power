class Item:

    __owner = ""
    __title = ""
    __description = ""
    __quantity = 0
    __price = 0.0
    __imagePath = ""

    def __init__(self, owner, title, description, quantity, price, imagePath):
        self.__owner = owner
        self.__title = title
        self.__description = description
        self.__quantity = quantity
        self.__price = price
        self.__imagePath = imagePath

    def getOwner(self):
        return self.__owner

    def getTitle(self):
        return self.__title

    def getDescription(self):
        return self.__description

    def getQuantity(self):
        return self.__quantity

    def getPrice(self):
        return self.__price

    def getImagePath(self):
        return self.__imagePath
