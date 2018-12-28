from Entities.Tool import Tool
from Code.Utilities import util, WriteFile as wf
import Resources.Values.values as values


class addTool:

    def __init__(self, owner):
        """
        :param owner: user's login
        """

        self.__owner = owner

    def add(self, item):
        ID = util.generateID()
        util.copyIMG(item[5], values.filePath_images, ID)
        newPath = "{}{}".format(values.filePath_images, ID)
        myTool = Tool(ID, self.__owner, item[0], item[1], item[2], item[3], item[4], newPath, "yes")
        wf.write(myTool, values.filePath_tool, values.fieldNames_tool)
        print("Tool has been added")
