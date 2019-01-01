import tkinter as tk
from tkinter import ttk
from Resources.Values import strings, colors, dimens, fonts
from Code.Utilities import util, ReadFile as rf


class SearchToolPage(tk.Frame):
    toolList = []
    bgColor = colors.bgColor
    fgColor = colors.fgColor
    width = dimens.mainWindowWidth
    heigh = dimens.mainWindowHeigh

    def __init__(self, parent, controller):
        """
        :param master: master
        :param arg: login
        """
        self.login = controller.login
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.initUI()


    def start(self, args):
        if not args:
            for item in self.tree.selection():
                self.tree.selection_remove(item)

        self.retrieveData()

    def initUI(self):

        frame = tk.Frame(self, bg=self.bgColor)
        frame.grid(row=0, column=0, sticky="", pady=40)

        self.searchEntry = tk.Entry(frame, width=80)
        self.searchEntry.grid(row=0, column=1, padx=25, pady=20, sticky="N")

        searchButton = tk.Label(frame, text=strings.search, bg=self.bgColor, fg=self.fgColor,
                                font=fonts.buttonFont)
        searchButton.grid(row=0, column=2)
        searchButton.bind("<Button-1>", lambda event: self.retrieveData())

        self.tree = ttk.Treeview(frame, columns=(strings.priceDay, strings.priceHalfDay))

        self.yscrollbar = ttk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscrollbar.set)

        self.tree.heading('#0', text=strings.tool)
        self.tree.heading('#1', text=strings.priceDay)
        self.tree.heading('#2', text=strings.priceHalfDay)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.grid(row=1, column=1, columnspan=2, pady=20, sticky="N")

        self.yscrollbar.grid(row=1, column=4, pady=20, sticky='WNS')

        hireIMG = tk.PhotoImage(file=strings.buttonHire)
        hireButton = tk.Label(frame, image=hireIMG, bg=self.bgColor)
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

            for i in range(len(self.toolList)):
                if self.toolList[i].getID() in itemID:
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
            self.controller.show_frame(strings.bookToolClass, self.toolList[index])

    def retrieveData(self):
        """
        Retrieve all data from DB and populate it in the list

        :return: None
        """

        self.toolList.clear()

        if not self.searchEntry.get().lower():
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
            self.toolList.append(util.convertToObj(items[i]))
        self.populateData()

    def populateData(self):
        """
        Populates all data in the list
        :return: None
        """

        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.toolList:
            for i in range(len(self.toolList)):
                self.tree.insert('', 'end', text=self.toolList[i].getTitle(),
                                 values=(self.toolList[i].getPriceFullDay(),
                                         self.toolList[i].getPriceHalfDay()),
                                 tag=self.toolList[i].getID())
