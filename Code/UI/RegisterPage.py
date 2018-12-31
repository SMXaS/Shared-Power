from Resources.Values import strings, colors, dimens, fonts
from Code.Utilities import util
import tkinter as tk


class RegisterPage(tk.Frame):

    bgColor = colors.bgColor
    fgColor = colors.fgColor
    errorColor = colors.errorColor

    def __init__(self, parent, controller):
        """
        :param master: master
        :param arg: None
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=colors.bgColor)
        self.initUI()

    def start(self, args):
        self.controller.geometry("{}x{}+%d+%d".format(dimens.registerWindowWidth, dimens.registerWindowHeigh) %
                                 ((self.winfo_screenwidth() / 2) - 100, (self.winfo_screenheight() / 2) - 150))

        # resetting views
        self.firstNameEntry.delete(0, "end")
        self.lastNameEntry.delete(0, "end")
        self.userNameEntry.delete(0, "end")
        self.postCodeEntry.delete(0, "end")
        self.streetNameEntry.delete(0, "end")
        self.houseNumberEntry.delete(0, "end")
        self.emailEntry.delete(0, "end")
        self.emailConfirmEntry.delete(0, "end")
        self.passwordEntry.delete(0, "end")
        self.passwordConfirmationEntry.delete(0, "end")
        self.phoneNumberEntry.delete(0, "end")

        # set focus
        self.firstNameEntry.focus()

    def initUI(self):
        self.errorLabel = tk.Label(self, text="", bg=self.bgColor, fg=self.errorColor)
        self.errorLabel.grid(row=0, column=0, columnspan=2, padx=10)

        firstNameLabel = tk.Label(self, text="{}{}".format(strings.asterix, strings.firstName),
                                  bg=self.bgColor, fg=self.fgColor)
        firstNameLabel.grid(row=1, column=0, padx=5, pady=2, sticky="E")

        lastNameLabel = tk.Label(self, text="{}{}".format(strings.asterix, strings.lastName),
                                 bg=self.bgColor, fg=self.fgColor)
        lastNameLabel.grid(row=2, column=0, padx=5, pady=2, sticky="E")

        userNameLabel = tk.Label(self, text="{}{}".format(strings.asterix, strings.userName),
                                 bg=self.bgColor, fg=self.fgColor)
        userNameLabel.grid(row=3, column=0, padx=5, pady=2, sticky="E")

        postCodeLabel = tk.Label(self, text="{}{}".format(strings.asterix, strings.postCode),
                                 bg=self.bgColor, fg=self.fgColor)
        postCodeLabel.grid(row=4, column=0, padx=5, pady=2, sticky="E")

        streetNameLabel = tk.Label(self, text="{}{}".format(strings.asterix, strings.streetName),
                                   bg=self.bgColor, fg=self.fgColor)
        streetNameLabel.grid(row=5, column=0, padx=5, pady=2, sticky="E")

        houseNumberLabel = tk.Label(self, text="{}{}".format(strings.asterix, strings.houseNumber),
                                    bg=self.bgColor, fg=self.fgColor)
        houseNumberLabel.grid(row=6, column=0, padx=5, pady=2, sticky="E")

        emailLabel = tk.Label(self, text="{}{}".format(strings.asterix, strings.email), bg=self.bgColor,
                              fg=self.fgColor)
        emailLabel.grid(row=7, column=0, padx=5, pady=2, sticky="E")

        emailConfirmLabel = tk.Label(self, text="{}{}".format(strings.asterix, strings.emailConfirmation),
                                     bg=self.bgColor, fg=self.fgColor)
        emailConfirmLabel.grid(row=8, column=0, padx=5, pady=2, sticky="E")

        passwordLabel = tk.Label(self, text="{}{}".format(strings.asterix, strings.password),
                                 bg=self.bgColor, fg=self.fgColor)
        passwordLabel.grid(row=9, column=0, padx=5, pady=2, sticky="E")

        passwordConfirmationLabel = tk.Label(self, text="{}{}".format(strings.asterix, strings.passwordConfirmation),
                                             bg=self.bgColor, fg=self.fgColor)
        passwordConfirmationLabel.grid(row=10, column=0, padx=5, pady=2)

        phoneNumberLabel = tk.Label(self, text="{}{}".format(strings.asterix, strings.phoneNumber),
                                    bg=self.bgColor, fg=self.fgColor)
        phoneNumberLabel.grid(row=11, column=0, padx=5, pady=2, sticky="E")

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

        self.phoneNumberEntry = tk.Entry(self)
        self.phoneNumberEntry.grid(row=11, column=1)

        backIMG = tk.PhotoImage(file=strings.buttonBack)
        backButton = tk.Label(self, image=backIMG, bg=self.bgColor)
        backButton.image = backIMG
        backButton.grid(row=12, column=0, pady=10)
        backButton.bind("<Button-1>", lambda event: self.controller.show_frame(strings.loginClass))

        createAccountButton = tk.Label(self, text=strings.createAccount, bg=self.bgColor, fg=self.fgColor,
                                       font=fonts.buttonFont)
        createAccountButton.grid(row=12, column=1, columnspan=2, sticky="E")
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
        user.append(self.phoneNumberEntry.get())

        isCorrect = util.verifyRegistration(user)
        if isinstance(isCorrect, str):
            self.errorLabel.config(text=isCorrect)
        else:
            if isCorrect:
                self.controller.init(self.userNameEntry.get())
                self.controller.show_frame(strings.welcomeClass)
            else:
                self.errorLabel.config(text=isCorrect)
