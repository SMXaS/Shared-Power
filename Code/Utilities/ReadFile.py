import csv
import glob
import os
from Code.Utilities import converters
from Resources.Values import strings


# TODO work in progress to clean this part as I presume there is some boilerplate code
def getTool(returnObj, column, value):
    """
    :param returnObj: boolean value. True - want to return object. False - want to return list
    :param column: str(witch column)
    :param value: str(value)
    :return: object or list
    """
    exist = os.path.isfile("Data/tools.csv")
    if exist:
        with open(strings.filePath_tool, 'r') as f:
            l = list(csv.reader(f))
            my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
            item = [i for i, x in enumerate(my_dict[column]) if value.lower() in x.lower()]

        if returnObj:
            itemList = []
            for i in range(len(item)):
                itemList.append(converters.convertToObj(item[i]))
            return itemList
        else:
            return item

def get_allfromcolumn(key):
    """
    Use to get everything from column in 'tools.csv'

    You need to pass:
    key = name of the column

    """
    with open("Data/tools.csv", 'r') as f:
        l = list(csv.reader(f))
        my_dict = {i[0]:[x for x in i[1:]] for i in zip(*l)}
        return my_dict.get(key)

def get_tool(key,value):
    """
    Use to get row from 'tools.csv' file

    You need to pass:
    key = name of the column
    value = value in that column

    """
    with open(strings.filePath_tool, 'r') as f:
        tool = []
        l = list(csv.reader(f))
        my_dict = {i[0]:[x for x in i[1:]] for i in zip(*l)}
        ind = my_dict[key].index(value)
        for x in my_dict:
            tool.append(my_dict[x][ind])
        return tool

def get_alltools():
    """
    Use to get all tools from file 'tools.csv' as dict

    """
    with open("Data/tools.csv", 'r') as f:
        l = list(csv.reader(f))
        my_dict = {i[0]:[x for x in i[1:]] for i in zip(*l)}
        return my_dict

def getAllBookings(column, arg, status):
    pathList = glob.glob(strings.filePath_allBookings)

    itemList = []
    for i in range(len(pathList)):
        with open(pathList[i], 'r') as f:
            l = list(csv.reader(f))
            my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
            item = [i for i, x in enumerate(my_dict[column]) if arg == x]
            for k in range(len(item)):
                if my_dict["status"][item[k]] == strings.toolStatus[status]:
                    itemList.append(converters.convertBookingToObject(item[k], pathList[i]))

    return itemList

def getAllInvoices(column, arg, path):
    itemList = []
    with open(path, 'r') as f:
        l = list(csv.reader(f))
        my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
        item = [i for i, x in enumerate(my_dict[column]) if arg == x]
        for k in range(len(item)):
            itemList.append(converters.convertInvoiceToObj(item[k], path))

    return itemList

def isOngoingBooking(tool):
    path = "{}{}.csv".format(strings.filePath_booking, tool.getID())

    if os.path.isfile(path) == True:
        with open(path, "r") as f:
            l = list(csv.reader(f))
            my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
            start = my_dict.get('startDate')
            end = [i for i, x in enumerate(my_dict['returnDate']) if x == None]
            if len(start) > len(end):
                return 'yes'
            else:
                return 'no'
    else:
        return 'no'


"""

def search_tools(key,value):
    
    Use to get all tools from file 'tools.csv' where columb contain value

    You need to pass:
    key = name of the column
    value = value in that column

    
    with open("Data/users.csv", 'r') as f:
        l = list(csv.reader(f))
        my_dict = {i[0]:[x for x in i[1:]] for i in zip(*l)}
        items = [i for i, x in enumerate(my_dict[key]) if x == value]

        print('\n___________OptionA__________')

        for x in my_dict:
            print('======================')
            y=0
            while y<len(items):
                print(my_dict[x][items[y]])
                y=y+1

        print('\n+++++++++++OptionB+++++++++++++')

        for y in range(0, len(items)):
            print('======================')
            for x in my_dict:
                print(my_dict[x][items[y]])
"""
