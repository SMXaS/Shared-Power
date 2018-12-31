import tkinter as tk
from tkinter import ttk
from Resources.Values import strings, colors, dimens, fonts
import Code.Utilities.ReadFile as rf
import Code.Utilities.util as util


class ReturnToolPage(tk.Frame):
    bgColor = colors.bgColor
    fgColor = colors.fgColor
    toolIDList = []
    toolObjList = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        ###################################
        # DO not change!
        ###################################

        ###################################

        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.initUI()

    def start(self, args):
        self.login = self.controller.login
        self.bookingList = rf.getAllBookings("userName", self.login)
        self.populateData()
        self.ThereWillBeYourLogic()

    def initUI(self):

        frame = tk.Frame(self, bg=self.bgColor)
        frame.grid(row=0, column=0, sticky="", pady=40)

        self.tree = ttk.Treeview(frame, columns=(strings.priceDay, strings.priceHalfDay))

        self.yscrollbar = ttk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscrollbar.set)

        self.tree.heading('#0', text=strings.tool)
        self.tree.heading('#1', text=strings.hireDate)
        self.tree.heading('#2', text=strings.returnDate)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.grid(row=0, column=0, columnspan=2, pady=20, sticky="N")

        self.yscrollbar.grid(row=0, column=3, pady=20, sticky='WNS')

        self.returnButton = tk.Label(frame, text=strings.returnItem, bg=colors.bgColor, fg=colors.fgColor,
                                     font=fonts.buttonFont)
        self.returnButton.rowconfigure(0, weight=1)
        self.returnButton.grid(row=1, column=0, columnspan=2)
        self.returnButton.bind("<Button-1>", lambda event: self.returnItem())

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

    def populateData(self):
        """
        Gets data and populates all data in the list
        :return: None
        """

        for i in range(len(self.bookingList)):
            self.toolIDList.append(self.bookingList[i].getToolID())

        for i in range(len(self.toolIDList)):
            tool = rf.get_tool("ID", self.toolIDList[i])
            self.toolObjList.append(util.convertFromListToObj(tool))

        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.bookingList:
            for i in range(len(self.bookingList)):
                toolDict = rf.get_tool("ID", self.toolIDList[i])
                tool = util.convertFromListToObj(toolDict)
                self.tree.insert('', 'end', text=tool.getTitle(),
                                 values=(self.bookingList[i].getStartDate(),
                                         self.bookingList[i].getExpectedReturnDate()),
                                 tags=self.bookingList[i].getBookingID())

    def returnItem(self):
        curItem = self.tree.focus()
        index = None
        if curItem:
            itemID = None
            for item in self.tree.selection():
                itemID = self.tree.item(item, "tag")

            for i in range(len(self.bookingList)):
                if self.bookingList[i].getBookingID() in itemID:
                    index = i
                    break

            returnItemObj = self.bookingList[index]

            # toolStatus[1] = "pending_receive"
            returnItemObj.setStatus(strings.toolStatus[1])

            print("new status:", returnItemObj.getStatus())

    # Rename this function according to what you want to do
    def ThereWillBeYourLogic(self):
        """
        ###self.bookingList### = this is your main variable. It holds an list of objects (booking)

        # get bookings:
            for i in range(len(self.bookingList):
                self.bookingList[i].getToolID()
                self.bookingList[i].getExpectedReturnDate()
                ...
            for more information check documentation on github

        # get tool by ID:
            toolDict = rf.get_tool("ID", self.toolIDList[i])  // "i" indicates index in the list from where
                                                                     you will take tool ID

            tool = util.convertFromListToObj(toolDict)


        # Extract tool information:
            title = tool.getTitle()
            owner = tool.getOwner()
            description = tool.getDescription()
            ...
        """






