import csv


def add_user(user):
    """Add line to CSV file.

    user = name of object you want to add

    """
    fn_user = ['login','first_name','last_name','user_password','email','user_adress','user_phone_number']

    with open("Data/users.csv", 'a') as f:

        csv_writer = csv.DictWriter(f, fieldnames=fn_user, delimiter=',',lineterminator='\n')

        #csv_writer.writeheader()                                                           #<<ONLY ONCE when making new file
        csv_writer.writerow(user.__dict__)

def add_tool(tool):
    """Add line to CSV file.

    tool = name of object you want to add

    """
    fn_tool = ['ID','owner','title','description','priceFullDay','priceHalfDay','imgPath','availability']

    with open(Data/tools.csv, 'a') as f:

        csv_writer = csv.DictWriter(f, fieldnames=fn_tool, delimiter=',',lineterminator='\n')

        #csv_writer.writeheader()                                                           #<<ONLY ONCE when making new file
        csv_writer.writerow(tool.__dict__)

def add_invoice():
    pass
