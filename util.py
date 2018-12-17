import csv
import re
import uuid
import imghdr
import os
from shutil import copy2
import WriteFile as wf
from Entities.User import User
from Entities.Tool import Tool


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
                    return "Incorrect password"
        else:
            return "User does not exist!"


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
            return "empty fields"
        elif " " in user[i]:
            if i != 4:
                return "Contain spaces"

    # check if user exist
    with open("Data/users.csv", 'r') as f:
        l = list(csv.reader(f))
        my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
        if user[2] in my_dict.get('login'):
            return "User already exist"

    if user[6] != user[7]:
        return "Email does not match"

    if not verifyEmail(user[6]):
        return "Invalid email address"

    if user[8] != user[9]:
        return "Password does not match"
    else:
        if len(user[8]) < 4:
            return "Password is too short"

    address = "{} - {}, {}".format(user[3], user[5], user[4])
    newUser = User(user[2], user[0], user[1], user[8], user[6], address, 999)
    wf.add_user(newUser)

    return True


def verifyEmail(email):
    if len(email) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))


def getImageFormat(path):
    return imghdr.what(path)


def verifyIMG(path):
    imgFormat = getImageFormat(path)
    if imgFormat is None:
        print("Wrong image format")
        return False
    elif imgFormat == "gif":
        print("Wrong image format")
        return False
    else:
        return True


def verifyTool(tool):
    """
    tool[0] = title
    tool[1] = description
    tool[2] = price full day
    tool[3] = price half day
    tool[4] = img path
    """
    for i in range(len(tool)):
        if not tool[i]:
            print("Empty fields")
            return False
        if i == 2 or i == 3:
            if " " in tool[i]:
                print("empty space in field")
                return False
    
    try:
        val = float(tool[2])
        val = float(tool[3])
    except ValueError:
        print("Incorrect Price format")
        return False

    if not verifyIMG(tool[4]):
        return False

    return True


def copyIMG(src, dst,  ID):
    copy2(src, dst)
    oldName = os.path.basename(src)
    newName = "{}{}.{}".format(dst, ID, getImageFormat(src))
    os.rename(dst+oldName, newName)


def generateID():
    return uuid.uuid4()


def removeIMG(path):
    pass
