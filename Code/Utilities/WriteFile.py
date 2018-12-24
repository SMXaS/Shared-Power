import csv
import os

def add_user(user):
    """Add line to CSV file.

    user = name of object you want to add

    """
    fn_user = ['login','first_name','last_name','user_password','email','user_adress','user_phone_number']

    filePath = "Data/users.csv"
    exist = os.path.isfile(filePath)

    with open(filePath, "a") as f:

        csv_writer = csv.DictWriter(f, fieldnames=fn_user, delimiter=',',lineterminator='\n')

        if not exist:
            csv_writer.writeheader()

        csv_writer.writerow(user.__dict__)

def add_tool(tool):
    """Add line to CSV file.

    tool = name of object you want to add

    """
    fn_tool = ['ID','owner','title','description','condition','priceFullDay','priceHalfDay','imgPath','availability']

    filePath = "Data/tools.csv"
    exist = os.path.isfile(filePath)

    with open(filePath, "a") as f:

        csv_writer = csv.DictWriter(f, fieldnames=fn_tool, delimiter=',',lineterminator='\n')

        if not exist:
            csv_writer.writeheader()

        csv_writer.writerow(tool.__dict__)

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

def add_booking(book):

    fn_book = ['toolID','userName','bookInCondition','startDate', 'startTerm','expectedReturnDate',
               'expectedTerm','returnDate','bookOutCondition']

    filePath = "Data/Bookings/"+book.getToolID()+".csv"
    exist = os.path.isfile(filePath)
    with open(filePath, "a") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fn_book, delimiter=',',lineterminator='\n')

        if not exist:
            csv_writer.writeheader()

        csv_writer.writerow(book.__dict__)

def add_invoice():
    pass
