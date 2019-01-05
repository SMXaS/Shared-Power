import tkinter as tk
from tkinter import END
from tkinter import messagebox
from Resources.Values import strings, colors, dimens, fonts
import Code.Utilities.util as util
from Entities.Bookings import Bookings
import Code.Utilities.WriteFile as wf
import Code.Utilities.ReadFile as rf
import uuid


class BookToolPage(tk.Frame):
    __bgColor = colors.bgColor
    __fgColor = colors.fgColor
    __width = dimens.mainWindowWidth
    __heigh = dimens.mainWindowHeigh
    __start_date = ""
    __end_date = ""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__controller = controller
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.__initUI()

    def start(self, args):
        self.tool = args

        # resetting views
        self.__errorLabel.config(text="")
        self.__availableDate.delete(0, tk.END)
        self.__availableEndDate.delete(0, tk.END)
        self.__availableEndDate.unbind("<FocusOut>")
        self.__availableDate.unbind("<FocusOut>")
        self.__riderValue.set(0)
        self.__endDateVar.set("f")
        self.__startDateVar.set("f")
        self.__pickUpEntry.delete(0, "end")
        self.__dropOffEntry.delete(0, "end")
        self.showArrangeRider()

        self.populateStartList()

    def getStartDate(self):
        """
        Getting start booking date.
        based on selection from start date (bookings) list will generate end date list

        :return: None
        """

        index = int(self.__availableDate.curselection()[0])
        self.__start_date = self.__availableDate.get(index)
        print(self.__start_date)
        self.nextDays = util.getNextAvailableDates(self.__start_date, self.availableDateList)

        self.showReturnDateList()
        self.populateEndList()

    def getEndDate(self):
        """
        Getting end booking date. Calls "show arrange rider" function
        :return: None
        """

        index = int(self.__availableEndDate.curselection()[0])
        self.__end_date = self.__availableEndDate.get(index)
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

        self.__availableDate = tk.Listbox(frame, exportselection=0)
        self.__availableDate.bind("<<ListboxSelect>>", lambda event: self.getStartDate())
        self.__availableDate.grid(row=2, column=0, sticky="W")

        scrollAvailableDate = tk.Scrollbar(frame, orient="vertical")
        scrollAvailableDate.config(command=self.__availableDate.yview)
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

        self.__availableEndDate = tk.Listbox(frame, exportselection=0)
        self.__availableEndDate.bind("<<ListboxSelect>>", lambda event: self.getEndDate())

        self.endDateLabel.grid(row=1, column=3, padx=5, pady=2, sticky="WNE")
        self.__availableEndDate.grid(row=2, column=3, sticky="WNE")

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

        self.riderRadio = tk.Radiobutton(frame, text=strings.arrangeRider, variable=self.__riderValue, value=1,
                                         bg=self.__bgColor, fg=self.__fgColor, activebackground=self.__bgColor,
                                         activeforeground=self.__fgColor, selectcolor=self.__bgColor,
                                         command=lambda: self.showArrangeRider())
        self.riderRadio.grid(row=5, column=0, columnspan=2, sticky="WE")

        self.pickUpLabel = tk.Label(frame, text=strings.pickUpLocation, bg=self.__bgColor, fg=self.__fgColor)
        self.pickUpLabel.grid(row=6, column=0)
        self.__pickUpEntry = tk.Entry(frame, width=20)
        self.__pickUpEntry.grid(row=6, column=2, columnspan=3, padx=5)

        self.dropOffLabel = tk.Label(frame, text=strings.dropOffLocation, bg=self.__bgColor, fg=self.__fgColor)
        self.dropOffLabel.grid(row=7, column=0)
        self.__dropOffEntry = tk.Entry(frame, width=20)
        self.__dropOffEntry.grid(row=7, column=2, columnspan=3, padx=5)



        backIMG = tk.PhotoImage(file=strings.buttonBack)
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

        if len(self.nextDays)>1:
            self.startHalfDateRadio.grid()
            self.endHalfDateRadio.grid()
        else:
            self.startHalfDateRadio.grid_remove()
            self.endHalfDateRadio.grid_remove()

    def populateStartList(self):
        """
        Fills Start booking list with available dates
        :return: None
        """

        bookingList = self.getBookingList()

        self.availableDateList = self.getAvailableList(bookingList)
        for i in range(len(self.availableDateList)):
            self.__availableDate.insert(END, self.availableDateList[i])

    def getBookingList(self):
        """
        :return: list(obj(all bookings for particular item))
        """

        return rf.getAllBookings("toolID", self.tool.getID(), 0)

    def getAvailableList(self, bookingList):
        """
        :param bookingList: list(obj(bookings))
        :return: list(available dates)
        """

        return util.getBookingDates(bookingList)

    def populateEndList(self):
        """
          Fills Return booking list with available dates
          :return: None
          """

        self.__availableEndDate.delete(0, tk.END)
        for i in range(len(self.nextDays)):
            print(self.nextDays[i])
            self.__availableEndDate.insert(END, self.nextDays[i])

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
            self.__pickUpEntry.config(bg=colors.bgInactive, state="disabled")
            self.__dropOffEntry.config(bg=colors.bgInactive, state="disabled")

    def verifyHiring(self):
        """
        Verifies booking
        :return: boolean (True - approved, False - not)
        """

        booking = self.getBookingList()
        availabeList = self.getAvailableList(booking)
        dayDiff = util.getDayDifference(self.__start_date, self.__end_date)
        if util.verifyBooking(self.__start_date, availabeList, dayDiff):
            return True
        else:
            return False

    def hireTool(self):
        """
        Verify booking. If True:
            Create booking object and pass it to WriteFile
            Will return to SearchToolPage
        :return: None
        """

        if self.__start_date and self.__end_date:
            hiredTool = Bookings(uuid.uuid4(), self.tool.getID(), self.__controller.login, self.tool.getCondition(),
                                 self.__start_date, self.__startDateVar.get(), self.__end_date, self.__endDateVar.get(),
                                 strings.toolStatus[0])

            hiredTool.setPickUpLocation(self.__pickUpEntry.get())
            hiredTool.setDropOffLocation(self.__dropOffEntry.get())

            if self.verifyHiring():
                # show confirmation window

                totalPrice = util.calculateToolhireCost(hiredTool, self.tool)
                message = "{} {}\n{} {}\n{} {}\n{} {}{}\n\n{}".format(strings.toolTitleForInvoice, self.tool.getTitle(),
                                                                      strings.hireDate, hiredTool.getStartDate(),
                                                                      strings.returnDate, hiredTool.getExpectedReturnDate(),
                                                                      strings.totalCost, str(totalPrice), strings.currency,
                                                                      strings.confirmBooking)
                if messagebox.askokcancel("Information", message):
                    #          obj,     simplePath,     fieldNames,           complex path              path parameter
                    wf.write(hiredTool, None, strings.fieldNames_booking, strings.filePath_booking, hiredTool.getToolID())
                    self.__availableEndDate.unbind("<FocusOut>")
                    self.__availableDate.unbind("<FocusOut>")
                    self.__controller.show_frame(strings.searchToolClass)
            else:
                self.__errorLabel.config(text=strings.errorAlreadyBooked)
        else:
            print("Error")

