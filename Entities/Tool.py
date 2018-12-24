class Tool:

    def __init__(self, ID, owner, title, description, condition, priceFullDay, priceHalfDay, imgPath, availability):
        self.ID = ID
        self.owner = owner
        self.title = title
        self.description = description
        self.condition = condition
        self.priceFullDay = priceFullDay
        self.priceHalfDay = priceHalfDay
        self.imgPath = imgPath
        self.availability = availability

    def getID(self):
        return self.ID

    def getOwner(self):
        return self.owner

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getCondition(self):
        return self.condition

    def getPriceFullDay(self):
        return self.priceFullDay

    def getPriceHalfDay(self):
        return self.priceHalfDay

    def getImagePath(self):
        return self.imgPath

    def isAvailable(self):
        return self.availability
    
    def setAvailability(self, availability):
        self.availability = availability

    def setCondition(self, condition):
        self.condition = condition