from Entities.Tool import Tool
import WriteFile as wf
import util
import imghdr


class addTool:

    def __init__(self, owner):
        self.__owner = owner

    def add(self, item):
        destination = "Data/Images/"
        ID = util.generateID()
        util.copyIMG(item[4], destination, ID)
        newPath = "Data/Images/{}".format(ID)
        myTool = Tool(ID, self.__owner, item[0], item[1], item[2], item[3], newPath, "yes")
        wf.add_tool(myTool)
        print("Tool has been added")
