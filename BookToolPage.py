import tkinter as tk
import SearchToolPage as sp
import Resources.Values.values as values

class BookToolPage(tk.Frame):
    placeHolder = []
    bgColor = values.bgColor
    fgColor = values.fgColor

    def __init__(self, master, tool):
        self.login = tool[0]
        tk.Frame.__init__(self, master)

        self.tool = tool[1]
        self.master=master
        self.owner = master.owner
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title('Search for Tool')

        self.initUI()

    def initUI(self):
        backButton = tk.Button(self, text="back", command=lambda: self.master.change_frame(sp.SearchToolPage, self.login))
        backButton.grid(row=0, column=0)
        print(self.tool.getTitle())
