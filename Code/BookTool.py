from Resources.Values import strings
import Code.Utilities.util as util
from Entities.Bookings import Bookings
import Code.Utilities.WriteFile as wf
import Code.Utilities.ReadFile as rf
import uuid

"""
-------------------------------------------------------------------------------------------------
This Class Makes the Booking For the user
-------------------------------------------------------------------------------------------------

---------------------------------------------------------------------
*** Implementation:
---------------------------------------------------------------------
    class:
        @ 'your assigned name' = BookTool(listBox, listBox, Object):
            * takes ListBox (startDate)
            * takes ListBox (endDate)
            * takes Object (Selected Tool)
---------------------------------------------------------------------
    methods:
        @ 'your assigned name'.getNextDays():
            - returns list with available end dates
        @ 'your assigned name'.getStartDate():
            - gets the string for the Start Date
            - based on Start Date will generate End Dates and populates the listbox
        @ 'your assigned name'.populateStartList():
            -Calls __getAvailableList()
            -populates available Dates List
        @ 'your assigned name'.getEndDate():
            -Gets the end Date of the booking from the User
        @ 'your assigned name'.getMessage():
            -returns the message list to the UI
        @ 'your assigned name'.hireTool(string, string, string, string, string):
            *takes string (username)
            *takes string (startDate)
            *takes string (endDate)
            *takes string (PickupLocation)
            *takes string (DropoffLocation)
            -Check if Start Date and End Date are picked if True:
                                                                  - Creates booking Object
                                                                  - Calls VerifyHiring()
                                                        if False:
                                                                  - Returns "Error" 
        @ 'your assigned name'.vfWrite():
            - passes the booking object to WriteFile
"""

class BookTool:
    def __init__(self, availableDateBox, availableEndDateBox, tool):
        self.availableDateBox = availableDateBox
        self.tool = tool
        self.availableEndDateBox = availableEndDateBox

    def getNextDays(self):
        return self.nextDays

    def getStartDate(self):

        index = int(self.availableDateBox.curselection()[0])
        self.__start_date = self.availableDateBox.get(index)
        print(self.__start_date)
        self.nextDays = util.getNextAvailableDates(self.__start_date, self.availableDateList)


        self.__populateEndList()

    def populateStartList(self):

        bookingList = self.__getBookingList()

        self.availableDateList = self.__getAvailableList(bookingList)
        for i in range(len(self.availableDateList)):
            self.availableDateBox.insert("end", self.availableDateList[i])

    def __getBookingList(self):
        """
        :return: list(obj(all bookings for particular item))
        """

        return rf.getAllBookings("toolID", self.tool.getID(), 0)

    def __getAvailableList(self, bookingList):
        """
        :param bookingList: list(obj(bookings))
        :return: list(available dates)
        """

        return util.getBookingDates(bookingList)

    def __populateEndList(self):
        """
          Fills Return booking list with available dates
          :return: None
          """

        self.availableEndDateBox.delete(0, "end")
        for i in range(len(self.nextDays)):
            print(self.nextDays[i])
            self.availableEndDateBox.insert("end", self.nextDays[i])

    def getEndDate(self):

        index = int(self.availableEndDateBox.curselection()[0])
        self.__end_date = self.availableEndDateBox.get(index)

    def __verifyHiring(self):
        """
        Verifies booking
        :return: boolean (True - approved, False - not)
        """

        booking = self.__getBookingList()
        availabeList = self.__getAvailableList(booking)
        dayDiff = util.getDayDifference(self.__start_date, self.__end_date)
        if util.verifyBooking(self.__start_date, availabeList, dayDiff):
            return True
        else:
            return False

    def getMessage(self):
        return self.message

    def hireTool(self, login, startTerm, endTerm, pickUpEntry, dropOffEntry):

        if self.__start_date and self.__end_date:
            self.hiredTool = Bookings(uuid.uuid4(), self.tool.getID(), login, self.tool.getCondition(),
                                 self.__start_date, startTerm, self.__end_date, endTerm,
                                 strings.toolStatus[0])

            self.hiredTool.setPickUpLocation(pickUpEntry)
            self.hiredTool.setDropOffLocation(dropOffEntry)

            if self.__verifyHiring():
                # show confirmation window
                totalPrice = util.calculateToolhireCost(self.hiredTool, self.tool)
                self.message = "{} {}\n{} {}\n{} {}\n{} {}{}\n\n{}".format(strings.toolTitleForInvoice, self.tool.getTitle(),
                                                                           strings.hireDate, self.hiredTool.getStartDate(),
                                                                           strings.returnDate,
                                                                           self.hiredTool.getExpectedReturnDate(),
                                                                           strings.totalCost, strings.currency,
                                                                           str(totalPrice), strings.confirmBooking)

                return 1
            else:
                return 0

        else:
            print("Error")

    def wfwrite(self):

        #          obj,     simplePath,     fieldNames,           complex path              path parameter
        wf.write(self.hiredTool, None, strings.fieldNames_booking, strings.filePath_booking, self.hiredTool.getToolID())






