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

    # TODO live cost view
    # TODO error label

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__controller = controller
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.__initUI()

    def start(self, args):
        self.tool = args

        # resetting views
        self.availableDate.delete(0, tk.END)
        self.availableEndDate.delete(0, tk.END)
        self.availableEndDate.unbind("<FocusOut>")
        self.availableDate.unbind("<FocusOut>")
        self.riderValue.set(0)
        self.endDateVar.set("f")
        self.startDateVar.set("f")
        self.pickUpEntry.delete(0, "end")
        self.dropOffEntry.delete(0, "end")
        self.showArrangeRider()

        self.populateStartList()

    def getStartDate(self):
        """
        Getting start booking date.
        based on selection from start date (bookings) list will generate end date list

        :return: None
        """

        index = int(self.availableDate.curselection()[0])
        self.__start_date = self.availableDate.get(index)
        print(self.__start_date)
        self.nextDays = util.getNextAvailableDates(self.__start_date, self.availableDateList)

        self.showReturnDateList()
        self.populateEndList()

    def getEndDate(self):
        """
        Getting end booking date. Calls "show arrange rider" function
        :return: None
        """

        index = int(self.availableEndDate.curselection()[0])
        self.__end_date = self.availableEndDate.get(index)
        self.showArrangeRider()

    def __initUI(self):

        frame = tk.Frame(self, bg=self.__bgColor)
        frame.grid(row=0, column=0, pady=60)
        frame.columnconfigure(2, minsize=20)
        frame.rowconfigure(3, minsize=30)

        ###########################################################################
        # Selection widgets
        ###########################################################################

        DateLabel = tk.Label(frame, text=strings.hireDate, bg=self.__bgColor, fg=self.__fgColor)
        DateLabel.grid(row=0, column=0, padx=5, pady=2, sticky="W")

        self.endDateLabel = tk.Label(frame, text=strings.returnDate, bg=self.__bgColor, fg=self.__fgColor)

        self.availableDate = tk.Listbox(frame, exportselection=0)
        self.availableDate.bind("<<ListboxSelect>>", lambda event: self.getStartDate())
        self.availableDate.grid(row=1, column=0, sticky="W")

        scrollAvailableDate = tk.Scrollbar(frame, orient="vertical")
        scrollAvailableDate.config(command=self.availableDate.yview)
        scrollAvailableDate.grid(row=1, column=1, sticky="WNS")

        self.startDateVar = tk.StringVar()

        startFullDateRadio = tk.Radiobutton(frame, text=strings.fullDay, variable=self.startDateVar,
                                            indicatoron=False, value="f", width=8, borderwidth=0,
                                            bg=colors.bgInactive)
        endFullDateRadio = tk.Radiobutton(frame, text=strings.halfDay, variable=self.startDateVar,
                                          indicatoron=False, value="h", width=8, borderwidth=0,
                                          bg=colors.bgInactive)

        self.startDateVar.set("f")

        startFullDateRadio.grid(row=2, column=0, sticky="W")
        endFullDateRadio.grid(row=2, column=0, sticky="E")

        self.availableEndDate = tk.Listbox(frame, exportselection=0)
        self.availableEndDate.bind("<<ListboxSelect>>", lambda event: self.getEndDate())

        self.endDateLabel.grid(row=0, column=3, padx=5, pady=2, sticky="WNE")
        self.availableEndDate.grid(row=1, column=3, sticky="WNE")

        self.scrollNextAvailableDate = tk.Scrollbar(frame, orient="vertical")
        self.scrollNextAvailableDate.config(command=self.availableEndDate.yview)
        self.scrollNextAvailableDate.grid(row=1, column=4, sticky="WNS")

        self.endDateVar = tk.StringVar()
        self.endDateVar.set("f")

        self.startHalfDateRadio = tk.Radiobutton(frame, text=strings.fullDay, variable=self.endDateVar,
                                                 indicatoron=False, value="f", width=8, borderwidth=0,
                                                 bg=colors.bgInactive)
        self.endHalfDateRadio = tk.Radiobutton(frame, text=strings.halfDay, variable=self.endDateVar,
                                               indicatoron=False, value="h", width=8, borderwidth=0,
                                               bg=colors.bgInactive)

        self.startHalfDateRadio.grid(row=2, column=3, sticky="W")
        self.endHalfDateRadio.grid(row=2, column=3, sticky="E")

        self.riderValue = tk.IntVar()
        self.riderValue.set(0)

        self.riderRadio = tk.Radiobutton(frame, text=strings.arrangeRider, variable=self.riderValue, value=1,
                                         bg=self.__bgColor, fg=self.__fgColor, activebackground=self.__bgColor,
                                         activeforeground=self.__fgColor, selectcolor=self.__bgColor,
                                         command=lambda: self.showArrangeRider())
        self.riderRadio.grid(row=4, column=0, columnspan=2, sticky="WE")

        self.pickUpLabel = tk.Label(frame, text=strings.pickUpLocation, bg=self.__bgColor, fg=self.__fgColor)
        self.pickUpLabel.grid(row=5, column=0)
        self.pickUpEntry = tk.Entry(frame, width=20)
        self.pickUpEntry.grid(row=5, column=2, columnspan=3, padx=5)

        self.dropOffLabel = tk.Label(frame, text=strings.dropOffLocation, bg=self.__bgColor, fg=self.__fgColor)
        self.dropOffLabel.grid(row=6, column=0)
        self.dropOffEntry = tk.Entry(frame, width=20)
        self.dropOffEntry.grid(row=6, column=2, columnspan=3, padx=5)



        backIMG = tk.PhotoImage(file=strings.buttonBack)
        backButton = tk.Label(frame, image=backIMG, bg=self.__bgColor)
        backButton.image = backIMG
        backButton.bind("<Button-1>", lambda event: self.__controller.show_frame(strings.searchToolClass))
        backButton.grid(row=8, column=0, padx=10, sticky="W")

        hireIMG = tk.PhotoImage(file=strings.buttonHire)
        hireButton = tk.Label(frame, image=hireIMG, bg=self.__bgColor)
        hireButton.image = hireIMG
        hireButton.bind("<Button-1>", lambda event: self.hireTool())
        hireButton.grid(row=8, column=1, columnspan=4, pady=40, sticky="WE")

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
            self.availableDate.insert(END, self.availableDateList[i])

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

        self.availableEndDate.delete(0, tk.END)
        for i in range(len(self.nextDays)):
            print(self.nextDays[i])
            self.availableEndDate.insert(END, self.nextDays[i])

    def showArrangeRider(self):
        """
        Makes rider option visible
        :return: None
        """
        if self.riderValue.get() == 1:
            self.pickUpLabel.config(fg=self.__fgColor)
            self.dropOffLabel.config(fg=self.__fgColor)
            self.pickUpEntry.config(bg=self.__fgColor, state="normal")
            self.dropOffEntry.config(bg=self.__fgColor, state="normal")

        else:
            self.pickUpLabel.config(fg=colors.bgInactive)
            self.dropOffLabel.config(fg=colors.bgInactive)
            self.pickUpEntry.config(bg=colors.bgInactive, state="disabled")
            self.dropOffEntry.config(bg=colors.bgInactive, state="disabled")

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
            print("sT: {}; eT: {}".format(self.startDateVar.get(), self.endDateVar.get()))
            hiredTool = Bookings(uuid.uuid4(), self.tool.getID(), self.__controller.login, self.tool.getCondition(),
                                 self.__start_date, self.startDateVar.get(), self.__end_date, self.endDateVar.get(),
                                 strings.toolStatus[0])

            hiredTool.setPickUpLocation(self.pickUpEntry.get())
            hiredTool.setDropOffLocation(self.dropOffEntry.get())

            if self.verifyHiring():
                # show confirmation window

                message = "{} {}\n{} {}\n{} {}\n{} {}{}\n\n{}".format(strings.toolTitleForInvoice, self.tool.getTitle(),
                                                                      strings.hireDate, hiredTool.getStartDate(),
                                                                      strings.returnDate, hiredTool.getExpectedReturnDate(),
                                                                      strings.totalCost, 50, strings.currency,
                                                                      strings.confirmBooking)
                if messagebox.askokcancel("Information", message):
                    #          obj,     simplePath,     fieldNames,           complex path              path parameter
                    wf.write(hiredTool, None, strings.fieldNames_booking, strings.filePath_booking, hiredTool.getToolID())
                    self.availableEndDate.unbind("<FocusOut>")
                    self.availableDate.unbind("<FocusOut>")
                    self.__controller.show_frame(strings.searchToolClass)
            else:
                print("too late.. item is booked")
        else:
            print("Error")
