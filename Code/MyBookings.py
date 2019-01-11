from Resources.Values import strings
from Code.MyInvoice import MyInvoice
import Code.Utilities.util as util
import Code.Utilities.ReadFile as rf
import Code.Utilities.WriteFile as wf
import Code.test_printObj as test
import datetime

"""
-------------------------------------------------------------------------------------------------
This class shows a list with all booked items (status = hired) and allows user to return an item
    or cancel the booking
-------------------------------------------------------------------------------------------------

---------------------------------------------------------------------
*** Implementation:
---------------------------------------------------------------------
    class:
        @ 'your assigned name' = ReturnTool(Label, TreeView, string):
            * takes Label(for error messages)
            * takes TreeView (for populating the list and getting 
                information about booking)
            * takes string (userName)
---------------------------------------------------------------------
    methods:
        @ 'your assigned name'.populateData():
            populates hired items
        @ 'your assigned name'.returnItem(string):
            * takes string(tool condition (from Entry))
            - marks item as returned (changes booking status into "pending_receive") and refreshes the list
        @ 'your assigned name'.cancelBooking():
            - deletes this booking for database       
"""


class MyBookings:

    __toolIDList = []
    __toolObjList = []

    def __init__(self, errorLabel, tree, login):
        self.__errorLabel = errorLabel
        self.__tree = tree
        self.__login = login
        self.__bookingList = []
        print("MyBookings login:", login)

    def returnItem(self, toolCondition):
        if self.__tree.focus():
            self.__errorLabel.config(text="")
            self.__errorLabel.config(text="")
            returnItemObj = self.__bookingList[self.__getBookingIndex()]
            diff = util.getDayDifference(self.__getCurrentDate(), returnItemObj.getStartDate())
            print("diff at return:", diff)

            if diff <= 0:
                # toolStatus[1] = "pending_receive"
                returnItemObj.setStatus(strings.toolStatus[1])
                returnItemObj.setReturnDate(self.__getCurrentDate())
                returnItemObj.setBookOutCondition(toolCondition.get())
                bookObj_forTest = []
                bookObj_forTest.append(returnItemObj)
                print("--------------")
                print("single book Obj")
                print("--------------")
                test.printBookingObjects(bookObj_forTest)
                wf.editBooking(returnItemObj)
                self.populateData()
                toolCondition.delete(0, "end")
                MyInvoice(self.__login).generateInvoice(returnItemObj)
                return True
            else:
                self.cancelBooking()
                return False
        else:
            self.__errorLabel.config(text=strings.errorSelectItem)

    def cancelBooking(self):
        if self.__tree.focus():
            cancelItemObj = self.__bookingList[self.__getBookingIndex()]
            currentDate = self.__getCurrentDate()
            dayDiff = util.getDayDifference(currentDate, cancelItemObj.getStartDate())
            print("day diff:", dayDiff)
            if dayDiff < 1:
                print("Sorry, its too late to cancel")
                self.__errorLabel.config(text=strings.cancelErrorMessage)
            else:
                print("Cancel in progress")
                wf.cancelBooking(cancelItemObj)
                self.populateData()
                self.__errorLabel.config(text="")
        else:
            if self.getCount() > 0:
                self.__errorLabel.config(text=strings.errorSelectItem)
            else:
                self.__errorLabel.config(text=strings.errorEmptyList)

    def populateData(self):
        """
        Gets data and populates all data in the list
        :return: None
        """

        self.__toolObjList = []
        self.__toolIDList = []
        self.__bookingList = []

        self.__bookingList = rf.getAllBookings("userName", self.__login, 0)
        for i in range(len(self.__bookingList)):
            self.__toolIDList.append(self.__bookingList[i].getToolID())

        for i in range(len(self.__toolIDList)):
            tool = rf.get_tool("ID", self.__toolIDList[i])
            self.__toolObjList.append(util.convertFromListToObj(tool))

        for i in self.__tree.get_children():
            self.__tree.delete(i)
        if self.__bookingList:
            for i in range(len(self.__bookingList)):
                toolDict = rf.get_tool("ID", self.__toolIDList[i])
                tool = util.convertFromListToObj(toolDict)
                self.__tree.insert('', 'end', text=tool.getTitle(),
                                   values=(self.__bookingList[i].getStartDate(),
                                           self.__bookingList[i].getExpectedReturnDate(),
                                           self.__bookingList[i].getStatus()),
                                   tags=self.__bookingList[i].getBookingID())

    def getCount(self):
        print("count:", len(self.__bookingList))
        if self.__bookingList:
            return len(self.__bookingList)
        else:
            return 0

    def __getBookingIndex(self):
        """
        gets selected item index

        :return: int(index)
        """

        curItem = self.__tree.focus()
        index = None
        if curItem:
            itemID = None
            for item in self.__tree.selection():
                itemID = self.__tree.item(item, "tag")

            for i in range(len(self.__bookingList)):
                if self.__bookingList[i].getBookingID() in itemID:
                    index = i
                    break

        return index

    def __getCurrentDate(self):
        return datetime.datetime.now().strftime(strings.dateFormat)
