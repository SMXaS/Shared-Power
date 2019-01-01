

import BookTool
import utilities
import time
import photos

class HireTool():

def __init___(self, search_tool, check_availability, book_tool, rider, pick_up, time, charge, photos, drop_off, provide condition, receive item):

    self.search_tool            =       search_tool
    self.check_availability     =       check_availability
    self.book_tool              =       book_tool
    self.rider                  =       rider
    self.pick_up                =       pick_up
    self.time                   =       time
    self.charge                 =       charge
    self.photos                 =       photos
    self.drop_off               =       drop_off
    self.provide_condition      =       provide_condition
    self.receive_item           =       receive_item

# return search tool
def getSearchTool(self):
    return self.search_tool


# return check availability
def getCheckAvailability(self):
    return self.check_availability


#  return book tool
def getBookTool(self):
    return self.book_tool

# return rider
def getRider(self):
    return self.rider

# return pick pick_up
def getPickUp(self):
    return self.pick_up

# return time
def getTime(self):
    return self.time

# return charge
def getCharge(self):
    retrun self.charge

# return photos
def getPhotos(self):
    return self.photos

# return drop off
def getDropOff(self):
    return self.drop_off

# return provide condition
def getProvideCondition(self):
    return self.provide_condition

 # return receive item
 def getReceiveItem(self):
    return self.receive_item

# Persist the invoice to disk
def persist(self):

    filepath = self.buildFilePath()
    self.createHireToolDirectories(filePath)

    fileName = filePath + '/' + self.search_tool

    self.writeHireToolToFile(fileName)
    self.writeBookToolToFile(fileName)

# Load HireTool from utilities
def load(self):

    filePath = self.buildFilepath()

    fileName = filePath +'/' + self.search_tool

    self.readHireToolfromFile(fileName)

# __str___function
def___str___(self):

    returnValue = 'Search Tool: ' + self.search_tool + '\n'
    returnValue += 'HireTool Date: ' + str(self.hiretool_date) + '\n'

    for BookTool in self.book_tool:
        returnValue += str(BookTool)

    returnValue += '\nDescription \t \t Quantity'
    returnValue += '\n------------\t \t--------\n'

    for BookTool in self.book_tool:
        returnValue += str(BookTool)

    return returnValue

#___repr__function
def__repr__(self):

    returnValue = 'Search Tool: ' + self.search_tool + '\n'
    returnValue += HireTool Date: '   + str(self.hiretool_date) + '\n'

    returnValue += '\nDescription \t \t quantity'
    returnValue += '\n------------\t \t---------\n'

    for BookTool in self.book_tool:
        returnValue += str(BookTool)
        
    return returnValue
