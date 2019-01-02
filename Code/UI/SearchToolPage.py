import tkinter as tk
from tkinter import ttk
from Resources.Values import strings, colors, dimens, fonts
from Code.Utilities import util, ReadFile as rf
import Code.test_printObj as test


class SearchToolPage(tk.Frame):
    __toolList = []
    __bgColor = colors.bgColor
    __fgColor = colors.fgColor
    __width = dimens.mainWindowWidth
    __heigh = dimens.mainWindowHeigh

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__login = controller.login
        self.__controller = controller
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.__initUI()


    def start(self, args):
        if not args:
            for item in self.tree.selection():
                self.tree.selection_remove(item)

        self.__retrieveData()
        test.printToolObject(self.__toolList)

    def __initUI(self):
        frame = tk.Frame(self, bg=self.__bgColor)
        frame.grid(row=0, column=0, sticky="", pady=40)

        self.searchEntry = tk.Entry(frame, width=80)
        self.searchEntry.grid(row=0, column=1, padx=25, pady=20, sticky="N")

        searchButton = tk.Label(frame, text=strings.search, bg=self.__bgColor, fg=self.__fgColor,
                                font=fonts.buttonFont)
        searchButton.grid(row=0, column=2)
        searchButton.bind("<Button-1>", lambda event: self.__retrieveData())

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

        toolInfoButton = tk.Label(frame, text=strings.toolInfo, bg=self.__bgColor, fg=self.__fgColor,
                                  font=fonts.toolInfoFont)
        toolInfoButton.grid(row=2, column=1, columnspan=2, sticky="E")
        toolInfoButton.bind("<Button-1>", lambda event: self.__selectItem(False))

        hireIMG = tk.PhotoImage(file=strings.buttonHire)
        hireButton = tk.Label(frame, image=hireIMG, bg=self.__bgColor)
        hireButton.image = hireIMG
        hireButton.bind("<Button-1>", lambda event: self.__selectItem(True))
        hireButton.grid(row=3, column=0, columnspan=3, padx=10, pady=40)

    def __getItemIDIndex(self):
        """
        :return: int(index of selected item)
        """

        curItem = self.tree.focus()
        if curItem:
            index = None
            itemID = None

            for item in self.tree.selection():
                itemID = self.tree.item(item, "tag")

            for i in range(len(self.__toolList)):
                if self.__toolList[i].getID() in itemID:
                    index = i
                    break
            return index

    def __selectItem(self, boolBook):
        """
        Select item and go to BookToolPage

        :return: None
        """

        curItem = self.tree.focus()
        if curItem:
            index = self.__getItemIDIndex()
            if boolBook:
                self.__controller.show_frame(strings.bookToolClass, self.__toolList[index])
            else:
                self.__controller.show_frame(strings.toolInfoPage, self.__toolList[index])

    def __retrieveData(self):
        """
        Retrieve all data from DB and populate it in the list

        :return: None
        """

        self.__toolList.clear()

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
            self.__toolList.append(util.convertToObj(items[i]))
        self.__populateData()

    def __populateData(self):
        """
        Populates all data in the list
        :return: None
        """

        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.__toolList:
            for i in range(len(self.__toolList)):
                self.tree.insert('', 'end', text=self.__toolList[i].getTitle(),
                                 values=(self.__toolList[i].getPriceFullDay(),
                                         self.__toolList[i].getPriceHalfDay()),
                                 tag=self.__toolList[i].getID())
