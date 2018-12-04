import os
from Entities.User import User

class Login:

    userPath = ""
    userName = ""
    userPassword = ""
    user = User()
    
    #def checkUser(self, userName, userPassword):
     #   if not os.path.exists(self.path):
     #       os.mkdir(self.path)

    def checkUser(self, userName, userPassword):
        self.userPath = "data/Users/{}".format(userName)
        if not os.path.exists(self.userPath):
            return None
            #os.mkdir(userPath)
        else:
            with open(self.userPath+"/userData.txt", "r") as myfile:
                line = myfile.readlines()
                passLine = []
                for x in line:
                    passLine.append(x.split(' ')[2])
                self.user = self.__extractUserFromFile(passLine)
                if self.user.getPassword() == userPassword:
                    return True
                else:
                    return False
                myfile.close()

    def __extractUserFromFile(self, txtList):
        return User(txtList[0].strip(), txtList[1].strip(),
                    txtList[2].strip(), txtList[3].strip(),
                    txtList[4].strip(), txtList[5].strip())

class Register:

    def __checkIfExist(self, user):
        self.userPath = "data/Users/{}".format(user[2])
        if os.path.exists(self.userPath):
            return True
        else:
            return False

    def __createUser(self, user):
        file = open("{}/userData.txt".format(self.userPath), "w")
        file.write("Name = {}{}".format(user[0], "\n"))
        file.write("LastName = {}{}".format(user[1], "\n"))
        file.write("UserName = {}{}".format(user[2], "\n"))
        file.write("Password = {}{}".format(user[3], "\n"))
        file.write("Email = {}{}".format(user[4], "\n"))
        file.write("Phone = {}{}".format(user[5], "\n"))
    
    def registerUser(self, user):
        if self.__checkIfExist(user):
            return True
        else:
            os.mkdir(self.userPath)
            self.__createUser(user)
            return False
