Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
import photos

class Hiretool

    def __init__(self, search_tool, check_availability, book_tool, pick_up, drop_off, time, charge, photos, provide_condition, receive_item):

        self.search_tool            =   search_tool
        self.check_availability     =   check_availability
        self.book_tool              =   book_tool
        self.pick_up                =   pick_up
        self.drop_off               =   drop_off
        self.time                   =   time
        self.charge                 =   charge
        self.photos                 =   photos
        self. provide_condition     =   provide_condition
        self. receive_item          =   receive_item

# returns search tool
    def getSearch(self):
        return self.search_tool

# returns book tool
    def getBookTool(self):
        return self.book_tool

# returns pick up
    def getPickUp(self):
        return self.pick_up

# returns drop off
    def getDropOff(self):
        return self.drop_off

# returns time
    def getTime(self):
        return self.time

# returns charge
    def getCharge(self):
        return self.charge

# returns photos
def getPhotos(self):
        return self.photos

# returns provide condition
def getProvideCondition(self):
        return self.provide_condition

# returns receive items
def getReceiveItems(self):
        return self.receive_item

# Return true if the tools is available
def inRange(self, searchTool):

        returnResult = False

        if (searchTool > self._availability and searchTool < self._book_tool):

                    returnResult = True

                return returnResult
# save hire tool
def__str__(self):

    returnValue = ''
    returnValue += ()
