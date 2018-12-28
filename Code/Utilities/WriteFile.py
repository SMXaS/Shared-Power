import csv
import os


def write(obj, filePath, fieldNames, bookingFilePath=""):
    """
    This function writes an object into a file

    :param obj: object to write to the file
    :param filePath: location where to write (simple path)
    :param fieldNames: dict keys
    :param bookingFilePath: location where to write (complex path)
    :return: None
    """
    if bookingFilePath:
        path = "{}{}.csv".format(bookingFilePath, obj.getToolID())
    else:
        path = filePath
    exist = os.path.isfile(path)
    with open(path, "a") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldNames, delimiter=',', lineterminator='\n')
        if not exist:
            csv_writer.writeheader()
        csv_writer.writerow(obj.__dict__)


def change_tool(my_dict):
    with open("Data/tools.csv", "w") as f:
        csv_writer = csv.DictWriter(f, my_dict.keys())
        csv_writer.writeheader()
        csv_writer.writerow(my_dict)


def change_user(my_dict):
    with open("Data/users.csv", "w") as f:
        csv_writer = csv.DictWriter(f, my_dict.keys())
        csv_writer.writeheader()
        csv_writer.writerow(my_dict)


def add_invoice():
    pass
