import tkinter as tk
from tkinter import ttk
from Resources.Values import strings, colors, dimens, fonts
from Code.Utilities import ReadFile as rf
import Code.test_printObj as test


# TODO Late returns page which will show information about that person who hired tool?
# TODO one more column which will represents item availability?
# TODO adjust error labels to show correct text if list is empty


class MyToolPage(tk.Frame):
    bgColor = colors.bgColor
    fgColor = colors.fgColor
    width = dimens.mainWindowWidth
    heigh = dimens.mainWindowHeigh
    login = ""

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.config(bg=colors.bgColor)
        self.controller = controller
        self.columnconfigure(0, weight=1)

        self.initUI()

    def start(self, args):
        self.__toolList = rf.getTool(True, "owner", self.controller.login)
        test.printToolObject(self.__toolList)
        menuFrame = self.controller.getMenuFrame(self)
        menuFrame.grid(row=0, column=0, sticky="WN")
        self.ThereWillBeYourLogic()
        self.__errorLabel.config(text="")
        self.populateData()

    def initUI(self):

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

        frame = tk.Frame(self, bg=self.bgColor)
        frame.grid(row=1, column=0, sticky="", pady=19)

        ####################################################################################################
        #                                            DISPLAY
        ####################################################################################################
        self.__errorLabel = tk.Label(frame, bg=colors.bgColor, fg=colors.errorColor)
        self.__errorLabel.grid(row=0, column=0, columnspan= 2, sticky="WN")

        self.__tree = ttk.Treeview(frame, columns=("Full day price", "Half day price"))

        self.yscrollbar = ttk.Scrollbar(frame, orient='vertical', command=self.__tree.yview)
        self.__tree.configure(yscrollcommand=self.yscrollbar.set)

        self.__tree.heading('#0', text=strings.toolTitle)
        self.__tree.heading('#1', text='Full day price')
        self.__tree.heading('#2', text='Half Day Price')
        self.__tree.column('#1', stretch=tk.YES)
        self.__tree.column('#2', stretch=tk.YES)
        self.__tree.column('#0', stretch=tk.YES)
        self.__tree.grid(row=1, column=0, columnspan=5, pady=20, sticky="N")

        self.yscrollbar.grid(row=1, column=5, pady=20, sticky='WNS')

        self.editButton = tk.Label(frame, text="Edit Tool", bg=colors.bgColor, fg=colors.fgColor,
                                   font=fonts.subMenuButtonFont)
        self.editButton.grid(row=2, column=0, padx=4, sticky="N")
        self.editButton.bind("<Button-1>", lambda event: self.__editTool())

        self.deleteButton = tk.Label(frame, text="Delete Tool", bg=colors.bgColor, fg=colors.fgColor,
                                     font=fonts.subMenuButtonFont)
        self.deleteButton.grid(row=2, column=1, padx=4, sticky="N")
        # deleteButton.bind("<Button-2>", lambda event: self.selectItem())

        self.damage_restoreButton = tk.Label(frame, text="Damage/Restore tool", bg=colors.bgColor, fg=colors.fgColor,
                                             font=fonts.subMenuButtonFont)
        self.damage_restoreButton.grid(row=2, column=2, padx=4, sticky="N")
        # damage_restoreButton.bind("<Button-2>", lambda event: self.selectItem())

    def __editTool(self):
        if self.__tree.focus():
            self.__errorLabel.config(text="")
            index = self.__getItemIDIndex()
            self.controller.show_frame(strings.addToolClass, self.__toolList[index])
            print("test")
        else:
            self.__errorLabel.config(text="select item first")
            print("select item first")

    def __getItemIDIndex(self):
        """
        :return: int(index of selected item)
        """

        curItem = self.__tree.focus()
        if curItem:
            index = None
            itemID = None

            for item in self.__tree.selection():
                itemID = self.__tree.item(item, "tag")

            for i in range(len(self.__toolList)):
                if self.__toolList[i].getID() in itemID:
                    index = i
                    break
            return index

    # Rename this function according to what you want to do
    def ThereWillBeYourLogic(self):
        """
        ###self.__toolList### = this is your main variable. It holds a list of objects (your tools)
        
        get items:
            for i in range(len(self.__toolList)):
                title = self.__toolList[i].getTitle()
                description = self.__toolList[i].getDescription()
                ...
                for more information check documentation on github
        """


    def populateData(self):
        """
        Populates all data in the list
        :return: None
        """

        for i in self.__tree.get_children():
            self.__tree.delete(i)

        if self.__toolList:
            for i in range(len(self.__toolList)):
                self.__tree.insert('', 'end', text=self.__toolList[i].getTitle(),
                                   values=("{}{}".format(strings.currency, self.__toolList[i].getPriceFullDay()),
                                         "{}{}".format(strings.currency, self.__toolList[i].getPriceHalfDay())),
                                   tags=self.__toolList[i].getID())
