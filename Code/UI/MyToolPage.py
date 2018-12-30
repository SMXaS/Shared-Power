import tkinter as tk
import Resources.Values.values as values
from Code.UI import MainMenu as mm
from Code.Utilities import ReadFile as rf


class MyToolPage(tk.Frame):
    placeHolder = []
    bgColor = values.bgColor
    fgColor = values.fgColor
    width = values.mainWindowWidth
    heigh = values.mainWindowHeigh

    def __init__(self, parent, controller):
        """
        :param master: master
        :param arg: login
        """

        tk.Frame.__init__(self, parent)
        self.config(bg=values.bgColor)
        self.columnconfigure(0, weight=1)

        self.toolList = rf.getTool(True, "owner", "test")

        self.initUI()
        self.ThereWillBeYourLogic()

    def start(self, args):
        pass

    def initUI(self):

        """
        Store all your widgets here
        i.e.:
            self.myLabel = tk.Label(self, text="my first label")
            self.myLabel.grid(row=1, column=0)

            self.myButton = tk.Button(self, text="my first button")
            self.myButton.grid(row=1, column=1)


        add functionality to your buttons:
            when you define a button, add this text:
                ###  command=lambda: 'your function' ### (check how backButton is made)

        add functionality to your labels:
            self.myLabel.bind("<Button-1>", lambda event: '/your function/' )

        """

    # Rename this function according to what you want to do
    def ThereWillBeYourLogic(self):
        for i in range(len(self.toolList)):
            print(self.toolList[i].getTitle())

        """
        ###self.toolList### = this is your main variable. It holds a list of objects (your tools)
        
        get items:
            for i in range(len(self.toolList)):
                self.toolList[i].getTitle()
                self.toolList[i].getDescription()
                ...
                for more information check documentation on github
        """