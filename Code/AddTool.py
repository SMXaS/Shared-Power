from Entities.Tool import Tool
from Code.Utilities import util, WriteFile as wf
from Resources.Values import strings
import uuid


class AddTool:

    def __init__(self, login, errorLabel):
        """
        :param login: str(user's login)
        """

        self.__login = login
        self.__errorLabel = errorLabel

    def add(self, tool):
        """
        :param tool: list(item specifications)
        :return:
        """
        print("class: AddTool; method: add")
        isCorrect = self.__verifyTool(tool)
        if isCorrect:
            print("isCorrect")
            ID = uuid.uuid4()
            util.copyIMG(tool[6], strings.filePath_images, ID)
            newPath = "{}{}".format(strings.filePath_images, ID)
            myTool = Tool(ID, self.__login, tool[0], tool[1], tool[2], tool[3], tool[4], tool[5], newPath, "yes")
            wf.write(myTool, strings.filePath_tool, strings.fieldNames_tool)
            print("Tool has been added")

            return True
        else:
            return False

    def __verifyTool(self, tool):
        """

        :param tool: obj(tool)
        :return True or error code

        tool[0] = title
        tool[1] = description
        tool[2] = tool condition
        tool[3] = price full day
        tool[4] = price half day
        tool[5] = rider charge
        tool[6] = img path
        """

        for i in range(len(tool)):
            if not tool[i]:
                self.__errorLabel.config(text=strings.errorEmptyFields)
                return False
            if i == 3 or i == 4 or i == 5:
                if " " in tool[i]:
                    return strings.errorIncorrectPriceFormat

        if not (tool[3].isdigit() or tool[4].isdigit() or tool[5].isdigit()):
            self.__errorLabel.config(text=strings.errorIncorrectPriceFormat)
            return False

        if not util.verifyIMG(tool[6]):
            self.__errorLabel.config(text=strings.errorWrongImageFormat)
            return False

        if isinstance(util.verifyIMG(tool[6]), str):
            self.__errorLabel.config(text=strings.errorUnsupportedImageFormat)
            return False

        return True
