from Resources.Values import strings
import Code.Utilities.util as util
import Code.Utilities.ReadFile as rf
import datetime


class ReturnTool:

    __toolIDList = []
    __toolObjList = []

    def __init__(self, errorLabel, tree, login):
        """

        :param errorLabel: widget(label)(label which will show any error)
        :param tree: widget(treeView)
        :param login: str(user name)
        """

        self.__errorLabel = errorLabel
        self.__tree = tree
        self.__login = login
        self.__bookingList = rf.getAllBookings("userName", self.__login)

    def __getCurrentDate(self):
        return datetime.datetime.now().strftime(strings.dateFormat)

    def returnItem(self):
            returnItemObj = self.__bookingList[self.__getBookingIndex()]
            # toolStatus[1] = "pending_receive"
            returnItemObj.setStatus(strings.toolStatus[1])
            returnItemObj.setReturnDate(self.__getCurrentDate())
            # TODO edit booking #returnItemObj#
            print("new status:", returnItemObj.getStatus())

    def __getBookingIndex(self):
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

    def cancelBooking(self):
        cancelItemObj = self.__bookingList[self.__getBookingIndex()]
        print("start date:", cancelItemObj.getStartDate())
        print("end date:", cancelItemObj.getExpectedReturnDate())
        currentDate = self.__getCurrentDate()
        print("today", currentDate)
        dayDiff = util.getDayDifference(currentDate, cancelItemObj.getStartDate())
        print("day diff:", dayDiff)
        if dayDiff < 1:
            print("Sorry, its too late to cancel")
            self.__errorLabel.config(text=strings.cancelErrorMessage)
        else:
            print("Cancel in progress")
            # TODO remove booking #cancelItemObj#
            self.__errorLabel.config(text="")

    def populateData(self):
        """
        Gets data and populates all data in the list
        :return: None
        """

        self.__toolObjList = []
        self.__toolIDList = []

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
                                         self.__bookingList[i].getExpectedReturnDate()),
                                   tags=self.__bookingList[i].getBookingID())
