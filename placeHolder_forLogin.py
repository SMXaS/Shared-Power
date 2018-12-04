from Class.login import Login
from Class.login import Register

login = Login()
register = Register()

def logIn():
    check = login.checkUser("amazon4ever", "bubble")
    if check:
        print("Correct!")
    elif check == None:
        print("user doesn't exist")
    else:
        print("Incorrect..")


def registerUser():
    user = ["Stefan", "Sofrone", "amazon4ever", "bubble", "stefan@gmail.com",
            "555547"]
    check = register.registerUser(user)
    if check:
        print("User Exist")
    else:
        print("User Created!")

logIn()
#registerUser()
