import tkinter as tk
from tkinter import END
from Code.UI import SearchToolPage as sp
import Resources.Values.values as values
import Code.Utilities.util as util
from Entities.Bookings import Bookings


# Do not use PIL. This is external library


class BookToolPage(tk.Frame):
    bgColor = values.bgColor
    fgColor = values.fgColor

    def __init__(self, master, tool):
        self.login = tool[0]
        tk.Frame.__init__(self, master)

        self.tool = tool[1]
        self.master=master
        self.owner = master.owner
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title('Hire Tool')

        self.initUI()
        self.setPlaceholder()
        self.populateStartList()

    def getEndDays(self):
        index = int(self.availableDate.curselection()[0])
        self.start_date = self.availableDate.get(index)
        print(self.start_date)
        self.nextDays = util.getNextAvailableDates(self.start_date, self.availableDateList)

        self.showSecondList()
        self.populateEndList()


    def getNextDaysTest(self):
        index = int(self.availableEndDate.curselection()[0])
        self.end_date = self.availableEndDate.get(index)


    def initUI(self):

        self.master.columnconfigure(0, weight=1)

        #############################################################################
        # Info widgets
        #############################################################################
        ownerLabel = tk.Label(self, text="Owner: ", bg=self.bgColor, fg=self.fgColor)
        ownerLabel.grid(row=1, column=0, padx=5, pady=2, sticky="E")

        ownerTxt = tk.Label(self, text=self.tool.getOwner(), bg=self.bgColor, fg=self.fgColor)
        ownerTxt.grid(row=1, column=1, columnspan=3, padx=5, sticky="W")

        titleLabel = tk.Label(self, text="title: ", bg=self.bgColor, fg=self.fgColor)
        titleLabel.grid(row=2, column=0, padx=5, pady=2, sticky="E")

        titleTxt = tk.Label(self, text=self.tool.getTitle(), bg=self.bgColor, fg=self.fgColor)
        titleTxt.grid(row=2, column=1, columnspan=3, padx=5, sticky="W")

        descriptionLabel = tk.Label(self, text="description: ", bg=self.bgColor, fg=self.fgColor)
        descriptionLabel.grid(row=3, column=0, padx=5, pady=2, sticky="E")

        descriptionTxt = tk.Label(self, text=self.tool.getDescription(), bg=self.bgColor, fg=self.fgColor)
        descriptionTxt.grid(row=3, column=1, columnspan=3, padx=5, sticky="W")

        priceFullDayLabel = tk.Label(self, text="priceFullDay: ", bg=self.bgColor, fg=self.fgColor)
        priceFullDayLabel.grid(row=4, column=0, padx=5, pady=2, sticky="E")

        priceFullDayTxt = tk.Label(self, text=self.tool.getPriceFullDay() + " $", bg=self.bgColor,
                                   fg=self.fgColor)
        priceFullDayTxt.grid(row=4, column=1, columnspan=3, padx=5, pady=2, sticky="W")

        priceHalfDayLabel = tk.Label(self, text="priceHalfDay: ", bg=self.bgColor, fg=self.fgColor)
        priceHalfDayLabel.grid(row=5, column=0, padx=5, pady=2, sticky="E")

        priceHalfDayTxt = tk.Label(self, text=self.tool.getPriceHalfDay()+" $", bg=self.bgColor,
                                   fg=self.fgColor)
        priceHalfDayTxt.grid(row=5, column=1, columnspan=3, padx=5, pady=2, sticky="W")
        ###########################################################################

        ###########################################################################
        # Selection widgets
        ###########################################################################

        DateLabel = tk.Label(self, text="Hire date", bg=self.bgColor, fg=self.fgColor)
        DateLabel.grid(row=6, column=0, padx=5, pady=2, sticky="WNE")

        self.endDateLabel = tk.Label(self, text="End date", bg=self.bgColor, fg=self.fgColor)

        self.availableDate = tk.Listbox(self, exportselection=0)
        self.availableDate.bind("<<ListboxSelect>>", lambda event: self.getEndDays())
        self.availableDate.grid(row=7, column=0, rowspan=3, padx=5, sticky="WNE")

        self.startDateVar = tk.IntVar()
        startFullDateRadio = tk.Radiobutton(self, text="Full day", variable=self.startDateVar,
                                            indicatoron=False, value=1, width=8, borderwidth=0,
                                            bg="grey")
        endFullDateRadio = tk.Radiobutton(self, text="Half day", variable=self.startDateVar,
                                          indicatoron=False, value=0, width=8, borderwidth=0,
                                          bg="grey")

        self.startDateVar.set(1)

        startFullDateRadio.grid(row=10, column=0, padx=5, sticky="W")
        endFullDateRadio.grid(row=10, column=0, padx=5, sticky="E")

        self.availableEndDate = tk.Listbox(self, exportselection=0)
        self.availableEndDate.bind("<<ListboxSelect>>", lambda event: self.getNextDaysTest())

        self.endDateLabel.grid(row=6, column=1, padx=5, pady=2, sticky="WNE")
        self.availableEndDate.grid(row=7, column=1, rowspan=3, padx=5, sticky="WNE")

        self.endDateLabel.grid_remove()
        self.availableEndDate.grid_remove()
        self.halfDateVar = tk.IntVar()
        self.halfDateVar.set(1)
        self.startHalfDateRadio = tk.Radiobutton(self, text="Full day", variable=self.halfDateVar,
                                                 indicatoron=False, value=1, width=8, borderwidth=0,
                                                 bg="grey")
        self.endHalfDateRadio = tk.Radiobutton(self, text="Half day", variable=self.halfDateVar,
                                               indicatoron=False, value=0, width=8, borderwidth=0,
                                               bg="grey")

        self.startHalfDateRadio.grid(row=10, column=1, padx=5, sticky="W")
        self.endHalfDateRadio.grid(row=10, column=1, padx=5, sticky="E")

        self.startHalfDateRadio.grid_remove()
        self.endHalfDateRadio.grid_remove()

        hireIMG = tk.PhotoImage(file="Resources/Drawable/btn_hire.png")
        hireButton = tk.Label(self, image=hireIMG, bg=self.bgColor)
        hireButton.image = hireIMG
        hireButton.bind("<Button-1>", lambda event: self.hireTool())
        self.grid_rowconfigure(11, weight=1)
        hireButton.grid(row=11, column=0, columnspan=2, pady=40, sticky="WE")

        # TODO
        # If file name == "ID" not exist make one
        # If exist compere date //in util?
        # Keys: HireBy,startDate,endDate,confirmedEndDate anything else? Owner(or find by tool ID)

        backButton = tk.Button(self, text="back", command=lambda: self.master.change_frame(sp.SearchToolPage, self.login))
        backButton.grid(row=0, column=0)

    def setPlaceholder(self):
        #######################################################
        # PlaceHolder
        #######################################################
        testBook = Bookings(self.tool.getID(), self.login, "24/12/2018", "26/12/2018")
        testBook2 = Bookings(self.tool.getID(), self.login, "30/12/2018", "1/1/2019")
        self.testList = []
        self.testList.append(testBook)
        self.testList.append(testBook2)
        #######################################################


    def showSecondList(self):
        self.availableEndDate.grid()
        self.endDateLabel.grid()

        if len(self.nextDays)>1:
            self.startHalfDateRadio.grid()
            self.endHalfDateRadio.grid()
        else:
            self.startHalfDateRadio.grid_remove()
            self.endHalfDateRadio.grid_remove()

    def populateStartList(self):
        self.availableDateList = util.getBookingDates(self.testList)
        for i in range(len(self.availableDateList)):
            self.availableDate.insert(END, self.availableDateList[i])

    def populateEndList(self):
        self.availableEndDate.delete(0, tk.END)
        for i in range(len(self.nextDays)):
            print(self.nextDays[i])
            self.availableEndDate.insert(END, self.nextDays[i])

    def hireTool(self):
        pass
