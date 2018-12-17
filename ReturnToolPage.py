import tkinter as tk
from tkinter import Widget
import Resources.Values.values as values
import MainMenu as mm

class ReturnToolPage(tk.Frame):
    placeHolder = []
    bgColor = values.bgColor
    fgColor = values.fgColor

    def __init__(self, master, tool):
        tk.Frame.__init__(self, master)
        self.tool = tool
        self.master=master
        self.login = master.login
        self.owner = master.owner
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title('Return Tool')

        self.initUI()

    def initUI(self):
        ####################################################################################################
        # !!!Leave this button as an option to go back
        ####################################################################################################
        backButton = tk.Button(self, text="back", command= lambda: self.master.change_frame(mm.MainMenu))
        backButton.grid(row=0, column=0)
        ####################################################################################################

        # Sorry, you dont need listbox here
