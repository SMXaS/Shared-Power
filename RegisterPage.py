import StartPage as sp
import MainMenu as mm
import Values.values as values
import tkinter as tk
import util


class RegisterPage(tk.Frame):

    bgColor = values.bgColor
    fgColor = values.fgColor
    errorColor = values.errorColor

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Register")
        master.minsize(width=280, height=280)
        master.minsize('280', '330')
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

        firstNameEntry = tk.Entry(self, textvariable=self.u_fName).grid(row=1, column=1)
        lastNameEntry = tk.Entry(self, textvariable=self.u_lName).grid(row=2, column=1)
        userNameEntry = tk.Entry(self, textvariable=self.u_userName).grid(row=3, column=1)
        postCodeEntry = tk.Entry(self, textvariable=self.u_postCode).grid(row=4, column=1)
        streetNameEntry = tk.Entry(self, textvariable=self.u_stAddress).grid(row=5, column=1)
        houseNumberEntry = tk.Entry(self, textvariable=self.u_houseNumber).grid(row=6, column=1)
        emailEntry = tk.Entry(self, textvariable=self.u_email).grid(row=7, column=1)
        emailConfirmEntry = tk.Entry(self, textvariable=self.u_emailVerify).grid(row=8, column=1)
        passwordEntry = tk.Entry(self, show="*", textvariable=self.u_password).grid(row=9, column=1)
        passwordConfirmationEntry = tk.Entry(self, show="*", textvariable=self.u_passwordVerify)
        passwordConfirmationEntry.grid(row=10, column=1)

        backIMG = tk.PhotoImage(file="Assets/btn_back.png")
        backButton = tk.Label(self, image=backIMG, bg=self.bgColor)
        backButton.image = backIMG
        backButton.grid(row=11, column=0, pady=10)
        backButton.bind("<Button-1>", lambda event: self.master.change_frame(sp.StartPage))

        #backButton = tk.Button(self, text="Back", command=lambda: self.master.change_frame(sp.StartPage))
        #backButton.grid(row=11, column=0, pady=10)

        createAccountButton = tk.Label(self, text="Create Account", bg=self.bgColor, fg=self.fgColor,
                                       font='Helvetica 10 bold')
        createAccountButton.grid(row=11, column=1, columnspan=2, sticky="E")
        createAccountButton.bind("<Button-1>", lambda event: self.checkRegistration(self.master))

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
        if isinstance(isCorrect, str):
            self.errorLabel.config(text=isCorrect)
        else:
            if isCorrect:
                print()
                login = self.u_userName.get()
                master.change_frame(mm.MainMenu)
            else:
                self.errorLabel.config(text=isCorrect)