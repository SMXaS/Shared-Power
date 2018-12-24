from Entities.Tool import Tool
from Code.Utilities import util, WriteFile as wf


class addTool:

    def __init__(self, owner):
        """
        :param owner: user's login
        """

        self.__owner = owner

    def add(self, item):
        destination = "Data/Images/"
        ID = util.generateID()
        util.copyIMG(item[5], destination, ID)
        newPath = "Data/Images/{}".format(ID)
        myTool = Tool(ID, self.__owner, item[0], item[1], item[2], item[3], item[4], newPath, "yes")
        wf.add_tool(myTool)
        print("Tool has been added")
