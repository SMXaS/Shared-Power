import tkinter as tk
from tkinter import ttk
from Resources.Values import strings, colors, fonts
from Code.UI.ReturnToolPage import ReturnToolPage
from Code.UI.InvoicePage import InvoicePage
from Code.UI.MyToolPage import MyToolPage
from Code.UI.ReceiveToolPage import ReceiveToolPage
from Code.UI.AddToolPage import AddToolPage


class MyProfilePage(tk.Frame):

    __buttonList = []
    __subMenuButtonList = []
    __page_name = ""
    login = ""

    def __init__(self, parent, controller):
        self.controller = controller

        tk.Frame.__init__(self, parent)
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)
        self.__initUI()

    def start(self, args):
        self.login = self.controller.login
        self.show_frame(strings.myToolClass)

    def __initUI(self):

        menuFrame = tk.Frame(self, bg=colors.bgColor)
        menuFrame.grid(row=0, column=0, sticky="WEN")

        container = tk.Frame(self, bg=colors.bgColor)
        container.grid(row=1, column=0, pady=10, sticky="WES")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        myToolsButton = tk.Label(menuFrame, text=strings.menuMyTools, bg=colors.bgColor, fg=colors.fgColor,
                                 font=fonts.menuButtonFont)
        myToolsButton.grid(row=0, column=0, padx=10, pady=10, sticky="NW")
        myToolsButton.bind("<Button-1>", lambda event: self.show_frame(strings.myToolClass))

        menuBorderx1 = ttk.Separator(menuFrame, orient="vertical")
        menuBorderx1.grid(row=0, column=1, pady=2, sticky="NS")

        myBookinsButton = tk.Label(menuFrame, text=strings.menuMyBookings, bg=colors.bgColor, fg=colors.fgColor,
                                   font=fonts.menuButtonFont)
        myBookinsButton.grid(row=0, column=2, padx=10, pady=10, sticky="NW")
        myBookinsButton.bind("<Button-1>", lambda event: self.show_frame(strings.returnToolClass))

        menuBorderx2 = ttk.Separator(menuFrame, orient="vertical")
        menuBorderx2.grid(row=0, column=3, pady=2, sticky="NS")

        myInvoicesButton = tk.Label(menuFrame, text=strings.menuInvoice, bg=colors.bgColor, fg=colors.fgColor,
                                    font=fonts.menuButtonFont)
        myInvoicesButton.grid(row=0, column=4, padx=10, pady=10, sticky="NW")
        myInvoicesButton.bind("<Button-1>", lambda event: self.show_frame(strings.invoiceClass))

        menuBorderx2 = ttk.Separator(menuFrame, orient="vertical")
        menuBorderx2.grid(row=0, column=5, pady=2, sticky="NS")

        # menuBorderGround = ttk.Separator(menuFrame, orient="horizontal")
        # menuBorderGround.grid(row=1, column=0, columnspan=6, padx=2, sticky="WE")

       # viewLabel = tk.Label(container, text="test View Label")
        #viewLabel.grid(row=0, column=0, sticky="N")
        self.buttonList = (myToolsButton, myBookinsButton, myInvoicesButton)

        self.frames = {}

        for F in (MyToolPage, ReturnToolPage, InvoicePage, ReceiveToolPage, AddToolPage):
            self.__page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[self.__page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name, args=[]):
        """
        This is main function in order to change frames
        :param page_name: str(class name which you want to populate)
        :param args: **optional** list(whatever you want to send to the requested frame)
        :return: None
        """

        # pulling the requested frame
        frame = self.frames[page_name]
        frame.tkraise()
        self.__page_name = page_name

        # sending arguments and initializing logic
        frame.start(args)

        # adjusting menu button fonts
        self.checkButton()

    def checkButton(self):
        """
        This function checks which menu button is pressed (based on which frame is called) in order
        to highlight it. It will send buttonList index of that button to 'highlightButton' method
        :return: None
        """

        if self.__page_name is strings.myToolClass:
            self.highlightButton(0)
            self.highlightSubButton(0)
        elif self.__page_name is strings.returnToolClass:
            self.highlightButton(1)
        elif self.__page_name is strings.invoiceClass:
            self.highlightButton(2)
        elif self.__page_name is strings.addToolClass:
            self.highlightSubButton(1)
        elif self.__page_name is strings.receiveToolPage:
            self.highlightSubButton(2)

    def highlightSubButton(self, index):
        """
                This function changing fonts for all buttons based on the index
                :param index: int(buttonList index)
                :return: None
                """

        # looping through buttonList and looking for match.
        for i in range(len(self.__subMenuButtonList)):
            if index == i:
                self.__subMenuButtonList[i].config(font=fonts.subMenuButtonPressedFont)
            else:
                self.__subMenuButtonList[i].config(font=fonts.subMenuButtonFont)
    def highlightButton(self, index):
        """
        This function changing fonts for all buttons based on the index
        :param index: int(buttonList index)
        :return: None
        """

        # looping through buttonList and looking for match.
        for i in range(len(self.buttonList)):
            if index == i:
                self.buttonList[i].config(font=fonts.menuButtonPressedFont)
            else:
                self.buttonList[i].config(font=fonts.menuButtonFont)

    def getMenuFrame(self, frame):
        menuFrame = tk.Frame(frame, bg=colors.bgColor)


        self.myToolsButton = tk.Label(menuFrame, text=strings.menuMyTools, bg=colors.bgColor, fg=colors.fgColor,
                                 font=fonts.subMenuButtonFont)
        self.myToolsButton.grid(row=0, column=0, padx=4)
        if self.__page_name is not strings.myToolClass:
            self.myToolsButton.bind("<Button-1>", lambda event: self.show_frame(strings.myToolClass))

        self.receiveButton = tk.Label(menuFrame, text=strings.receiveItem, bg=colors.bgColor, fg=colors.fgColor,
                                      font=fonts.subMenuButtonFont)
        self.receiveButton.grid(row=0, column=1, padx=4)
        if self.__page_name is not strings.receiveToolPage:
            self.receiveButton.bind("<Button-1>", lambda event: self.show_frame(strings.receiveToolPage))

        menuBorderx = ttk.Separator(menuFrame, orient="vertical")
        menuBorderx.grid(row=0, column=2, pady=2, sticky="NS")

        self.addToolButton = tk.Label(menuFrame, text=strings.menuAddTool, bg=colors.bgColor, fg=colors.fgColor,
                                      font=fonts.subMenuButtonFont)
        self.addToolButton.grid(row=0, column=3, padx=4)
        if self.__page_name is not strings.addToolClass:
            self.addToolButton.bind("<Button-1>", lambda event: self.show_frame(strings.addToolClass))



        self.__subMenuButtonList = (self.myToolsButton, self.addToolButton, self.receiveButton)
        return menuFrame