import csv
import WriteFile as wf
from Entities.User import User


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


def verifyRegistration (user):
    """
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
    """
    
    # Check if entries contain spaces or empty fields
    for i in range(len(user)):
        if not user[i]:
            print("empty fields")
            return False
        elif " " in user[i]:
            if i != 4:
                print("Contain spaces")
                return False

    # check if user exist
    with open("Data/users.csv", 'r') as f:
        l = list(csv.reader(f))
        my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
        if user[2] in my_dict.get('login'):
            return None

    if user[6] != user[7]:
        print("Email does not match")
        return False

    if user[8] != user[9]:
        print("Password does not match")
        return False
    else:
        if len(user[8]) <4:
            print("Password too short")
            return False

    address = "{} - {}, {}".format(user[3], user[5], user[4])
    newUser = User(user[2], user[0], user[1], user[8], user[6], address, 999)
    wf.add_user(dict(newUser))

    return True
