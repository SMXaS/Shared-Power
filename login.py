import os
from Entities.User import User


class Login:

    userPath = ""
    userName = ""
    userPassword = ""
    
    
    """
    This function will check if user enters valid information
    """
    def checkUser(self, userName, userPassword):
        self.userPath = "data/Users/{}".format(userName)
        if not os.path.exists(self.userPath):
            # If path doesn't exist - it will return None
            return None
        else:
            with open(self.userPath+"/userData.txt", "r") as myfile:
                # Opening 'userData' file and reading all entries
                line = myfile.readlines()
                passLine = []
                for x in line:
                    # Spliting every line into 3 parts
                    # Name = users_name
                    #  0   1     2
                    # storring last part (user profile) into list and trim CR off
                    passLine.append(x.split(' ')[2][:-1])
                    # Passing that list to another function
                self.user = self.__extractUserFromFile(passLine)

                # Checking if passwords matches
                if self.user.getPassword() == userPassword:
                    return True
                else:
                    return False
                myfile.close()

    """
    This Function will construct and return an Object from txtList parameter
    """
    def __extractUserFromFile(self, txtList):
        return User(txtList[0], txtList[1], txtList[2], txtList[3], txtList[4], txtList[5])


class Register:

    """
    This Function checks if user exist
    """
    def __checkIfExist(self, user):
        self.userPath = "data/Users/{}".format(user[2])
        if os.path.exists(self.userPath):
            return True
        else:
            return False

    """
    This Function will write user data into 'userData.txt' file
    """
    def __createUser(self, user):
        # Writing user data
        file = open("{}/userData.txt".format(self.userPath), "w")
        file.write("Name = {}{}".format(user[0], "\n"))
        file.write("LastName = {}{}".format(user[1], "\n"))
        file.write("UserName = {}{}".format(user[2], "\n"))
        file.write("Password = {}{}".format(user[3], "\n"))
        file.write("Email = {}{}".format(user[4], "\n"))
        file.write("Phone = {}{}".format(user[5], "\n"))
        file.close()

    """
    This Function will check if user exist. If not - will create one
    """
    def registerUser(self, user):
        if self.__checkIfExist(user):
            return True
        else:
            # Creating user directory based on userName
            os.mkdir(self.userPath)
            self.__createUser(user)
            return False
