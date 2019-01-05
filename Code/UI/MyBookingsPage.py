import tkinter as tk
from tkinter import ttk
from Resources.Values import strings, colors, fonts
from Code.MyBookings import MyBookings


class ReturnToolPage(tk.Frame):

    __bgColor = colors.bgColor
    __fgColor = colors.fgColor

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__controller = controller
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.__initUI()

    def start(self, args):
        self.__returnTool = MyBookings(self.__errorLabel, self.__tree, self.__controller.login)
        self.__controller.addToolButton.config(text=strings.menuAddTool)
        self.__returnTool.populateData()

        if self.__returnTool.getCount() > 0:
            self.__errorLabel.config(text="")
            self.__showReturn(False)
        else:
            self.__controller.show_frame(strings.emptyLayout)
            self.__controller.highlightButton(1)

    def __initUI(self):

        """
        ReturnToolPage UI.
        main functions which you can call:
            self.returnTool.cancelBooking()  --     will cancel booking based on your selection
            self.returnTool.returnItem()     --     will return an item based on your selection
            self.returnTool.populateData()   --     will populate all required data in your treeView
        """

        menuFrame = tk.Frame(self, bg=self.__bgColor)
        menuFrame.grid(row=0, column=0, sticky="WN")

        showReturnFrame = tk.Label(menuFrame, text=strings.returnItem, bg=colors.bgColor, fg=colors.fgColor,
                                   font=fonts.subMenuButtonFont)
        showReturnFrame.grid(row=0, column=0, padx=5)
        showReturnFrame.bind("<Button-1>", lambda event: self.__showReturn(True))

        menuBorderx = ttk.Separator(menuFrame, orient="vertical")
        menuBorderx.grid(row=0, column=1, pady=2, sticky="NS")

        cancelButton = tk.Label(menuFrame, text=strings.cancelBooking, bg=colors.bgColor, fg=colors.fgColor,
                                font=fonts.subMenuButtonFont)
        cancelButton.grid(row=0, column=2, padx=5)
        cancelButton.bind("<Button-1>", lambda event: self.__returnTool.cancelBooking())

        frame = tk.Frame(self, bg=self.__bgColor)
        frame.grid(row=1, column=0, sticky="", pady=19)

        frame.rowconfigure(2, minsize=30)
        frame.rowconfigure(4, weight=1)

        self.__tree = ttk.Treeview(frame, columns=(strings.priceDay, strings.priceHalfDay, "btn_search"))

        mScrollBar = ttk.Scrollbar(frame, orient='vertical', command=self.__tree.yview)
        self.__tree.configure(yscrollcommand=mScrollBar.set)

        self.__errorLabel = tk.Label(frame, bg=colors.bgColor, fg=colors.errorColor)
        self.__errorLabel.grid(row=0, column=0, columnspan=2, sticky="WN")

        self.__tree.heading('#0', text=strings.tool)
        self.__tree.heading('#1', text=strings.hireDate)
        self.__tree.heading('#2', text=strings.returnDate)
        self.__tree.heading('#3', text="state")
        self.__tree.column('#1', minwidth=20, width=150, stretch=tk.YES)
        self.__tree.column('#2', minwidth=20, width=150, stretch=tk.YES)
        self.__tree.column('#0', minwidth=20, width=150, stretch=tk.YES)
        self.__tree.column('#3', minwidth=20, width=150, stretch=tk.YES)
        self.__tree.grid(row=1, column=0, columnspan=4, pady=20, sticky="N")

        mScrollBar.grid(row=1, column=5, pady=20, sticky='WNS')

        self.returnFrame = tk.Frame(frame, bg=colors.bgColor)
        self.returnFrame.grid(row=3, column=0, sticky="E")

        toolConditionLabel = tk.Label(self.returnFrame, text=strings.bookOutConditionLabel, bg=self.__bgColor,
                                      fg=self.__fgColor)
        toolConditionLabel.grid(row=0, column=0, sticky="WE")

        toolConditionEntry = tk.Entry(self.returnFrame)
        toolConditionEntry.grid(row=0, column=1, padx=10, sticky="WW")

        returnIMG = tk.PhotoImage(file=strings.buttonEdit)
        returnToolButton = tk.Label(self.returnFrame, image=returnIMG, bg=self.__bgColor)
        returnToolButton.image = returnIMG
        returnToolButton.grid(row=1, column=1, pady=20)
        returnToolButton.bind("<Button-1>", lambda event: self.__returnTool.returnItem(toolConditionEntry))

    def __showReturn(self, show):
        if show:
            if self.__tree.focus():
                self.returnFrame.grid()
            else:
                if self.__returnTool.getCount() > 0:
                    self.__errorLabel.config(text=strings.errorSelectItem)
                else:
                    self.__errorLabel.config(text=strings.errorEmptyList)
        else:
            self.returnFrame.grid_remove()
        """
        if self.__tree.focus():
            if show:
                self.returnFrame.grid()
            else:
                self.returnFrame.grid_remove()
        else:
            if self.__returnTool.getCount() > 0:
                self.__errorLabel.config(text=strings.errorSelectItem)
            else:
                self.__errorLabel.config(text=strings.errorEmptyList)
        """

    def showReturnFrame(self, show):
        pass

