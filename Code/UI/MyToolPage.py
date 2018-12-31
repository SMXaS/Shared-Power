import tkinter as tk
from tkinter import ttk
from Resources.Values import strings, colors, dimens, fonts
from Code.Utilities import ReadFile as rf
import Code.Utilities.util as util


class MyToolPage(tk.Frame):
    placeHolder = []
    bgColor = colors.bgColor
    fgColor = colors.fgColor
    width = dimens.mainWindowWidth
    heigh = dimens.mainWindowHeigh

    def __init__(self, parent, controller):
        """
        :param master: master
        :param arg: login
        """

        tk.Frame.__init__(self, parent)
        self.config(bg=colors.bgColor)
        self.controller = controller
        self.columnconfigure(0, weight=1)

        self.initUI()

    def start(self, args):
        self.toolList = rf.getTool(True, "owner", self.controller.login)
        self.ThereWillBeYourLogic()
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


        ####################################################################################################
        #                                            DISPLAY
        ####################################################################################################
        self.tree = ttk.Treeview(self, columns=("Full day price", "Half day price"))

        self.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscrollbar.set)

        self.tree.heading('#0', text='')
        self.tree.heading('#1', text='Your Booked Tools')
        self.tree.heading('#2', text='')
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.grid(row=1, column=1, columnspan=2, pady=20, sticky="N")

        self.yscrollbar.grid(row=1, column=4, pady=20, sticky='WNS')

        ####################################################################################################
        #                                           WIDGETS
        ####################################################################################################

        editButton = tk.Label(self, text="Edit Tool", bg=self.bgColor, fg=self.fgColor,
                              font='Helvetica 10 bold')
        editButton.grid(row=0, column=2, padx=1, pady=20, sticky="N")
        #editButton.bind("<Button-1>", lambda event: self.selectItem())

        deleteButton = tk.Label(self, text="Delete Tool", bg=self.bgColor, fg=self.fgColor,
                                font='Helvetica 10 bold')
        deleteButton.grid(row=2, column=2, padx=0, pady=10, sticky="N")

        #deleteButton.bind("<Button-2>", lambda event: self.selectItem())

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
                                 tags=self.toolList[i].getID())
