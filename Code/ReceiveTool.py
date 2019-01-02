import Code.Utilities.ReadFile as rf
import Code.test_printObj as test
import Code.Utilities.util as util
from Resources.Values import strings


class ReceiveTool:

    # TODO suggest to cancel if current date < hire date
    def __init__(self, tree, errorLabel, login):
        """
        :param tree: widget(treeView)
        :param login: str(user name)
        """

        self.__bookingList = []
        self.__tree = tree
        self.__errorLabel = errorLabel
        self.__login = login
        toolList = rf.getTool(True, "owner", self.__login)
        toolIDList = []

        #############################
        test.printToolObject(toolList)
        #############################

        for m in range(len(toolList)):
            toolIDList.append(toolList[m].getID())

        for i in range(len(toolList)):
            list = rf.getAllBookings("toolID", toolList[i].getID(), 1)

            for k in range(len(list)):
                if list[k].getToolID() in toolIDList:
                    print("yes")
                    self.__bookingList.append(list[k])

        ############################################
        test.printBookingObjects(self.__bookingList)
        ############################################

    def populateList(self):
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
                                           self.__bookingList[i].getExpectedReturnDate(),
                                           self.__bookingList[i].getStatus()),
                                   tags=self.__bookingList[i].getBookingID())

    def receiveItem(self):
        if self.__tree.focus():
            receiveItemObj = self.__bookingList[self.__getBookingIndex()]
            print(receiveItemObj.getStartDate())
            receiveItemObj.setStatus(strings.toolStatus[2])
            # TODO edit this object in DB
            # TODO refresh list
            # test list
            testlist = [receiveItemObj]
            test.printBookingObjects(testlist)
        else:
            # TODO error label
            pass

    def damageItem(self):
        if self.__tree.focus():
            damageBookingObj = self.__bookingList[self.__getBookingIndex()]
            print(damageBookingObj.getStartDate())
            toolID = damageBookingObj.getToolID()
            tool = rf.getTool(True, "ID", toolID)
            tool[0].setAvailability("no")
            test.printToolObject(tool)
            # TODO edit this object in DB
            # TODO refresh list
            # TODO cancel all bookings for this item
        else:
            # TODO error label
            pass

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