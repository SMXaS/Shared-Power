class Bookings:
  
    def __init__ (self, toolID, userName, startDate, expectedReturnDate, returnDate = ""):
        self.toolID = toolID
        self.userName = userName
        self.startDate = startDate
        self.expectedReturnDate = expectedReturnDate
        self.returnDate = returnDate
    
    def getToolID(self):
        return self.toolID
    
    def getUserName(self):
        return self.userName
      
    def getStartDate(self):
        return self.startDate
      
    def getExpectedReturnDate(self):
        return self.expectedReturnDate
      
    def get returnDate(self):
        return self.returnDate
      
    def setReturnDate(self, returnDate):
        self.returnDate = returnDate
