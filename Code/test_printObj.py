def printToolObject(toolList):
    print("----------------------------")
    print("tool Objects and their attr")
    print("----------------------------")
    for i in range(len(toolList)):
        print("index:", i)
        print("ID:", toolList[i].getID())
        print("owner:", toolList[i].getOwner())
        print("description:", toolList[i].getDescription())
        print("condition:", toolList[i].getCondition())
        print("price/day:", toolList[i].getPriceFullDay())
        print("price/h day:", toolList[i].getPriceHalfDay())
        print("dispatch price:", toolList[i].getRiderCharge())
        print("img path:", toolList[i].getImagePath())
        print("availability:", toolList[i].isAvailable())
        print("--------------")


def printBookingObjects(booking):
    print("----------------------------")
    print("booking Objects and their attr")
    print("----------------------------")
    for i in range(len(booking)):
        print("index:", i)
        print("ID:", booking[i].getBookingID())
        print("tool ID:", booking[i].getToolID())
        print("user name:", booking[i].getUserName())
        print("book in condition:", booking[i].getBookInCondition())
        print("start date:", booking[i].getStartDate())
        print("start term", booking[i].getStartTerm())
        print("expected return date:", booking[i].getExpectedReturnDate())
        print("status:", booking[i].getStatus())
        print("return date:", booking[i].getReturnDate())
        print("book out condition:", booking[i].getBookOutCondition())
        print("drop off location:", booking[i].getDropOffLocation())
        print("pick up location:", booking[i].getPickUpLocation())
        print("--------------")


def printInvoiceObject(invoices):
    print("----------------------------")
    print("Invoice Objects and their attr")
    print("----------------------------")
    for i in range(len(invoices)):
        print("index:", i)
        print("user:", invoices[i].getUser())
        print("tool title:", invoices[i].getToolTitle())
        print("hire price:", invoices[i].getHirePrice())
        print("dispatch price:", invoices[i].getRiderPrice())
        print("fines:", invoices[i].getFine())
        print("--------------")
