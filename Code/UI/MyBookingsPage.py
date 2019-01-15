import tkinter as tk
from tkinter import ttk, messagebox
from Resources.Values import strings, colors
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
        self.__myBookings = MyBookings(self.__errorLabel, self.__tree, self.__controller.login)
        self.__controller.addToolButton.config(text=strings.menuAddTool)
        self.__myBookings.populateData()
        self.__isEmpty()

    def __isEmpty(self):
        if self.__myBookings.getCount() > 0:
            self.__errorLabel.config(text="")
            self.__showReturn(False)
        else:
            self.__controller.show_frame(strings.emptyLayout)
            self.__controller.highlightButton(1)

    def __initUI(self):

        frame = tk.Frame(self, bg=self.__bgColor)
        frame.grid(row=0, column=0, sticky="", pady=40)

        frame.rowconfigure(2, minsize=10)
        frame.rowconfigure(3, weight=1)
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

        # --------------------------------------------------------------

        menuFrame = tk.Frame(frame, bg=self.__bgColor)
        menuFrame.grid(row=3, column=0, columnspan=5, pady=10, sticky="WE")

        returnIMG = tk.PhotoImage(file=strings.btn_return)
        returnButton = tk.Label(menuFrame, image=returnIMG, bg=self.__bgColor)
        returnButton.image = returnIMG
        returnButton.grid(row=0, column=0, padx=5, sticky="WE")
        returnButton.bind("<Button-1>", lambda event: self.__showReturn(True))

        cancelIMG = tk.PhotoImage(file=strings.btn_cancel)
        cancelButton = tk.Label(menuFrame, image=cancelIMG, bg=self.__bgColor)
        cancelButton.image = cancelIMG
        cancelButton.grid(row=0, column=1, padx=5, sticky="WE")
        cancelButton.bind("<Button-1>", lambda event: self.__cancelItem())

        # --------------------------------------------------------------

        self.returnFrame = tk.Frame(frame, bg=colors.bgColor)
        self.returnFrame.grid(row=4, column=0, sticky="E")

        toolConditionLabel = tk.Label(self.returnFrame, text=strings.bookOutConditionLabel, bg=self.__bgColor,
                                      fg=self.__fgColor)
        toolConditionLabel.grid(row=0, column=0, sticky="WE")

        toolConditionEntry = tk.Entry(self.returnFrame)
        toolConditionEntry.grid(row=0, column=1, padx=10, sticky="WW")

        confirmIMG = tk.PhotoImage(file=strings.btn_confirm)
        confirmButton = tk.Label(self.returnFrame, image=confirmIMG, bg=self.__bgColor)
        confirmButton.image = confirmIMG
        confirmButton.grid(row=1, column=1, pady=20)
        confirmButton.bind("<Button-1>", lambda event: self.__returnItem(toolConditionEntry))

    def __cancelItem(self):
        if messagebox.askokcancel(strings.confirmDialogTitle, strings.cancelItemConfirm):
            self.__myBookings.cancelBooking()
            self.__isEmpty()

    def __returnItem(self, condition):
        if condition.get():
            isReturn = self.__myBookings.returnItem(condition)
            self.__showReturn(False)
            self.__isEmpty()
            if isReturn:
                messagebox.showinfo(strings.infoDialogTitle, strings.returnDialogMessage)
            else:
                messagebox.showinfo(strings.infoDialogTitle, strings.cancelDialogMessage)

            condition.delete(0, "end")
        else:
            self.__errorLabel.config(text=strings.errorToolConditionMissing)

    def __showReturn(self, show):
        if show:
            self.__errorLabel.config(text="")
            if self.__tree.focus():
                self.returnFrame.grid()
            else:
                if self.__myBookings.getCount() > 0:
                    self.__errorLabel.config(text=strings.errorSelectItem)
                else:
                    self.__errorLabel.config(text=strings.errorEmptyList)
        else:
            self.returnFrame.grid_remove()
