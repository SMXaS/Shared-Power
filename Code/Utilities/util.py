import csv
import re
import uuid
import imghdr
import os
from shutil import copy2
from datetime import datetime, timedelta
from Code.Utilities import WriteFile as wf
from Entities.User import User
from Entities.Tool import Tool
from Entities.Bookings import Bookings
import Resources.Values.strings as strings


def verifyLogin (userName, userPassword):
    """
    Use to check if login is in file

    :param str(userName)
    :param str(userPassword
    :return True or error code
    """

    exist = os.path.isfile(strings.filePath_user)
    if exist:
        with open(strings.filePath_user, 'r') as f:
            l = list(csv.reader(f))
            my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
            if userName in my_dict.get('login'):
                with open(strings.filePath_user, 'r') as f:
                    l = list(csv.reader(f))
                    my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
                    ind = my_dict['login'].index(userName)
                    if userPassword == my_dict['user_password'][ind]:
                        return True
                    else:
                        return strings.errorIncorrectPassword
            else:
                return strings.errorUserDoesntExist
    else:
        return strings.errorUserDoesntExist


def verifyRegistration (user):
    """
    Verify registration
    if its True - add user to db

    :param obj(user)
    :return True or error code

    user[0] = firstName
    user[1] = lastName
    user[2] = userName
    user[3] = post Code
    user[4] = street name
    user[5] = house number
    user[6] = email
    user[7] = email confirmation
    user[8] = password
    user[9] = password confirmation
    user[10] = phone number
    """

    # Check if entries contain spaces or empty fields
    for i in range(len(user)):
        if not user[i]:
            return strings.errorEmptyFields
        elif " " in user[i]:
            if i != 4:
                return strings.errorSpaces
    exist = os.path.isfile(strings.filePath_user)
    if exist:
        with open(strings.filePath_user, 'r') as f:
            l = list(csv.reader(f))
            my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
            if user[2] in my_dict.get('login'):
                return strings.errorUserAlreadyExist

    if user[6] != user[7]:
        return strings.errorEmailMismatch

    if not verifyEmail(user[6]):
        return strings.errorInvalidEmail

    if user[8] != user[9]:
        return strings.errorPasswordMismatch
    else:
        if len(user[8]) < 4:
            return strings.errorShortPassword

    if not str(user[10]).isdigit():
        return strings.errorInvalidEmail

    address = "{} - {}, {}".format(user[3], user[5], user[4])
    newUser = User(user[2], user[0], user[1], user[8], user[6], address, user[10])
    wf.write(newUser, strings.filePath_user, strings.fieldNames_user)
    createUserFolder(user[2])

    return True


def createUserFolder(userName):
    """
    Creates folder for users based on their userName (for invoices)

    :param userName: str (userName)
    :return: None
    """
    path = strings.filePath_invoiceFolder.format(userName)
    os.mkdir(path)


def verifyEmail(email):
    """
    Verifies email

    :param email: str
    :return: True (correct email) or False (incorrect email)
    """

    if len(email) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))


def getImageFormat(path):
    """
    Gets image format

    :param path: str (image location + extension)
    :return: str (image format. i.e. 'png', 'jpeg' etc.)
    """

    return imghdr.what(path)


def verifyIMG(path):
    """
    Verifies if IMG format is usable for our project

    :param path: str (image location)
    :return: True or error code
    """
    imgFormat = getImageFormat(path)
    if imgFormat is None:
        return False
    else:
        if imgFormat != "png":
            return False
        else:
            return True





def copyIMG(src, dst,  ID):
    """
    :param src: str (file's source location)
    :param dst: str (file's destination)
    :param ID: str (tool ID)
    :return: None
    """

    copy2(src, dst)
    oldName = getFileName(src)
    newName = "{}{}.{}".format(dst, ID, "png")
    os.rename(dst+oldName, newName)


def getFileName(path):
    """

    :param path: str (file path)
    :return: str (file name)
    """
    return os.path.basename(path)


def removeIMG(path):
    os.remove(path)


def convertFromListToObj(list):
    """
    Convert tool list to Tool object
    :param list:
    :return: obj(Tool)
    """

    return Tool(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8])


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
                    dict["imgPath"][index], dict["availability"][index])
    return tool


def convertBookingToObject(index, path):
    """
        Converts dict(tool) to obj(tool)

        :param index (in db)
        :return obj(tool)
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


def getBookingDates(bookings):
    """
    will check for ongoing bookings

    :param list(obj(bookings))
    :return list(str(available dates))
    """

    firstAvailableDate = datetime.now()
    allDateList = []
    dateFormat = strings.dateFormat
    for i in range(42):
        firstAvailableDate+= timedelta(days=1)
        # check if date is available
        # if not = pass
        allDateList.append(firstAvailableDate.strftime(dateFormat))

    if bookings:
        for i in range(len(bookings)):
            if bookings[i].getStartDate() in allDateList:
                startDate = datetime.strptime(bookings[i].getStartDate(), dateFormat)
                endDate = datetime.strptime(bookings[i].getExpectedReturnDate(), dateFormat)
                diff = endDate-startDate
                for k in range(diff.days+1):
                    nextDate = (startDate+timedelta(days=k)).strftime(dateFormat)
                    allDateList.remove(nextDate)
            else:
                if bookings[i].getExpectedReturnDate() in allDateList:
                    startDate = datetime.strptime(bookings[i].getStartDate(), dateFormat)
                    endDate = datetime.strptime(bookings[i].getExpectedReturnDate(), dateFormat)
                    diff = endDate - startDate
                    for k in range(diff.days + 1):
                        try:
                            nextDate = (startDate + timedelta(days=k)).strftime(dateFormat)
                            allDateList.remove(nextDate)
                        except ValueError:
                            continue

    return allDateList


def getNextAvailableDates(startDate, dayList):
    """
    will check available days based on startDate

    :param startDate: str(start booking date)
    :param obj(bookings)
    :return: list(str(available days))
    """

    dateFormat = strings.dateFormat
    allDateList = []
    date = datetime.strptime(startDate, dateFormat)
    firstNextDate = date
    allDateList.append(firstNextDate.strftime(dateFormat))
    for i in range(2):
        firstNextDate += timedelta(days=1)
        allDateList.append(firstNextDate.strftime(dateFormat))

    finalList = []

    for i in range(len(allDateList)):
        if allDateList[i] in dayList:
            print(allDateList[i], "is in the list")
            nextDay = allDateList[i]
            finalList.append(nextDay)

    return finalList


def getDayDifference(startDate, endDate):
    """
    checks the difference between two days

    :param startDate: str (date)
    :param endDate: str (second date)
    :return: int(difference)
    """

    dateFormat = strings.dateFormat
    date1 = datetime.strptime(startDate, dateFormat)
    date2 = datetime.strptime(endDate, dateFormat)
    diff = date2-date1
    return diff.days


def verifyBooking(startDate, availableDays, diff):
    """
    Verifies booking.

    :param startDate: str
    :param availableDays: list(all available days)
    :param diff: int(difference between start and end days)
    :return: boolean (True - approved, False - not)
    """

    dateFormat = strings.dateFormat
    date = datetime.strptime(startDate, dateFormat)
    allDateList = []
    for i in range(diff):
        date += timedelta(days=1)
        allDateList.append(date.strftime(dateFormat))

    for i in range(len(allDateList)):
        if allDateList[i] in availableDays:
            continue
        else:
            return False

    return True
