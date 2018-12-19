import MainMenu as mm
import tkinter as tk
from tkinter import ttk
import BookToolPage as bk
import Resources.Values.values as values
import util
import ReadFile as rf


class SearchToolPage(tk.Frame):
    placeHolder = []
    bgColor = values.bgColor
    fgColor = values.fgColor

    def __init__(self, master, arg):
        tk.Frame.__init__(self, master)
        self.login = arg

        self.owner = master.owner
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title('Search for Tool')

        self.initUI()
        self.retriveData()

    def initUI(self):
        print(self.login)
        self.master.columnconfigure(0, weight=1)

        backIMG = tk.PhotoImage(file="Resources/Drawable/btn_back.png")
        backButton = tk.Label(self, image=backIMG, bg=self.bgColor)
        backButton.image = backIMG
        backButton.bind("<Button-1>", lambda event: self.master.change_frame(mm.MainMenu, self.login))
        backButton.grid(row=0, column=0, sticky=tk.W)

        self.searchEntry = tk.Entry(self, width=80)
        self.searchEntry.grid(row=0, column=1, padx=5, pady=20, sticky="N")

        searchButton = tk.Label(self, text="Search", bg=self.bgColor, fg=self.fgColor,
                                font='Helvetica 10 bold')
        searchButton.grid(row=0, column=2)
        searchButton.bind("<Button-1>", lambda event: self.retriveData())

        self.tree = ttk.Treeview(self, columns=("Full day price", "Half day price"))

        self.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscrollbar.set)

        self.tree.heading('#0', text='Title')
        self.tree.heading('#1', text='Full day price')
        self.tree.heading('#2', text='Half day price')
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.grid(row=1, column=0, columnspan=3, pady=20, sticky="N")

        self.yscrollbar.grid(row=1, column=4, pady=20, sticky='WNS')
        self.yscrollbar.configure(command=self.tree.yview)

        hireIMG = tk.PhotoImage(file="Resources/Drawable/btn_hire.png")
        hireButton = tk.Label(self, image=hireIMG, bg=self.bgColor)
        hireButton.image = hireIMG
        hireButton.bind("<Button-1>", lambda event: self.selectItem())
        hireButton.grid(row=2, column=0, columnspan=3, padx=10, pady=40)

    def selectItem(self):
        curItem = self.tree.focus()
        if curItem:
            index = None
            itemID = None

            for item in self.tree.selection():
                itemID = self.tree.item(item, "tag")

            for i in range(len(self.placeHolder)):
                if self.placeHolder[i].getID() in itemID:
                    index = i
            tool = []
            tool.append(self.login)
            tool.append(self.placeHolder[index])
            self.master.change_frame(bk.BookToolPage, tool)


    def retriveData(self):
        self.placeHolder.clear()

        if not self.searchEntry.get():
            items = rf.getTool(False, "availability", "yes")
        else:
            titleList = rf.getTool(False, "title", self.searchEntry.get().lower())
            availableList = rf.getTool(False, "availability", "yes")
            sellerList = rf.getTool(False, "owner", self.searchEntry.get().lower())
            descriptionList = rf.getTool(False, "description", self.searchEntry.get().lower())
            items = list(set(titleList).intersection(availableList))

            for i in range(len(sellerList)):
                if not sellerList[i] in items:
                    items.append(sellerList[i])

            for i in range(len(descriptionList)):
                if not descriptionList[i] in items:
                    items.append(descriptionList[i])

        for i in range(len(items)):
            self.placeHolder.append(util.convertToObj(items[i]))
        self.populateData()

    def populateData(self):

        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.placeHolder:
            for i in range(len(self.placeHolder)):
                self.tree.insert('', 'end', text=self.placeHolder[i].getTitle(),
                                 values=(self.placeHolder[i].getPriceFullDay(),
                                         self.placeHolder[i].getPriceHalfDay()),
                                 tags=self.placeHolder[i].getID())
