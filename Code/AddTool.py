from Entities.Tool import Tool
from Code.Utilities import util, WriteFile as wf
from Resources.Values import strings
import uuid
import os
import shutil
from shutil import copy2

"""
----------------------------------------------------------------------------------------------------------------------
This class allows user to Add Tool. First it will check if all entries are correct:
   * entries shouldn't be empty
   * currency fields shouldn't take strings
   * image must be .png
If requirements match - it will build an object and send it to WriteFile class to write it into a Data/tools.csv file
----------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------
***Implementation:
----------------------------------------------------------------
    class: 
        @ 'your assigned name' = AddTool(string, Label widget):
            * takes str(userName)
            * takes widget(label for error messages)
----------------------------------------------------------------
    methods:
        @ 'your assigned name'.add(list):
            * takes list as a parameter where is all entries about the tool
            - Adds tool to the database
            * will return boolean value:
                True - file was added into database
                False - there was an error and it was highlighted 
"""


class AddTool:

    def __init__(self, login, errorLabel):
        """
        :param login: str(user's login)
        :param errorLabel: widget(for setting up errors)
        """

        self.__login = login
        self.__errorLabel = errorLabel

    def add(self, tool, editOrAdd):
        """
        :param tool: list(item specifications)
        :param editOrAdd: boolean value where True = add Tool and False = edit Tool
        :return: boolean
        """
        availability = "yes"
        isCorrect = self.__verifyTool(tool)
        if isCorrect:
            if editOrAdd:
                ID = uuid.uuid4()
                util.copyIMG(tool[6], strings.filePath_images, ID)
            else:
                ID = tool[7]
                copy2(tool[6], "{}{}_temp.png".format(strings.filePath_images, ID))
                shutil.move(os.path.join(strings.filePath_images, "{}_temp.png".format(ID)),
                            os.path.join(strings.filePath_images, ID+".png"))
                availability = "no"

            newPath = "{}{}".format(strings.filePath_images, ID)
            myTool = Tool(ID, self.__login, tool[0], tool[1], tool[2], tool[3], tool[4], tool[5], newPath, availability)
            if editOrAdd:
                wf.write(myTool, strings.filePath_tool, strings.fieldNames_tool)
            else:
                wf.editTool(myTool)
                print("edit")
            print("Tool has been added")

            return True
        else:
            return False

    def __verifyTool(self, tool):
        """
        :param tool: obj(tool)
        :return boolean

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

        if not (tool[3].isdigit() and tool[4].isdigit() and tool[5].isdigit()):
            self.__errorLabel.config(text=strings.errorIncorrectPriceFormat)
            return False

        if not util.verifyIMG(tool[6]):
            self.__errorLabel.config(text=strings.errorWrongImageFormat)
            return False

        if isinstance(util.verifyIMG(tool[6]), str):
            self.__errorLabel.config(text=strings.errorUnsupportedImageFormat)
            return False

        return True
