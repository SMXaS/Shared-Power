import tkinter as tk
from tkinter import ttk
from Resources.Values import strings, colors, fonts
from Code.UI.MyBookingsPage import ReturnToolPage
from Code.UI.InvoicePage import InvoicePage
from Code.UI.MyToolPage import MyToolPage
from Code.UI.ReceiveToolPage import ReceiveToolPage
from Code.UI.AddToolPage import AddToolPage
from Code.UI.EmptyLayout import EmptyLayout


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

        menuFrame = tk.Frame(self, bg=colors.menuBgColor)
        menuFrame.grid(row=0, column=0, sticky="WEN")

        container = tk.Frame(self, bg=colors.bgColor)
        container.grid(row=2, column=0, pady=10, sticky="WES")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #######################################################
        # MyTool Frame
        #######################################################

        myToolsFrame = tk.Frame(menuFrame, bg=colors.menuBgColor)
        myToolsFrame.grid(row=0, column=0, sticky="NW")
        myToolsFrame.columnconfigure(0, minsize=100)

        toolIMG = tk.PhotoImage(file=strings.tool_img)
        tool = tk.Label(myToolsFrame, image=toolIMG, bg=colors.menuBgColor)
        tool.image = toolIMG
        tool.grid(row=0, column=0, padx=5, pady=2, sticky="WENS")

        myToolsButton = tk.Label(myToolsFrame, text=strings.menuMyTools, bg=colors.menuBgColor, fg=colors.fgColor,
                                 font=fonts.menuButtonFont)
        myToolsButton.grid(row=1, column=0, padx=10, pady=2, sticky="WES")

        myToolsFrame.bind("<Button-1>", lambda event: self.__verifyFrame(strings.myToolClass))
        tool.bind("<Button-1>", lambda event: self.__verifyFrame(strings.myToolClass))
        myToolsButton.bind("<Button-1>", lambda event: self.__verifyFrame(strings.myToolClass))

        menuBorderx1 = ttk.Separator(menuFrame, orient="vertical")
        menuBorderx1.grid(row=0, column=1, pady=2, sticky="NS")

        #######################################################
        # MyBookings Frame
        #######################################################

        myBookingsFrame = tk.Frame(menuFrame, bg=colors.menuBgColor)
        myBookingsFrame.grid(row=0, column=2, sticky="NW")
        myBookingsFrame.columnconfigure(0, minsize=100)

        bookingIMG = tk.PhotoImage(file=strings.bookings_img)
        booking = tk.Label(myBookingsFrame, image=bookingIMG, bg=colors.menuBgColor)
        booking.image = bookingIMG
        booking.grid(row=0, column=0, padx=5, pady=8, sticky="WENS")

        myBookinsButton = tk.Label(myBookingsFrame, text=strings.menuMyBookings, bg=colors.menuBgColor,
                                   fg=colors.fgColor, font=fonts.menuButtonFont)
        myBookinsButton.grid(row=1, column=0, padx=10, pady=2, sticky="WES")

        myBookingsFrame.bind("<Button-1>", lambda event: self.__verifyFrame(strings.returnToolClass))
        booking.bind("<Button-1>", lambda event: self.__verifyFrame(strings.returnToolClass))
        myBookinsButton.bind("<Button-1>", lambda event: self.__verifyFrame(strings.returnToolClass))

        menuBorderx2 = ttk.Separator(menuFrame, orient="vertical")
        menuBorderx2.grid(row=0, column=3, pady=2, sticky="NS")

        #######################################################
        # myInvoice Frame
        #######################################################

        myInvoiceFrame = tk.Frame(menuFrame, bg=colors.menuBgColor)
        myInvoiceFrame.grid(row=0, column=4, sticky="NW")
        myInvoiceFrame.columnconfigure(0, minsize=100)

        invoiceIMG = tk.PhotoImage(file=strings.invoice_img)
        invoice = tk.Label(myInvoiceFrame, image=invoiceIMG, bg=colors.menuBgColor)
        invoice.image = invoiceIMG
        invoice.grid(row=0, column=0, padx=5, pady=8, sticky="WENS")

        myInvoicesButton = tk.Label(myInvoiceFrame, text=strings.menuInvoice, bg=colors.menuBgColor, fg=colors.fgColor,
                                    font=fonts.menuButtonFont)
        myInvoicesButton.grid(row=1, column=0, padx=10, pady=2, sticky="NWE")

        myInvoiceFrame.bind("<Button-1>", lambda event: self.__verifyFrame(strings.invoiceClass))
        invoice.bind("<Button-1>", lambda event: self.__verifyFrame(strings.invoiceClass))
        myInvoicesButton.bind("<Button-1>", lambda event: self.__verifyFrame(strings.invoiceClass))

        menuBorderx2 = ttk.Separator(menuFrame, orient="vertical")
        menuBorderx2.grid(row=0, column=5, pady=2, sticky="NS")

        #######################################################
        # addTool Frame
        #######################################################

        addToolFrame = tk.Frame(menuFrame, bg=colors.menuBgColor)
        addToolFrame.grid(row=0, column=6, sticky="NW")
        addToolFrame.columnconfigure(0, minsize=100)

        addIMG = tk.PhotoImage(file=strings.add_img)
        add = tk.Label(addToolFrame, image=addIMG, bg=colors.menuBgColor)
        add.image = addIMG
        add.grid(row=0, column=0, padx=5, pady=8, sticky="WENS")

        self.addToolButton = tk.Label(addToolFrame, text=strings.menuAddTool, bg=colors.menuBgColor, fg=colors.fgColor,
                                      font=fonts.menuButtonFont)
        self.addToolButton.grid(row=1, column=0, padx=10, pady=2, sticky="NWE")

        if self.__page_name != strings.addToolClass:
            add.bind("<Button-1>", lambda event: self.__verifyFrame(strings.addToolClass))
            addToolFrame.bind("<Button-1>", lambda event: self.__verifyFrame(strings.addToolClass))
            self.addToolButton.bind("<Button-1>", lambda event: self.__verifyFrame(strings.addToolClass))

        # menuBorderGround = ttk.Separator(menuFrame, orient="horizontal")
        # menuBorderGround.grid(row=1, column=0, columnspan=6, padx=2, sticky="WE")

        self.buttonList = (myToolsButton, myBookinsButton, myInvoicesButton, self.addToolButton)
        self.labelList = (tool, booking, invoice, add)
        self.frameList = (myToolsFrame, myBookingsFrame, myInvoiceFrame, addToolFrame)

        self.frames = {}

        for F in (MyToolPage, ReturnToolPage, InvoicePage, ReceiveToolPage, AddToolPage, EmptyLayout):
            self.__page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[self.__page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def __verifyFrame(self, destinationPage, args=[]):
        """
        This method checks if active frame is the same as destination frame
        :param destinationPage: str(Class name)
        :param args: list (optional - what you want to send to destination Page)
        :return: None
        """

        if self.__page_name != destinationPage:
            self.show_frame(destinationPage, args)

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

        print("show frame args:", args)
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
            self.highlightButton(3)
        elif self.__page_name is strings.receiveToolPage:
            self.highlightSubButton(1)

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
                self.buttonList[i].config(bg=colors.bgColor, font=fonts.subMenuButtonPressedFont)
                self.labelList[i].config(bg=colors.bgColor)
                self.frameList[i].config(bg=colors.bgColor)
            else:
                self.buttonList[i].config(bg=colors.menuBgColor, font=fonts.subMenuButtonFont)
                self.labelList[i].config(bg=colors.menuBgColor)
                self.frameList[i].config(bg=colors.menuBgColor)

    def getMenuFrame(self, frame):
        menuFrame = tk.Frame(frame, bg=colors.bgColor)
        menuFrame.columnconfigure(0, minsize=80)
        menuFrame.columnconfigure(2, minsize=80)

        self.myToolsButton = tk.Label(menuFrame, text=strings.menuMyTools, bg=colors.bgColor, fg=colors.fgColor,
                                      font=fonts.subMenuButtonFont)
        self.myToolsButton.grid(row=0, column=0, padx=4)
        if self.__page_name is not strings.myToolClass:
            self.myToolsButton.bind("<Button-1>", lambda event: self.show_frame(strings.myToolClass))

        menuBorderx = ttk.Separator(menuFrame, orient="vertical")
        menuBorderx.grid(row=0, column=1, pady=2, sticky="NS")

        self.receiveButton = tk.Label(menuFrame, text=strings.receiveItem, bg=colors.bgColor, fg=colors.fgColor,
                                      font=fonts.subMenuButtonFont)
        self.receiveButton.grid(row=0, column=2, padx=10)
        if self.__page_name is not strings.receiveToolPage:
            self.receiveButton.bind("<Button-1>", lambda event: self.show_frame(strings.receiveToolPage))

        self.__subMenuButtonList = (self.myToolsButton, self.receiveButton)
        return menuFrame