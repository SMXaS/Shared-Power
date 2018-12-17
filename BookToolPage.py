import tkinter as tk
import Resources.Values.values as values

class BookToolPage(tk.Frame):
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
        master.title('Search for Tool')

        self.initUI()

    def initUI(self):
        pass
        print(self.tool.getTitle())
