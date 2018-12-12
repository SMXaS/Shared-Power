import csv

def verifyLogin (userName, userPassword):
    """
    Use to check if login is in file
    """
    with open("Data/users.csv", 'r') as f:
        l = list(csv.reader(f))
        my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
        if userName.get() in my_dict.get('login'):
            with open("Data/users.csv", 'r') as f:
                l = list(csv.reader(f))
                my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
                ind = my_dict['login'].index(userName.get())

                if userPassword.get() == my_dict['user_password'][ind]:
                    return True
                else:
                    return False
        else:
            return None

                #return my_dict['user_password'][ind]
        #return my_dict.get('login')


def verifyRegistration (user):
    return False
