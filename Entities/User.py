class User:

    def __init__(self, userName, firstName, lastName, userPassword, email, address, phoneNumber):
        self.first_name = firstName
        self.last_name = lastName
        self.login = userName
        self.user_password = userPassword
        self.user_adress = address
        self.email = email
        self.user_phone_number = phoneNumber

    def getFirstName(self):
        return self.__first_name

    def getLastName(self):
        return self.last_name

    def getUserName(self):
        return self.login

    def getPassword(self):
        return self.user_password

    def getAddress(self):
        return self.user_adress

    def getEmail(self):
        return self.email

    def getPhoneNumber(self):
        return self.user_phone_number
