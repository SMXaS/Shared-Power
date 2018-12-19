import tkinter as tk
import Resources.Values.values as values
import MainMenu as mm
import ReadFile as rf
import util

class MyToolPage(tk.Frame):
    placeHolder = []
    bgColor = values.bgColor
    fgColor = values.fgColor

    def __init__(self, master, arg):
        tk.Frame.__init__(self, master)
        self.login = arg
        self.master=master
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