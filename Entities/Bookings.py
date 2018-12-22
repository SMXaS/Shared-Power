class Bookings:
  
    def __init__ (self, toolID, userName, startDate, startTerm, expectedReturnDate, expectedTerm,
                  returnDate = ""):
        self.toolID = toolID
        self.userName = userName
        self.startDate = startDate
        self.startTerm = startTerm
        self.expectedReturnDate = expectedReturnDate
        self.expectedTerm = expectedTerm
        self.returnDate = returnDate
    
    def getToolID(self):
        return self.toolID
    
    def getUserName(self):
        return self.userName
      
    def getStartDate(self):
        return self.startDate

    def getStartTerm(self):
        return self.startTerm

    def getExpectedReturnDate(self):
        return self.expectedReturnDate

    def getExpectedTerm(self):
        return self.expectedTerm

    def getReturnDate(self):
        return self.returnDate
      
    def setReturnDate(self, returnDate):
        self.returnDate = returnDate
