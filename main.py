import tkinter as tk

class SharedPower(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Shared Power")
        self.geometry("200x100+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-50))
        self.minsize('200','100')

        self._frame = None
        self.change_frame(StartPage)

    def change_frame(self, f_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = f_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        def login():
            pass

        lab_user = tk.Label(self ,text="username").grid(row=3,column=0)
        ent_user = tk.Entry(self).grid(row=3,column=1)
        lab_pass = tk.Label(self ,text="password").grid(row=4,column=0)
        ent_pass = tk.Entry(self,show="*").grid(row=4,column=1)

        b_login = tk.Button(self, text="Login",command=lambda : login()).grid(row=5,column=0)
        b_reg = tk.Button(self, text="Register",command=lambda : master.change_frame(RegisterPage)).grid(row=5,column=1)

class RegisterPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        master.geometry("280x270+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-50))

        master.title('Register')
        firstNameLabel = tk.Label(self ,text = "First Name")
        lastNameLabel = tk.Label(self ,text = "Last Name")
        userNameLabel = tk.Label(self ,text = "User Name")
        postCodeLabel = tk.Label(self ,text = "Post Code")
        streetNameLabel = tk.Label(self ,text = "Street Name")
        houseNumberLabel = tk.Label(self ,text = "House Number")
        emailLabel = tk.Label(self ,text = "Email")
        emailConfirmLabel = tk.Label(self ,text = "Email Confirmation")
        passwordLabel = tk.Label(self ,text = "Password")
        passwordConfirmationLabel = tk.Label(self ,text = "Password Confirmation")

        firstNameEntry = tk.Entry(self)
        lastNameEntry = tk.Entry(self)
        userNameEntry = tk.Entry(self)
        postCodeEntry = tk.Entry(self)
        streetNameEntry = tk.Entry(self)
        houseNumberEntry = tk.Entry(self)
        emailEntry = tk.Entry(self)
        emailConfirmEntry = tk.Entry(self)
        passwordEntry = tk.Entry(self, show = "*")
        passwordConfirmationEntry = tk.Entry(self, show = "*")

        createAccountButton = tk.Button (self, text = "Create Account")

        firstNameLabel.grid(row = 0, column = 0, sticky="E")
        lastNameLabel.grid(row = 1, column = 0, sticky="E")
        userNameLabel.grid(row = 2, column = 0, sticky="E")
        postCodeLabel.grid(row = 3, column = 0, sticky="E")
        streetNameLabel.grid(row = 4, column = 0, sticky="E")
        houseNumberLabel.grid(row = 5, column = 0, sticky="E")
        emailLabel.grid(row = 6, column = 0, sticky="E")
        emailConfirmLabel.grid(row = 7, column = 0, sticky="E")
        passwordLabel.grid(row = 8, column = 0, sticky="E")
        passwordConfirmationLabel.grid(row = 9, column = 0)

        firstNameEntry.grid(row = 0, column = 1)
        lastNameEntry.grid(row = 1, column = 1)
        userNameEntry.grid(row = 2, column = 1)
        postCodeEntry.grid(row = 3, column = 1)
        streetNameEntry.grid(row = 4, column = 1)
        houseNumberEntry.grid(row = 5, column = 1)
        emailEntry.grid(row = 6, column = 1)
        emailConfirmEntry.grid(row = 7, column = 1)
        passwordEntry.grid(row = 8, column = 1)
        passwordConfirmationEntry.grid(row = 9, column = 1)

        createAccountButton.grid(row = 10, column =1)

class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)


app = SharedPower()
app.mainloop()
