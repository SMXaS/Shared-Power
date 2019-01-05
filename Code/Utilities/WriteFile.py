import csv
import os

def write(obj, filePath, fieldNames, complexFilePath="", filePathParam=""):
    """
    This function writes an object into a file

    :param obj: object to write to the file
    :param filePath: location where to write (simple path)
    :param fieldNames: dict keys
    :param bookingFilePath: location where to write (complex path)
    :return: None
    """
    if complexFilePath:
        path = "{}{}.csv".format(complexFilePath, filePathParam)
    else:
        path = filePath

    exist = os.path.isfile(path)
    with open(path, "a") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldNames, delimiter=',', lineterminator='\n')
        if not exist:
            csv_writer.writeheader()
        csv_writer.writerow(obj.__dict__)


def edit_tool(tool):
    """
    #toolID - ID of edited tool as string
    #new_tool - new tool data(same as add tool)+ availability as a list

    """
    my_dict = {}
    if not tool:
        print('no data')
    else:
        with open("Data/tools.csv", "r") as f:
            l = list(csv.reader(f))
            my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
            ind = my_dict['ID'].index(tool.getID())

            my_dict['title'][ind] = tool.getTitle()
            my_dict['description'][ind] = tool.getDescription()
            my_dict['condition'][ind] = tool.getCondition()
            my_dict['priceFullDay'][ind] = tool.getPriceFullDay()
            my_dict['priceHalfDay'][ind] = tool.getPriceHalfDay()
            my_dict['riderCharge'][ind] = tool.getRiderCharge()
            my_dict['imgPath'][ind] = tool.getImagePath()
            my_dict['availability'][ind] = tool.isAvailable()

        val=[]
        all_keys=[]
        all_items=[]
        for i,j in my_dict.items():
            all_keys.append(i)
            all_items.append(j)

        val = list(zip(all_items[0],all_items[1],all_items[2],all_items[3],all_items[4],all_items[5],all_items[6],all_items[7],all_items[8],all_items[9]))

        with open("Data/tools.csv", "w") as f:
            writer = csv.writer(f, delimiter=',', lineterminator='\n')
            writer.writerow(all_keys)
            y=0
            while y<len(val):
                writer.writerow(val[y])
                y=y+1

def cancel_booking(book_path, bookID):
    """
    book_path - book file name as string
    bookID - bookID as string

    """
    my_dict = {}
    with open(book_path, "r") as f:
        l = list(csv.reader(f))
        my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
        ind = my_dict['bookingID'].index(bookID)

        val=[]
        all_keys=[]
        all_items=[]
        for i,j in my_dict.items():
            all_keys.append(i)
            all_items.append(j)

        val = list(zip(all_items[0],all_items[1],all_items[2],all_items[3],all_items[4],all_items[5],all_items[6],all_items[7],all_items[8],all_items[9],all_items[10],all_items[11],all_items[12]))

        val.pop(ind)

    with open(book_path, "w") as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(all_keys)
        y=0
        while y<len(val):
            writer.writerow(val[y])
            y=y+1

def add_invoice():
    pass
