from Code.UI import MainMenu as mm, BookToolPage as bk
import tkinter as tk
from tkinter import ttk
import Resources.Values.values as values
from Code.Utilities import util, ReadFile as rf


class SearchToolPage(tk.Frame):
    placeHolder = []
    bgColor = values.bgColor
    fgColor = values.fgColor
    width = values.mainWindowWidth
    heigh = values.mainWindowHeigh

    def __init__(self, master, arg):
        """
        :param master: master
        :param arg: login
        """

        tk.Frame.__init__(self, master)
        self.login = arg

        self.owner = master.owner
        master.geometry("{}x{}+%d+%d".format(self.width, self.heigh) % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title(values.searchToolTitle)

        self.initUI()
        self.retrieveData()

    def initUI(self):

        backIMG = tk.PhotoImage(file=values.buttonBack)
        backButton = tk.Label(self, image=backIMG, bg=self.bgColor)
        backButton.image = backIMG
        backButton.bind("<Button-1>", lambda event: self.master.change_frame(mm.MainMenu, self.login))
        backButton.grid(row=0, column=0, padx=10, sticky=tk.W)

        self.searchEntry = tk.Entry(self, width=80)
        self.searchEntry.grid(row=0, column=1, padx=25, pady=20, sticky="N")

        searchButton = tk.Label(self, text=values.search, bg=self.bgColor, fg=self.fgColor,
                                font=values.buttonFont)
        searchButton.grid(row=0, column=2)
        searchButton.bind("<Button-1>", lambda event: self.retrieveData())

        self.tree = ttk.Treeview(self, columns=(values.priceDay, values.priceHalfDay))

        self.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscrollbar.set)

        self.tree.heading('#0', text=values.tool)
        self.tree.heading('#1', text=values.priceDay)
        self.tree.heading('#2', text=values.priceHalfDay)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.grid(row=1, column=1, columnspan=2, pady=20, sticky="N")

        self.yscrollbar.grid(row=1, column=4, pady=20, sticky='WNS')

        hireIMG = tk.PhotoImage(file=values.buttonHire)
        hireButton = tk.Label(self, image=hireIMG, bg=self.bgColor)
        hireButton.image = hireIMG
        hireButton.bind("<Button-1>", lambda event: self.selectItem())
        hireButton.grid(row=2, column=0, columnspan=3, padx=10, pady=40)

    def getItemIDIndex(self):
        """
        :return: int(index of selected item)
        """

        curItem = self.tree.focus()
        if curItem:
            index = None
            itemID = None

            for item in self.tree.selection():
                itemID = self.tree.item(item, "tag")

            for i in range(len(self.placeHolder)):
                if self.placeHolder[i].getID() in itemID:
                    index = i
                    break
            return index

    def selectItem(self):
        """
        Select item and go to BookToolPage

        :return: None
        """

        curItem = self.tree.focus()
        if curItem:
            index = self.getItemIDIndex()
            tool = []
            tool.append(self.login)
            tool.append(self.placeHolder[index])
            self.master.change_frame(bk.BookToolPage, tool)

    def retrieveData(self):
        """
        Retrieve all data from DB and populate it in the list

        :return: None
        """

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
        """
        Populates all data in the list
        :return: None
        """

        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.placeHolder:
            for i in range(len(self.placeHolder)):
                self.tree.insert('', 'end', text=self.placeHolder[i].getTitle(),
                                 values=(self.placeHolder[i].getPriceFullDay(),
                                         self.placeHolder[i].getPriceHalfDay()),
                                 tags=self.placeHolder[i].getID())
