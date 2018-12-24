from Code.UI import StartPage as sp, MainMenu as mm
import Resources.Values.values as values
import tkinter as tk
from Code.Utilities import util


class RegisterPage(tk.Frame):

    bgColor = values.bgColor
    fgColor = values.fgColor
    errorColor = values.errorColor

    def __init__(self, master, arg):
        """
        :param master: master
        :param arg: None
        """

        tk.Frame.__init__(self, master)
        master.minsize(width=280, height=280)
        master.geometry("280x320+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-150))
        master.title('Register')

        self.initUI()

    def initUI(self):
        self.errorLabel = tk.Label(self, text="", bg=self.bgColor, fg=self.errorColor)
        self.errorLabel.grid(row=0, column=0, columnspan=2, padx=10)

        firstNameLabel = tk.Label(self, text="*First Name", bg=self.bgColor, fg=self.fgColor)
        firstNameLabel.grid(row=1, column=0, padx=5, pady=2, sticky="E")

        lastNameLabel = tk.Label(self, text="*Last Name", bg=self.bgColor, fg=self.fgColor)
        lastNameLabel.grid(row=2, column=0, padx=5, pady=2, sticky="E")

        userNameLabel = tk.Label(self, text="*User Name", bg=self.bgColor, fg=self.fgColor)
        userNameLabel.grid(row=3, column=0, padx=5, pady=2, sticky="E")

        postCodeLabel = tk.Label(self, text="*Post Code", bg=self.bgColor, fg=self.fgColor)
        postCodeLabel.grid(row=4, column=0, padx=5, pady=2, sticky="E")

        streetNameLabel = tk.Label(self, text="*Street Name", bg=self.bgColor, fg=self.fgColor)
        streetNameLabel.grid(row=5, column=0, padx=5, pady=2, sticky="E")

        houseNumberLabel = tk.Label(self, text="*House Number", bg=self.bgColor, fg=self.fgColor)
        houseNumberLabel.grid(row=6, column=0, padx=5, pady=2, sticky="E")

        emailLabel = tk.Label(self, text="*Email", bg=self.bgColor, fg=self.fgColor)
        emailLabel.grid(row=7, column=0, padx=5, pady=2, sticky="E")

        emailConfirmLabel = tk.Label(self, text="*Email Confirmation", bg=self.bgColor, fg=self.fgColor)
        emailConfirmLabel.grid(row=8, column=0, padx=5, pady=2, sticky="E")

        passwordLabel = tk.Label(self, text="*Password", bg=self.bgColor, fg=self.fgColor)
        passwordLabel.grid(row=9, column=0, padx=5, pady=2, sticky="E")

        passwordConfirmationLabel = tk.Label(self, text="*Password Confirmation", bg=self.bgColor, fg=self.fgColor)
        passwordConfirmationLabel.grid(row=10, column=0, padx=5, pady=2)

        self.firstNameEntry = tk.Entry(self)
        self.firstNameEntry.grid(row=1, column=1)

        self.lastNameEntry = tk.Entry(self)
        self.lastNameEntry.grid(row=2, column=1)

        self.userNameEntry = tk.Entry(self)
        self.userNameEntry.grid(row=3, column=1)

        self.postCodeEntry = tk.Entry(self)
        self.postCodeEntry.grid(row=4, column=1)

        self.streetNameEntry = tk.Entry(self)
        self.streetNameEntry.grid(row=5, column=1)

        self.houseNumberEntry = tk.Entry(self)
        self.houseNumberEntry.grid(row=6, column=1)

        self.emailEntry = tk.Entry(self)
        self.emailEntry.grid(row=7, column=1)

        self.emailConfirmEntry = tk.Entry(self)
        self.emailConfirmEntry.grid(row=8, column=1)

        self.passwordEntry = tk.Entry(self, show="*")
        self.passwordEntry.grid(row=9, column=1)

        self.passwordConfirmationEntry = tk.Entry(self, show="*")
        self.passwordConfirmationEntry.grid(row=10, column=1)

        backIMG = tk.PhotoImage(file="Resources/Drawable/btn_back.png")
        backButton = tk.Label(self, image=backIMG, bg=self.bgColor)
        backButton.image = backIMG
        backButton.grid(row=11, column=0, pady=10)
        backButton.bind("<Button-1>", lambda event: self.master.change_frame(sp.StartPage))

        createAccountButton = tk.Label(self, text="Create Account", bg=self.bgColor, fg=self.fgColor,
                                       font='Helvetica 10 bold')
        createAccountButton.grid(row=11, column=1, columnspan=2, sticky="E")
        createAccountButton.bind("<Button-1>", lambda event: self.checkRegistration())

    def checkRegistration(self):
        """
        Checks registration
        if Correct - will go to main page
        :return: None
        """

        user = []
        user.append(self.firstNameEntry.get())
        user.append(self.lastNameEntry.get())
        user.append(self.userNameEntry.get())
        user.append(self.postCodeEntry.get())
        user.append(self.streetNameEntry.get())
        user.append(self.houseNumberEntry.get())
        user.append(self.emailEntry.get())
        user.append(self.emailConfirmEntry.get())
        user.append(self.passwordEntry.get())
        user.append(self.passwordConfirmationEntry.get())

        isCorrect = util.verifyRegistration(user)
        if isinstance(isCorrect, str):
            self.errorLabel.config(text=isCorrect)
        else:
            if isCorrect:
                login = self.userNameEntry.get()
                self.master.change_frame(mm.MainMenu, login)
            else:
                self.errorLabel.config(text=isCorrect)