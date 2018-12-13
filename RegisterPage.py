import StartPage as sp
import MainMenu as mm

import tkinter as tk
import ReadFile as rf
import util
import csv

class RegisterPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Register")
        master.minsize(width=280, height=280)
        master.geometry("280x270+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-50))

        """I take stuff from Adam RegisterUiGrid and modify a bit"""
        master.title('Register')

        firstNameLabel = tk.Label(self ,text = "First Name").grid(row = 0, column = 0, sticky="E")
        lastNameLabel = tk.Label(self ,text = "Last Name").grid(row = 1, column = 0, sticky="E")
        userNameLabel = tk.Label(self ,text = "User Name").grid(row = 2, column = 0, sticky="E")
        postCodeLabel = tk.Label(self ,text = "Post Code").grid(row = 3, column = 0, sticky="E")
        streetNameLabel = tk.Label(self ,text = "Street Name").grid(row = 4, column = 0, sticky="E")
        houseNumberLabel = tk.Label(self ,text = "House Number").grid(row = 5, column = 0, sticky="E")
        emailLabel = tk.Label(self ,text = "Email").grid(row = 6, column = 0, sticky="E")
        emailConfirmLabel = tk.Label(self ,text = "Email Confirmation").grid(row = 7, column = 0, sticky="E")
        passwordLabel = tk.Label(self ,text = "Password").grid(row = 8, column = 0, sticky="E")
        passwordConfirmationLabel = tk.Label(self ,text = "Password Confirmation").grid(row = 9, column = 0)

        self.u_fName = tk.StringVar(self)
        self.u_lName = tk.StringVar(self)
        self.u_userName = tk.StringVar(self)
        self.u_postCode = tk.StringVar(self)
        self.u_stAddress = tk.StringVar(self)
        self.u_houseNumber = tk.StringVar(self)
        self.u_email = tk.StringVar(self)
        self.u_emailVerify = tk.StringVar(self)
        self.u_password = tk.StringVar(self)
        self.u_passwordVerify = tk.StringVar(self)

        firstNameEntry = tk.Entry(self, textvariable = self.u_fName).grid(row = 0, column = 1)
        lastNameEntry = tk.Entry(self, textvariable = self.u_lName).grid(row = 1, column = 1)
        userNameEntry = tk.Entry(self, textvariable = self.u_userName).grid(row = 2, column = 1)
        postCodeEntry = tk.Entry(self, textvariable = self.u_postCode).grid(row = 3, column = 1)
        streetNameEntry = tk.Entry(self, textvariable = self.u_stAddress).grid(row = 4, column = 1)
        houseNumberEntry = tk.Entry(self, textvariable = self.u_houseNumber).grid(row = 5, column = 1)
        emailEntry = tk.Entry(self, textvariable = self.u_email).grid(row = 6, column = 1)
        emailConfirmEntry = tk.Entry(self, textvariable = self.u_emailVerify).grid(row = 7, column = 1)
        passwordEntry = tk.Entry(self, show = "*", textvariable = self.u_password).grid(row = 8, column = 1)
        passwordConfirmationEntry = tk.Entry(self, show = "*", textvariable = self.u_passwordVerify).grid(row = 9, column = 1)

        backButton = tk.Button (self, text = "Back",command=lambda : master.change_frame(sp.StartPage)).grid(row = 10, column =1, columnspan=2)
        createAccountButton = tk.Button (self, text = "Create Account", command=lambda : self.checkRegistration(master)).grid(row = 10, column =0, columnspan=2)

        #######################################################
        """
        same as login. Will send data to login class, verify it and return something and add some code

        """
    #######################################
    def checkRegistration(self, master):
        global login
        user = []
        user.append(self.u_fName.get())
        user.append(self.u_lName.get())
        user.append(self.u_userName.get())
        user.append(self.u_postCode.get())
        user.append(self.u_stAddress.get())
        user.append(self.u_houseNumber.get())
        user.append(self.u_email.get())
        user.append(self.u_emailVerify.get())
        user.append(self.u_password.get())
        user.append(self.u_passwordVerify.get())

        isCorrect = util.verifyRegistration(user)
        if isCorrect:
            print()
            login = self.u_userName.get()
            master.change_frame(mm.MainMenu)
        elif isCorrect == None:
            print('User already exist')
        else:
            print('Incorrect')
    #######################################

