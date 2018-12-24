import tkinter as tk
import Resources.Values.values as values
from Code.UI import MainMenu as mm
from Code.Utilities import ReadFile as rf


class MyToolPage(tk.Frame):
    placeHolder = []
    bgColor = values.bgColor
    fgColor = values.fgColor

    def __init__(self, master, arg):
        """
        :param master: master
        :param arg: login
        """

        tk.Frame.__init__(self, master)
        self.login = arg
        self.master = master
        self.owner = master.owner
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title('My Tools')
        self.toolList = rf.getTool(True, "owner", self.login)

        self.initUI()
        self.ThereWillBeYourLogic()

    def initUI(self):
        ####################################################################################################
        # !!!Leave this button as an option to go back
        ####################################################################################################
        backButton = tk.Button(self, text="back", command= lambda: self.master.change_frame(mm.MainMenu, self.login))
        backButton.grid(row=0, column=0)
        ####################################################################################################

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