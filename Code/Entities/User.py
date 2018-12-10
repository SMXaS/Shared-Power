class User:

    def __init__(self, firstName, lastName, userName, userPassword, postCode, address,
                 email, phoneNumber):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__userName = userName
        self.__userPassword = userPassword
        self.__postCode = postCode
        self.__address = address
        self.__email = email
        self.__phoneNumber = phoneNumber

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getUserName(self):
        return self.__userName

    def getPassword(self):
        return self.__userPassword

    def getPostCode(self):
        return self.__postCode

    def getAddress(self):
        return self.__address

    def getEmail(self):
        return self.__email

    def getPhoneNumber(self):
        return self.__phoneNumber
