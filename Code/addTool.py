from Entities.Tool import Tool
from Code.Utilities import util, WriteFile as wf
from Resources.Values import strings


class addTool:

    def __init__(self, owner):
        """
        :param owner: user's login
        """

        self.__owner = owner

    def add(self, item):
        """

        :param item: list(item specifications)
        :return:
        """
        ID = util.generateID()
        util.copyIMG(item[5], strings.filePath_images, ID)
        newPath = "{}{}".format(strings.filePath_images, ID)
        myTool = Tool(ID, self.__owner, item[0], item[1], item[2], item[3], item[4], newPath, "yes")
        wf.write(myTool, strings.filePath_tool, strings.fieldNames_tool)
        print("Tool has been added")
