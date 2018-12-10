class Tool:

    def __init__(self, ID, owner, title, description, priceFullDay, priceHalfDay, imagePath, availability):
        self.__ID = ID
        self.__owner = owner
        self.__title = title
        self.__description = description
        self.__priceFullDay = priceFullDay
        self.__priceHalfDay = priceHalfDay
        self.__imagePath = imagePath
        self.__availability = availability

    def getID(self):
        return self.__ID

    def getOwner(self):
        return self.__owner

    def getTitle(self):
        return self.__title

    def getDescription(self):
        return self.__description

    def getPriceFullDay(self):
        return self.__priceFullDay

    def getPriceHalfDay(self):
        return self.__priceHalfDay

    def getImagePath(self):
        return self.__imagePath

    def isAvailable(self):
        return self.__availability
    
    def setAvailability(self, availability):
        self.__availability = availability
