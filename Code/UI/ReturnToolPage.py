import tkinter as tk
import Resources.Values.values as values
from Code.UI import MainMenu as mm
import Code.Utilities.ReadFile as rf
import Code.Utilities.util as util


class ReturnToolPage(tk.Frame):
    bgColor = values.bgColor
    fgColor = values.fgColor
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
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title('Return Tool')

        self.initUI()
        self.ThereWillBeYourLogic()

    def getData(self):
        for i in range(len(self.bookingList)):
            self.toolIDList.append(self.bookingList[i].getToolID())

        for i in range(len(self.toolIDList)):
            tool = rf.get_tool("ID", self.toolIDList[i])
            self.toolObjList.append(util.convertFromListToObj(tool))

    def initUI(self):
        ####################################################################################################
        # !!!Leave this button as an option to go back
        ####################################################################################################
        backButton = tk.Button(self, text="back", command= lambda: self.master.change_frame(mm.MainMenu, self.login))
        backButton.grid(row=0, column=0)
        ####################################################################################################

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






