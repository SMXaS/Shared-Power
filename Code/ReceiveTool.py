import Code.Utilities.ReadFile as rf
import Code.test_printObj as test
import Code.Utilities.util as util

class ReceiveTool:

    def __init__(self, tree, login):
        """
        :param tree: widget(treeView)
        :param login: str(user name)
        """
        self.__bookingList = []
        self.__tree = tree
        self.__login = login
        toolList = rf.getTool(True, "owner", self.__login)
        for i in range(len(toolList)):
            list = rf.getAllBookings("toolID", toolList[i].getID(), 1)
            for k in range(len(list)):
                self.__bookingList.append(list[k])

        test.printBookingObjects(self.__bookingList)

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
