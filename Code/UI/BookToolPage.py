import tkinter as tk
from tkinter import messagebox
from Resources.Values import strings, colors
from Code.BookTool import BookTool


class BookToolPage(tk.Frame):
    __bgColor = colors.bgColor
    __fgColor = colors.fgColor

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__controller = controller
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.__initUI()
        self.showArrangeRider()

    def start(self, args):
        self.tool = args

        # resetting views
        self.__errorLabel.config(text="")
        self.__availableDateBox.delete(0, tk.END)
        self.__availableEndDateBox.delete(0, tk.END)
        self.__availableEndDateBox.unbind("<FocusOut>")
        self.__availableDateBox.unbind("<FocusOut>")
        self.__riderValue.set(0)
        self.__endDateVar.set("f")
        self.__startDateVar.set("f")
        self.__pickUpEntry.delete(0, "end")
        self.__dropOffEntry.delete(0, "end")

        self.bookTool = BookTool(self.__availableDateBox, self.__availableEndDateBox, self.tool)
        self.bookTool.populateStartList()

    def getEndDate(self):
        """
        Getting end booking date. Calls "show arrange rider" function
        :return: None
        """

        self.bookTool.getEndDate()
        self.showArrangeRider()

    def __initUI(self):

        frame = tk.Frame(self, bg=self.__bgColor)
        frame.grid(row=0, column=0, pady=60)
        frame.columnconfigure(2, minsize=20)
        frame.rowconfigure(3, minsize=30)

        ###########################################################################
        # Selection widgets
        ###########################################################################

        self.__errorLabel = tk.Label(frame, bg=colors.bgColor, fg=colors.errorColor)
        self.__errorLabel.grid(row=0, column=0, columnspan=4, sticky="WN")

        DateLabel = tk.Label(frame, text=strings.hireDate, bg=self.__bgColor, fg=self.__fgColor)
        DateLabel.grid(row=1, column=0, padx=5, pady=2, sticky="W")

        self.endDateLabel = tk.Label(frame, text=strings.returnDate, bg=self.__bgColor, fg=self.__fgColor)

        self.__availableDateBox = tk.Listbox(frame, exportselection=0)
        self.__availableDateBox.bind("<<ListboxSelect>>", lambda event: self.showReturnDateList())
        self.__availableDateBox.grid(row=2, column=0, sticky="W")

        scrollAvailableDate = tk.Scrollbar(frame, orient="vertical")
        scrollAvailableDate.config(command=self.__availableDateBox.yview)
        scrollAvailableDate.grid(row=2, column=1, sticky="WNS")

        self.__startDateVar = tk.StringVar()

        startFullDateRadio = tk.Radiobutton(frame, text=strings.fullDay, variable=self.__startDateVar,
                                            indicatoron=False, value="f", width=8, borderwidth=0,
                                            bg=colors.bgInactive)
        endFullDateRadio = tk.Radiobutton(frame, text=strings.halfDay, variable=self.__startDateVar,
                                          indicatoron=False, value="h", width=8, borderwidth=0,
                                          bg=colors.bgInactive)

        self.__startDateVar.set("f")

        startFullDateRadio.grid(row=3, column=0, sticky="W")
        endFullDateRadio.grid(row=3, column=0, sticky="E")

        self.__availableEndDateBox = tk.Listbox(frame, exportselection=0)
        self.__availableEndDateBox.bind("<<ListboxSelect>>", lambda event: self.getEndDate())

        self.endDateLabel.grid(row=1, column=3, padx=5, pady=2, sticky="WNE")
        self.__availableEndDateBox.grid(row=2, column=3, sticky="WNE")

        self.__endDateVar = tk.StringVar()
        self.__endDateVar.set("f")

        self.startHalfDateRadio = tk.Radiobutton(frame, text=strings.fullDay, variable=self.__endDateVar,
                                                 indicatoron=False, value="f", width=8, borderwidth=0,
                                                 bg=colors.bgInactive)
        self.endHalfDateRadio = tk.Radiobutton(frame, text=strings.halfDay, variable=self.__endDateVar,
                                               indicatoron=False, value="h", width=8, borderwidth=0,
                                               bg=colors.bgInactive)

        self.startHalfDateRadio.grid(row=3, column=3, sticky="W")
        self.endHalfDateRadio.grid(row=3, column=3, sticky="E")

        self.__riderValue = tk.IntVar()
        self.__riderValue.set(0)

        self.riderCheckButton = tk.Checkbutton(frame, text=strings.arrangeRider, variable=self.__riderValue,
                                               bg=self.__bgColor, fg=self.__fgColor, activebackground=self.__bgColor,
                                               activeforeground=self.__fgColor, selectcolor=self.__bgColor,
                                               command=lambda: self.showArrangeRider())
        self.riderCheckButton.grid(row=5, column=0, columnspan=2, sticky="WE")

        """

        self.riderRadio = tk.Radiobutton(frame, text=strings.arrangeRider, variable=self.__riderValue, value=1,
                                         bg=self.__bgColor, fg=self.__fgColor, activebackground=self.__bgColor,
                                         activeforeground=self.__fgColor, selectcolor=self.__bgColor,
                                         command=lambda: self.showArrangeRider())
        self.riderRadio.grid(row=5, column=0, columnspan=2, sticky="WE")

        """

        self.pickUpLabel = tk.Label(frame, text=strings.pickUpLocation, bg=self.__bgColor, fg=self.__fgColor)
        self.pickUpLabel.grid(row=6, column=0)
        self.__pickUpEntry = tk.Entry(frame, width=20)
        self.__pickUpEntry.grid(row=6, column=2, columnspan=3, padx=5)

        self.dropOffLabel = tk.Label(frame, text=strings.dropOffLocation, bg=self.__bgColor, fg=self.__fgColor)
        self.dropOffLabel.grid(row=7, column=0)
        self.__dropOffEntry = tk.Entry(frame, width=20)
        self.__dropOffEntry.grid(row=7, column=2, columnspan=3, padx=5)

        backIMG = tk.PhotoImage(file=strings.btn_back)
        backButton = tk.Label(frame, image=backIMG, bg=self.__bgColor)
        backButton.image = backIMG
        backButton.bind("<Button-1>", lambda event: self.__controller.show_frame(strings.searchToolClass, "args"))
        backButton.grid(row=9, column=0, padx=10, sticky="W")

        hireIMG = tk.PhotoImage(file=strings.buttonHire)
        hireButton = tk.Label(frame, image=hireIMG, bg=self.__bgColor)
        hireButton.image = hireIMG
        hireButton.bind("<Button-1>", lambda event: self.hireTool())
        hireButton.grid(row=9, column=1, columnspan=4, pady=40, sticky="WE")

    def showReturnDateList(self):
        """
        Makes Return Date list visible
        :return:
        """
        self.bookTool.getStartDate()

        if len(self.bookTool.getNextDays()) > 1:
            self.startHalfDateRadio.grid()
            self.endHalfDateRadio.grid()
        else:
            self.startHalfDateRadio.grid_remove()
            self.endHalfDateRadio.grid_remove()

    def showArrangeRider(self):
        """
        Makes rider option visible
        :return: None
        """
        if self.__riderValue.get() == 1:
            self.pickUpLabel.config(fg=self.__fgColor)
            self.dropOffLabel.config(fg=self.__fgColor)
            self.__pickUpEntry.config(bg=self.__fgColor, state="normal")
            self.__dropOffEntry.config(bg=self.__fgColor, state="normal")

        else:
            self.pickUpLabel.config(fg=colors.bgInactive)
            self.dropOffLabel.config(fg=colors.bgInactive)
            self.__pickUpEntry.delete(0, "end")
            self.__dropOffEntry.delete(0, "end")
            self.__pickUpEntry.config(bg=colors.bgInactive, state="disabled")
            self.__dropOffEntry.config(bg=colors.bgInactive, state="disabled")

    def hireTool(self):
        """
        Verify booking. If True:
            Create booking object and pass it to WriteFile
            Will return to SearchToolPage
        :return: None
        """
        myReturn = self.bookTool.hireTool(self.__controller.login, self.__startDateVar.get(), self.__endDateVar.get(),
                                          self.__pickUpEntry.get(), self.__dropOffEntry.get())

        if myReturn:
            if messagebox.askokcancel("Information", self.bookTool.getMessage()):
                self.bookTool.wfwrite()
                self.__availableEndDateBox.unbind("<FocusOut>")
                self.__availableDateBox.unbind("<FocusOut>")
                self.__controller.show_frame(strings.searchToolClass)
        else:
            self.__errorLabel.config(text=strings.errorAlreadyBooked)




