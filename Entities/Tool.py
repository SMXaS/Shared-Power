class Tool:

    def __init__(self, ID, owner, title, description, condition, priceFullDay, priceHalfDay, riderCharge,
                 imgPath, availability):
        self.ID = ID
        self.owner = owner
        self.title = title
        self.description = description
        self.condition = condition
        self.priceFullDay = priceFullDay
        self.priceHalfDay = priceHalfDay
        self.riderCharge = riderCharge
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

    def getRiderCharge(self):
        return self.riderCharge

    def getImagePath(self):
        return self.imgPath

    def isAvailable(self):
        return self.availability
    
    def setAvailability(self, availability):
        self.availability = availability

    def setCondition(self, condition):
        self.condition = condition
