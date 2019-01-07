import tkinter as tk
from tkinter import ttk
from Resources.Values import strings, colors, fonts
from Code.MyInvoice import MyInvoice
import datetime, calendar
import Code.Utilities.util as util


class InvoicePage(tk.Frame):
    currentDate = datetime.datetime.now().strftime(strings.invoiceMonth_YearFormat)
    #currentDate = "02-2019"
    currentMonth = datetime.datetime.now().strftime(strings.invoiceMonthFormat)
    currentYear = datetime.datetime.now().strftime(strings.invoiceYearFormat)
    yearList = []
    monthList = []
    checkedMonth = ""
    checkedYear = ""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__controller = controller
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.__initUI()

    def start(self, args):
        MyInvoice(self.__controller.login).showInvoice(self.invoiceText, self.totalLabel, self.currentDate)
        self.__controller.addToolButton.config(text=strings.menuAddTool)
        self.__getDates()

    def __initUI(self):
        frame = tk.Frame(self, bg=colors.bgColor)
        frame.grid(row=0, column=0, pady=40)
        tempYearList = ["2019"]
        tempMonthList = ["01", "02", "03", "04", "05", "06"]
        index = 0

        self.yearVar = tk.StringVar(self)
        self.monthVar = tk.StringVar(self)

        self.monthMenu = ttk.Combobox(frame, state="readonly", textvariable= self.monthVar)
        self.monthMenu.grid(row=0, column=0, sticky="W", pady=5)
        self.monthMenu.bind("<<ComboboxSelected>>", lambda event: self.__selectDate())

        self.yearMenu = ttk.Combobox(frame, state="readonly", textvariable= self.yearVar)
        self.yearMenu.grid(row=0, column=1, sticky="W")
        self.yearMenu.bind("<<ComboboxSelected>>", lambda event: self.__selectDate())

        self.invoiceText = tk.Text(frame, heigh=20, width=75)
        self.invoiceText.grid(row=1, column=0, columnspan=5)
        mScrollBar = tk.Scrollbar(frame)
        mScrollBar.grid(row=1, column=5, sticky="NS")
        mScrollBar.config(command=self.invoiceText.yview)
        self.invoiceText.config(yscrollcommand=mScrollBar.set)

        self.totalLabel = tk.Label(frame, bg=colors.bgColor, fg=colors.fgColor,
                                   font=fonts.buttonFont)
        self.totalLabel.grid(row=2, column=4, padx=5, pady=10, sticky="E")

    def __selectDate(self):
        """
        Handling date selection and populates invoice based on it
        :return: None
        """

        date = "{}-{}".format(self.monthList[self.monthMenu.current()], self.yearList[self.yearMenu.current()])
        MyInvoice(self.__controller.login).showInvoice(self.invoiceText, self.totalLabel, date)

    def __getDates(self):
        """
        Gets all dates from Invoice folder, splits it into moth/year and populates it in optionMenu widget
        :return: None
        """

        fullMonthNames = []
        dateList = util.getInvoiceDates(self.__controller.login)
        if not dateList:
            dateList.append(self.currentDate)
        else:
            if self.currentDate not in dateList:
                dateList.append(self.currentDate)
        for i in range(len(dateList)):
            year = dateList[i].split("-")[1]
            month = dateList[i].split("-")[0]

            if year not in self.yearList:
                self.yearList.append(year)

            self.monthList.append(month)
            monthName = calendar.month_name[int(month)]

            if monthName not in fullMonthNames:
                fullMonthNames.append(monthName)

        index = 0

        for i in range(len(dateList)):
            print("index: {}; dateList: {};".format(i, dateList[i]))
            if self.currentDate == dateList[i]:
                index = i

        print("index:", index)

        self.monthMenu.config(values=fullMonthNames)
        self.yearMenu.config(values=self.yearList)
        self.monthMenu.current(index)
        self.yearMenu.current(0)



