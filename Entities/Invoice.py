class Invoice:

    def __init__(self, user, toolTitle, hirePrice, riderPrice, fine):
        self.user = user
        self.toolTitle = toolTitle
        self.hirePrice = hirePrice
        self.riderPrice = riderPrice
        self.fine = fine

    def getUser(self):
        return self.user

    def getToolTitle(self):
        return self.toolTitle

    def getHirePrice(self):
        return self.hirePrice

    def getRiderPrice(self):
        return self.riderPrice

    def getFine(self):
        return self.fine