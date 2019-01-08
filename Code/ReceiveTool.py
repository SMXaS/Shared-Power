import Code.Utilities.ReadFile as rf
import Code.test_printObj as test
import Code.Utilities.util as util
from Resources.Values import strings
import Code.Utilities.WriteFile as wf

"""
-------------------------------------------------------------------------------------------------------------------
This class shows a list with items, which need to be received (status = pending_receive. It allows item owner to 
    receive items from a customer. It also provides an option to declare item as a damaged which will lead into 
    all booking cancellation for a particular item
-------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------
*** Implementation:
----------------------------------------------------------------------
    class:
        @ 'your assigned name' = ReceiveTool(TreeView, Label, string)
            * Takes TreeView (widget for populating all data)
            * Takes Label (widget for error messages)
----------------------------------------------------------------------
    Methods:
        @ 'your assigned name'.populateList():
            - populates returned items
        @ 'your assigned name'.receiveItem():
            - marks item as received (changes booking status into "inventory") and refreshes the list
        @ 'your assigned name.damageItem():
            - marks item as damaged (changes tool availability into "no") and received (changes booking status into
                "inventory"), cancels all future bookings and refreshes the list       
"""


class ReceiveTool:

    def __init__(self, tree, errorLabel, login):
        """
        :param tree: widget(treeView)
        :param login: str(user name)
        """

        self.__bookingList = []
        self.__tree = tree
        self.__errorLabel = errorLabel
        self.__login = login

    def populateList(self):
        toolObjList = []
        toolIDList = []
        self.__bookingList = []

        toolList = rf.getTool(True, "owner", self.__login)

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

        for i in range(len(self.__bookingList)):
            toolIDList.append(self.__bookingList[i].getToolID())

        """
        for i in range(len(toolIDList)):
            tool = rf.get_tool("ID", toolIDList[i])
            toolObjList.append(util.convertFromListToObj(tool))
        """

        for i in self.__tree.get_children():
            self.__tree.delete(i)

        if self.__bookingList:
            for i in range(len(self.__bookingList)):
                toolDict = rf.get_tool("ID", toolIDList[i])
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
            wf.editBooking(receiveItemObj)
            self.populateList()
            # btn_search list
            testlist = [receiveItemObj]
            test.printBookingObjects(testlist)
        else:
            if self.getCount() > 0:
                self.__errorLabel.config(text=strings.errorSelectItem)
            else:
                self.__errorLabel.config(text=strings.errorEmptyList)

    def getCount(self):
        if self.__bookingList:
            return len(self.__bookingList)
        else:
            return 0

    def damageItem(self):
        if self.__tree.focus():
            damageBookingObj = self.__bookingList[self.__getBookingIndex()]
            print(damageBookingObj.getStartDate())
            toolID = damageBookingObj.getToolID()
            tool = rf.getTool(True, "ID", toolID)
            tool[0].setAvailability("no")
            test.printToolObject(tool)
            wf.editTool(tool[0])
            self.receiveItem()
            # TODO cancel all bookings for this item
        else:
            if self.getCount() > 0:
                self.__errorLabel.config(text=strings.errorSelectItem)
            else:
                self.__errorLabel.config(text=strings.errorEmptyList)

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
