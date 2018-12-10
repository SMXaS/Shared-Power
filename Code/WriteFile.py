import csv
class Tool:

    # -----------------------------------------------------------
    # Class Constructor
    # -----------------------------------------------------------
    def __init__(self, toolName, toolBrand, toolPrice):

        self.toolName   = toolName
        self.toolBrand  = toolBrand
        self.toolPrice  = toolPrice

    def __str__(self):

        rV = '{}$ {} {}'.format(self.toolName, self.toolBrand, self.toolPrice)
        return rV

    def __repr__(self):

        rV = '{} {} {}'.format(self.toolName, self.toolBrand, self.toolPrice)
        return rV


t1 = Tool('t1000','Makita',99)
t2 = Tool('n754n','Bosh',199)

print(t1)

f_addres = "Data/tools.csv"
field = ['toolName','toolBrand','toolPrice']

def add_record(f_addres,fn,rec):
    """Add line to CSV file.

    f_addres = file adress
    fn = Keywords for collumns
    rec = name of object you want to add

    """

    with open(f_addres, 'a') as f:

        csv_writer = csv.DictWriter(f, fieldnames=fn, delimiter=',',lineterminator='\n')
        #csv_writer.writeheader()                                                           #<<ONLY ONCE when making new file

        csv_writer.writerow(vars(rec))

add_record(f_addres,field,t2)
