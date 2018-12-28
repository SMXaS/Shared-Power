import tkinter as tk
from tkinter import END
from Code.UI import SearchToolPage as sp
import Resources.Values.values as values
import Code.Utilities.util as util
from Entities.Bookings import Bookings
import Code.Utilities.WriteFile as wf
import Code.Utilities.ReadFile as rf


class BookToolPage(tk.Frame):
    bgColor = values.bgColor
    fgColor = values.fgColor
    width = values.mainWindowWidth
    heigh = values.mainWindowHeigh
    start_date = ""
    end_date = ""

    def __init__(self, master, tool):
        """
        :param master: master
        :param tool[0]: login
        :param tool[1]: obj(tool)
        """
        tk.Frame.__init__(self, master)
        master.geometry("{}x{}+%d+%d".format(self.width, self.heigh) % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title(values.bookToolTitle)

        self.login = tool[0]
        self.tool = tool[1]
        self.master = master
        self.owner = master.owner

        self.initUI()
        self.populateStartList()

    def getStartDate(self):
        """
        Getting start booking date.
        based on selection from start date (bookings) list will generate end date list

        :return: None
        """

        index = int(self.availableDate.curselection()[0])
        self.start_date = self.availableDate.get(index)
        print(self.start_date)
        self.nextDays = util.getNextAvailableDates(self.start_date, self.availableDateList)

        self.showReturnDateList()
        self.populateEndList()

    def getEndDate(self):
        """
        Getting end booking date. Calls "show arrange rider" function
        :return: None
        """

        index = int(self.availableEndDate.curselection()[0])
        self.end_date = self.availableEndDate.get(index)
        self.showArrangeRider()

    def initUI(self):

        #############################################################################
        # Info widgets
        #############################################################################
        ownerLabel = tk.Label(self, text=values.owner, bg=self.bgColor, fg=self.fgColor)
        ownerLabel.grid(row=1, column=0, padx=5, pady=2, sticky="E")

        ownerTxt = tk.Label(self, text=self.tool.getOwner(), bg=self.bgColor, fg=self.fgColor)
        ownerTxt.grid(row=1, column=1, columnspan=3, padx=5, sticky="W")

        titleLabel = tk.Label(self, text=values.toolTitle, bg=self.bgColor, fg=self.fgColor)
        titleLabel.grid(row=2, column=0, padx=5, pady=2, sticky="E")

        titleTxt = tk.Label(self, text=self.tool.getTitle(), bg=self.bgColor, fg=self.fgColor)
        titleTxt.grid(row=2, column=1, columnspan=3, padx=5, sticky="W")

        descriptionLabel = tk.Label(self, text=values.toolDescription, bg=self.bgColor, fg=self.fgColor)
        descriptionLabel.grid(row=3, column=0, padx=5, pady=2, sticky="E")

        descriptionTxt = tk.Label(self, text=self.tool.getDescription(), bg=self.bgColor, fg=self.fgColor)
        descriptionTxt.grid(row=3, column=1, columnspan=3, padx=5, sticky="W")

        conditionLabel = tk.Label(self, text=values.toolCondition, bg=self.bgColor, fg=self.fgColor)
        conditionLabel.grid(row=4, column=0, padx=5, pady=2, sticky="E")

        conditionTxt = tk.Label(self, text=self.tool.getCondition(), bg=self.bgColor, fg=self.fgColor)
        conditionTxt.grid(row=4, column=1, columnspan=3, padx=5, sticky="W")

        priceFullDayLabel = tk.Label(self, text=values.priceDay, bg=self.bgColor, fg=self.fgColor)
        priceFullDayLabel.grid(row=5, column=0, padx=5, pady=2, sticky="E")

        priceFullDayTxt = tk.Label(self, text="{}{}".format(self.tool.getPriceFullDay(), values.currency),
                                   bg=self.bgColor, fg=self.fgColor)
        priceFullDayTxt.grid(row=5, column=1, columnspan=3, padx=5, pady=2, sticky="W")

        priceHalfDayLabel = tk.Label(self, text=values.priceHalfDay, bg=self.bgColor, fg=self.fgColor)
        priceHalfDayLabel.grid(row=6, column=0, padx=5, pady=2, sticky="E")

        priceHalfDayTxt = tk.Label(self, text="{}{}".format(self.tool.getPriceHalfDay(), values.currency),
                                   bg=self.bgColor, fg=self.fgColor)
        priceHalfDayTxt.grid(row=6, column=1, columnspan=3, padx=5, pady=2, sticky="W")

        ###########################################################################

        ###########################################################################
        # Selection widgets
        ###########################################################################

        DateLabel = tk.Label(self, text=values.hireDate, bg=self.bgColor, fg=self.fgColor)
        DateLabel.grid(row=7, column=0, padx=5, pady=2, sticky="WNE")

        self.endDateLabel = tk.Label(self, text=values.returnDate, bg=self.bgColor, fg=self.fgColor)

        self.availableDate = tk.Listbox(self, exportselection=0)
        self.availableDate.bind("<<ListboxSelect>>", lambda event: self.getStartDate())
        self.availableDate.grid(row=8, column=0, rowspan=8, sticky="WNE")

        scrollAvailableDate = tk.Scrollbar(self, orient="vertical")
        scrollAvailableDate.config(command=self.availableDate.yview)
        scrollAvailableDate.grid(row=8, column=1, rowspan=8, sticky="WNS")

        self.startDateVar = tk.StringVar()
        startFullDateRadio = tk.Radiobutton(self, text=values.fullDay, variable=self.startDateVar,
                                            indicatoron=False, value="f", width=8, borderwidth=0,
                                            bg=values.bgInactive)
        endFullDateRadio = tk.Radiobutton(self, text=values.halfDay, variable=self.startDateVar,
                                          indicatoron=False, value="h", width=8, borderwidth=0,
                                          bg=values.bgInactive)

        self.startDateVar.set("f")

        startFullDateRadio.grid(row=16, column=0, sticky="W")
        endFullDateRadio.grid(row=16, column=0, sticky="E")

        self.availableEndDate = tk.Listbox(self, exportselection=0)
        self.availableEndDate.bind("<<ListboxSelect>>", lambda event: self.getEndDate())

        self.endDateLabel.grid(row=7, column=2, padx=5, pady=2, sticky="WNE")
        self.availableEndDate.grid(row=8, column=2, rowspan=8, sticky="WNE")

        self.scrollNextAvailableDate = tk.Scrollbar(self, orient="vertical")
        self.scrollNextAvailableDate.config(command=self.availableEndDate.yview)
        self.scrollNextAvailableDate.grid(row=8, column=3, rowspan=8, sticky="WNS")

        self.scrollNextAvailableDate.grid_remove()
        self.endDateLabel.grid_remove()
        self.availableEndDate.grid_remove()
        self.endDateVar = tk.StringVar()
        self.endDateVar.set("f")
        self.startHalfDateRadio = tk.Radiobutton(self, text=values.fullDay, variable=self.endDateVar,
                                                 indicatoron=False, value="f", width=8, borderwidth=0,
                                                 bg=values.bgInactive)
        self.endHalfDateRadio = tk.Radiobutton(self, text=values.halfDay, variable=self.endDateVar,
                                               indicatoron=False, value="h", width=8, borderwidth=0,
                                               bg=values.bgInactive)

        self.startHalfDateRadio.grid(row=16, column=2, sticky="W")
        self.endHalfDateRadio.grid(row=16, column=2, sticky="E")

        self.startHalfDateRadio.grid_remove()
        self.endHalfDateRadio.grid_remove()

        hireIMG = tk.PhotoImage(file=values.buttonHire)
        hireButton = tk.Label(self, image=hireIMG, bg=self.bgColor)
        hireButton.image = hireIMG
        hireButton.bind("<Button-1>", lambda event: self.hireTool())
        hireButton.grid(row=17, column=0, columnspan=2, pady=40, sticky="WE")

        self.riderValue = tk.IntVar()
        self.riderValue.set(0)

        self.riderRadio = tk.Radiobutton(self, text=values.arrangeRider, variable=self.riderValue, value=1,
                                         bg=self.bgColor, fg=self.fgColor,activebackground=self.bgColor,
                                         activeforeground=self.fgColor, selectcolor=self.bgColor,
                                         command=lambda: self.showArrangeRider())
        self.riderRadio.grid(row=7, column=4)
        self.riderRadio.grid_remove()

        self.pickUpLabel = tk.Label(self, text=values.pickUpLocation, bg=self.bgColor, fg=self.fgColor)
        self.pickUpLabel.grid(row=8, column=4)
        self.pickUpEntry = tk.Entry(self, width=20)
        self.pickUpEntry.grid(row=8, column=5, padx=5)

        self.dropOffLabel = tk.Label(self, text=values.dropOffLocation, bg=self.bgColor, fg=self.fgColor)
        self.dropOffLabel.grid(row=9, column=4)
        self.dropOffEntry = tk.Entry(self, width=20)
        self.dropOffEntry.grid(row=9, column=5, padx=5)

        self.pickUpLabel.grid_remove()
        self.pickUpEntry.grid_remove()
        self.dropOffLabel.grid_remove()
        self.dropOffEntry.grid_remove()

        # TODO
        # Keys: HireBy,startDate,endDate,confirmedEndDate anything else? Owner(or find by tool ID)

        backButton = tk.Button(self, text=values.back, command=lambda: self.master.change_frame(sp.SearchToolPage, self.login))
        backButton.grid(row=0, column=0)

    def showReturnDateList(self):
        """
        Makes Return Date list visible
        :return:
        """

        self.availableEndDate.grid()
        self.endDateLabel.grid()
        self.scrollNextAvailableDate.grid()

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
        return rf.getAllBookings("toolID", self.tool.getID())

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

        self.riderRadio.grid()
        self.pickUpLabel.grid()
        self.dropOffLabel.grid()
        self.pickUpEntry.grid()
        self.dropOffEntry.grid()

        if self.riderValue.get()==1:
            self.pickUpLabel.config(fg=self.fgColor)
            self.dropOffLabel.config(fg=self.fgColor)
            self.pickUpEntry.config(bg=self.fgColor, state="normal")
            self.dropOffEntry.config(bg=self.fgColor, state="normal")

        else:
            self.pickUpLabel.config(fg=values.bgInactive)
            self.dropOffLabel.config(fg=values.bgInactive)
            self.pickUpEntry.config(bg=values.bgInactive, state="disabled")
            self.dropOffEntry.config(bg=values.bgInactive, state="disabled")

    def verifyHiring(self):
        """
        Verifies booking
        :return: boolean (True - approved, False - not)
        """

        booking = self.getBookingList()
        availabeList = self.getAvailableList(booking)
        dayDiff = util.getDayDifference(self.start_date, self.end_date)
        if util.verifyBooking(self.start_date, availabeList, dayDiff):
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

        if self.start_date and self.end_date:
            print("sT: {}; eT: {}".format(self.startDateVar.get(), self.endDateVar.get()))
            hiredTool = Bookings(self.tool.getID(), self.login, self.tool.getCondition(), self.start_date,
                                 self.startDateVar.get(), self.end_date, self.endDateVar.get())

            hiredTool.setPickUpLocation(self.pickUpEntry.get())
            hiredTool.setDropOffLocation(self.dropOffEntry.get())

            if self.verifyHiring():
                #         obj,     simplePath,     fieldNames,           complex path
                wf.write(hiredTool, None, values.fieldNames_booking, values.filePath_booking)
                self.master.change_frame(sp.SearchToolPage, self.login)
            else:
                print("too late.. item is booked")
        else:
            print("Error")
