from Entities.Tool import Tool
import util
import WriteFile as wf


class addTool:

    def __init__(self, owner):
        self.__owner = owner

    def add(self, item):
        ID = util.generateID()
        toolOwner = self.__owner.getUserName()
        #toolOwner = "kvarcas91"
        
        """
        title = "ToolName1"
        description = "Where's Stefan 1"
        dayPrice = 9.89
        halfDayPrice = 6.99
        imagePath = "images/sendMeNudes.jpeg"
        available = True

        tool = Tool(ID, toolOwner, title, description, dayPrice, halfDayPrice, imagePath, available)
        """
       
        isCorrect = util.verifyTool(item)
        if isCorrect:
            print("Tool has been added")

        """
    def printTool(self, tool):
        print(tool.getOwner())
        """

