from tkinter import END
import Code.Utilities.WriteFile as wf
import Code.Utilities.ReadFile as rf
import Code.Utilities.util as utils
from Entities.Invoice import Invoice
from Resources.Values import strings
import Code.test_printObj as test
import datetime
import os


class MyInvoice:
    __currentMonth = datetime.datetime.now().strftime(strings.invoiceMonth_YearFormat)
    __currentMonthPlaceholder = "02-2019"
    __currentDatePlaceholder = "05/02/2019"
    __currentDate = datetime.datetime.now().strftime(strings.dateFormat)

    # TODO hired date/return date?

    def __init__(self, login):
        self.__login = login

    def generateInvoice(self, bookingObj):
        """
        generates invoice based on bookings

        :param bookingObj: booking object
        :return: None
        """

        toolDict = rf.get_tool("ID", bookingObj.getToolID())
        toolObject = utils.convertFromListToObj(toolDict)
        path = "{}{}/".format(strings.filePath_invoiceFolder, self.__login)
        invoiceObj = Invoice(self.__login, toolObject.getTitle(), self.__calculateHirePrice(bookingObj, toolObject),
                             self.__calculateRiderPrice(bookingObj, toolObject),
                             self.__calculateFine(bookingObj, toolObject))

        wf.write(invoiceObj, None, strings.fieldNames_invoice, path, self.__currentMonth)

    def __calculateHirePrice(self, bookingObj, toolObj):
        """
        Calculates hire price

        :param bookingObj: booking object
        :param toolObj: tool object
        :return: float(hire price)
        """

        diff = utils.getDayDifference(bookingObj.getStartDate(), bookingObj.getExpectedReturnDate()) + 1
        startTerm = bookingObj.getStartTerm()
        endTerm = bookingObj.getExpectedTerm()
        toolPriceFullDay = float(toolObj.getPriceFullDay())
        toolPriceHalfDay = float(toolObj.getPriceHalfDay())

        price = 0.0

        if startTerm == "f":
            firstDayPrice = toolPriceFullDay
        else:
            firstDayPrice = toolPriceHalfDay

        if endTerm == "f":
            lastDayPrice = toolPriceFullDay
        else:
            lastDayPrice = toolPriceHalfDay

        if diff < 2:
            price = firstDayPrice
        else:
            for i in range(diff):
                if i == 0:
                    price += firstDayPrice
                elif i == diff-1:
                    price += lastDayPrice
                else:
                    price += toolPriceFullDay

        return "%.2f" % price

    def __calculateRiderPrice(self, bookingObj, toolObj):
        """
        calculates dispatch cost

        :param bookingObj: booking object
        :param toolObj: tool object
        :return: float(dispatch cost)
        """

        riderPrice = 0
        if bookingObj.getPickUpLocation():
            riderPrice += float(toolObj.getRiderCharge())

        if bookingObj.getDropOffLocation():
            riderPrice += float(toolObj.getRiderCharge())

        return "%.2f" % riderPrice

    def __calculateFine(self, bookingObj, toolObj):
        """
        calculates fine for late return
        :param bookingObj: booking object
        :param toolObj: tool object
        :return: float(fine)
        """

        diff = utils.getDayDifference(bookingObj.getExpectedReturnDate(), self.__currentDate)
        fullPrice = float(toolObj.getPriceFullDay())

        if diff > 0:
            fine = float(fullPrice) * diff
        else:
            fine = 0

        return "%.2f" % fine

    def showInvoice(self, txtBox, totalLabel, date):
        """
        calculates total cost for given month bookings and populates that information (with total amount)
        on textBox widget

        :param txtBox: textBox widget(holds all information about bookings prices)
        :param totalLabel: Label widget(holds information about total cost)
        :param date: selected date
        :return: None
        """

        path = "{}{}/{}.csv".format(strings.filePath_invoiceFolder, self.__login, date)
        exist = os.path.isfile(path)
        invoiceList = []

        monthlyFee = 5.0
        hireCost = 0.0
        dispatchCost = 0.0
        fine = 0.0

        if exist:
            invoiceList = rf.getAllInvoices("user", self.__login, path)

        test.printInvoiceObject(invoiceList)

        txtBox.config(state="normal")

        txtBox.delete(1.0, END)
        txtBox.insert(END, self.__login + "\n")
        fileName = utils.getFileName(path)[:-4]
        txtBox.insert(END, fileName + "\n\n")
        for i in range(len(invoiceList)):
            txtBox.insert(END, "{} {}".format(strings.toolTitleForInvoice, invoiceList[i].getToolTitle()) + "\n")
            txtBox.insert(END, "{} {}{}".format(strings.toolCost, strings.currency,
                                                 invoiceList[i].getHirePrice()) + "\n")
            hireCost += float(invoiceList[i].getHirePrice())

            if float(invoiceList[i].getRiderPrice()) > 0:
                txtBox.insert(END, "{} {}{}".format(strings.dispatchCost, strings.currency,
                                                     invoiceList[i].getRiderPrice()) + "\n")
                dispatchCost += float(invoiceList[i].getRiderPrice())

            if float(invoiceList[i].getFine()) > 0:
                txtBox.insert(END, "{} {}{}".format(strings.fines, strings.currency,
                                                     invoiceList[i].getFine()) + "\n")
                fine += float(invoiceList[i].getFine())

            txtBox.insert(END, "-------------------------------------------------------\n")

        txtBox.config(state="disabled")

        totalPrice = "%.2f" % sum([hireCost, dispatchCost, fine])
        if float(totalPrice) > 0:
            totalPrice = float(monthlyFee) + float(totalPrice)
        totalLabel.config(text="{} {}{}".format(strings.totalCost,  strings.currency, totalPrice))
