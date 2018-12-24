import tkinter as tk
import Resources.Values.values as values
from Code.UI import MainMenu as mm


class ReturnToolPage(tk.Frame):
    placeHolder = []
    bgColor = values.bgColor
    fgColor = values.fgColor

    def __init__(self, master, tool):
        tk.Frame.__init__(self, master)
        ###################################
        # DO not change!
        ###################################
        self.login = tool[0]
        self.tool = tool[1]
        ###################################
        self.master = master
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title('Return Tool')

        self.initUI()
        self.ThereWillBeYourLogic()

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
        ###self.tool### = this is your main variable. It holds an object (booking)

        get items:
            self.tool.getToolID()
            self.tool.getExpectedReturnDate()
            ...
            for more information check documentation on github
        """