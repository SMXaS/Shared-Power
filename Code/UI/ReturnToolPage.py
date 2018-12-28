import tkinter as tk
from tkinter import ttk
import Resources.Values.values as values
from Code.UI import MainMenu as mm
import Code.Utilities.ReadFile as rf
import Code.Utilities.util as util


class ReturnToolPage(tk.Frame):
    bgColor = values.bgColor
    fgColor = values.fgColor
    width = values.mainWindowWidth
    heigh = values.mainWindowHeigh
    toolIDList = []
    toolObjList = []

    def __init__(self, master, arg):
        tk.Frame.__init__(self, master)
        ###################################
        # DO not change!
        ###################################
        self.login = arg
        self.bookingList = rf.getAllBookings("userName", self.login)
        ###################################
        self.master = master
        master.geometry("{}x{}+%d+%d".format(self.width, self.heigh) % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title('Return Tool')

        self.getData()
        self.initUI()
        self.populateData()
        self.ThereWillBeYourLogic()

    def getData(self):
        """
        Gets data from DB
        :return: None
        """

        for i in range(len(self.bookingList)):
            self.toolIDList.append(self.bookingList[i].getToolID())

        for i in range(len(self.toolIDList)):
            tool = rf.get_tool("ID", self.toolIDList[i])
            self.toolObjList.append(util.convertFromListToObj(tool))

    def initUI(self):
        ####################################################################################################
        # !!!Leave this button as an option to go back
        ####################################################################################################
        backButton = tk.Button(self, text=values.back, command= lambda: self.master.change_frame(mm.MainMenu, self.login))
        backButton.grid(row=0, column=0)
        ####################################################################################################

        self.tree = ttk.Treeview(self, columns=(values.priceDay, values.priceHalfDay))

        self.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscrollbar.set)

        self.tree.heading('#0', text=values.tool)
        self.tree.heading('#1', text=values.hireDate)
        self.tree.heading('#2', text=values.returnDate)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.grid(row=1, column=1, columnspan=2, pady=20, sticky="N")

        self.yscrollbar.grid(row=1, column=4, pady=20, sticky='WNS')

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
        Populates all data in the list
        :return: None
        """

        for i in self.tree.get_children():
            self.tree.delete(i)
        if self.bookingList:
            for i in range(len(self.bookingList)):
                toolDict = rf.get_tool("ID", self.toolIDList[i])
                tool = util.convertFromListToObj(toolDict)
                self.tree.insert('', 'end', text=tool.getTitle(),
                                 values=(self.bookingList[i].getStartDate(),
                                         self.bookingList[i].getExpectedReturnDate()),
                                 tags=self.bookingList[i].getToolID())

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






