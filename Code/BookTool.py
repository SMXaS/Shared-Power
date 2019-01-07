from Resources.Values import strings
import Code.Utilities.util as util
from Entities.Bookings import Bookings
import Code.Utilities.WriteFile as wf
import Code.Utilities.ReadFile as rf
import uuid



class BookTool:
    def __init__(self, availableDateBox, availableEndDateBox, tool):
        self.availableDateBox = availableDateBox
        self.tool = tool
        self.availableEndDateBox = availableEndDateBox

    def getNextDays(self):
        return self.nextDays

    def getStartDate(self):
        """
        Getting start booking date.
        based on selection from start date (bookings) list will generate end date list

        :return: None
        """

        index = int(self.availableDateBox.curselection()[0])
        self.__start_date = self.availableDateBox.get(index)
        print(self.__start_date)
        self.nextDays = util.getNextAvailableDates(self.__start_date, self.availableDateList)


        self.populateEndList()


    def populateStartList(self):
        """
        Fills Start booking list with available dates
        :return: None
        """

        bookingList = self.getBookingList()

        self.availableDateList = self.getAvailableList(bookingList)
        for i in range(len(self.availableDateList)):
            self.availableDateBox.insert("end", self.availableDateList[i])

    def getBookingList(self):
        """
        :return: list(obj(all bookings for particular item))
        """

        return rf.getAllBookings("toolID", self.tool.getID(), 0)

    def getAvailableList(self, bookingList):
        """
        :param bookingList: list(obj(bookings))
        :return: list(available dates)
        """

        return util.getBookingDates(bookingList)



    def populateEndList(self):
        """
          Fills Return booking list with available dates
          :return: None
          """

        self.availableEndDateBox.delete(0, "end")
        for i in range(len(self.nextDays)):
            print(self.nextDays[i])
            self.availableEndDateBox.insert("end", self.nextDays[i])


    def getEndDate(self):
        """
        Getting end booking date. Calls "show arrange rider" function
        :return: None
        """

        index = int(self.availableEndDateBox.curselection()[0])
        self.__end_date = self.availableEndDateBox.get(index)

    def verifyHiring(self):
        """
        Verifies booking
        :return: boolean (True - approved, False - not)
        """

        booking = self.getBookingList()
        availabeList = self.getAvailableList(booking)
        dayDiff = util.getDayDifference(self.__start_date, self.__end_date)
        if util.verifyBooking(self.__start_date, availabeList, dayDiff):
            return True
        else:
            return False


    def getMessage(self):
        return self.message

    def hireTool(self, login, startTerm, endTerm, pickUpEntry, dropOffEntry):
        """
        Verify booking. If True:
            Create booking object and pass it to WriteFile
            Will return to SearchToolPage
        :return: None
        """



        if self.__start_date and self.__end_date:
            self.hiredTool = Bookings(uuid.uuid4(), self.tool.getID(), login, self.tool.getCondition(),
                                 self.__start_date, startTerm, self.__end_date, endTerm,
                                 strings.toolStatus[0])

            self.hiredTool.setPickUpLocation(pickUpEntry)
            self.hiredTool.setDropOffLocation(dropOffEntry)

            if self.verifyHiring():
                # show confirmation window
                totalPrice = util.calculateToolhireCost(self.hiredTool, self.tool)
                self.message = "{} {}\n{} {}\n{} {}\n{} {}{}\n\n{}".format(strings.toolTitleForInvoice, self.tool.getTitle(),
                                                                      strings.hireDate, self.hiredTool.getStartDate(),
                                                                      strings.returnDate,
                                                                      self.hiredTool.getExpectedReturnDate(),
                                                                      strings.totalCost, str(totalPrice),
                                                                      strings.currency,
                                                                      strings.confirmBooking)

                return 1
            else:
                return 0




        else:
            print("Error")

    def wfwrite(self):

        #          obj,     simplePath,     fieldNames,           complex path              path parameter
        wf.write(self.hiredTool, None, strings.fieldNames_booking, strings.filePath_booking, self.hiredTool.getToolID())






