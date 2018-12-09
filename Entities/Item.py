class Item:

    __owner = ""

    def __init__(self, owner, title, description, price, imagePath):
        self.__owner = owner
        self.__title = title
        self.__description = description
        self.__price = price
        self.__imagePath = imagePath

    def getOwner(self):
        return self.__owner

    def getTitle(self):
        return self.__title

    def getDescription(self):
        return self.__description

    def getPrice(self):
        return self.__price

    def getImagePath(self):
        return self.__imagePath
