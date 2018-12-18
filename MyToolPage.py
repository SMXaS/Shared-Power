import tkinter as tk
import Resources.Values.values as values
import MainMenu as mm

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

        self.initUI()

    def initUI(self):
        ####################################################################################################
        # !!!Leave this button as an option to go back
        ####################################################################################################
        backButton = tk.Button(self, text="back", command= lambda: self.master.change_frame(mm.MainMenu, self.login))
        backButton.grid(row=0, column=0)
        ####################################################################################################

