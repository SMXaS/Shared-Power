from Entities.Invoice import Invoice
from Entities.Bookings import Bookings
from Entities.Tool import Tool
from Resources.Values import strings
import csv


def convertToObj(index):
    """
    Converts dict(tool) to obj(tool)

    :param index (in db)
    :return obj(tool)
    """

    with open(strings.filePath_tool, 'r') as f:
        l = list(csv.reader(f))
        dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
        tool = Tool(dict["ID"][index], dict["owner"][index], dict["title"][index],
                    dict["description"][index], dict["condition"][index],
                    dict["priceFullDay"][index], dict["priceHalfDay"][index],
                    dict["riderCharge"][index], dict["imgPath"][index], dict["availability"][index])
    return tool


def convertBookingToObject(index, path):
    """
        Converts dict(booking) to obj(booking)

        :param index (in db)
        :return obj(booking)
        """

    with open(path, 'r') as f:
        l = list(csv.reader(f))
        myDict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
        booking = Bookings(myDict["bookingID"][index], myDict["toolID"][index], myDict["userName"][index],
                           myDict["bookInCondition"][index],
                           myDict["startDate"][index], myDict["startTerm"][index],
                           myDict["expectedReturnDate"][index], myDict["expectedTerm"][index], myDict["status"][index],
                           myDict["returnDate"][index], myDict["bookOutCondition"][index],
                           myDict["pickUpLocation"][index], myDict["dropOffLocation"][index])
    return booking


def convertInvoiceToObj(index, path):
    """
        Converts dict(invoice) to obj(invoice)

        :param index (in db)
        :return obj(invoice)
        """

    with open(path, 'r') as f:
        l = list(csv.reader(f))
        myDict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
        invoice = Invoice(myDict["user"][index], myDict["toolTitle"][index], myDict["hirePrice"][index],
                           myDict["riderPrice"][index], myDict["fine"][index])
    return invoice