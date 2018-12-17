import RegisterPage as r
import MainMenu as mm
import tkinter as tk
import Resources.Values.values as values
import util


class StartPage(tk.Frame):

    bgColor = values.bgColor
    fgColor = values.fgColor
    errorColor = values.errorColor

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        master.title("Log in")
        master.minsize('220', '140')
        master.geometry("220x140+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-50))
        master.resizable(False, False)

        self.initUI()

        master.bind("<Return>", lambda event: self.log_in())

    def initUI(self):

        self.error_label = tk.Label(self, text="", bg=self.bgColor, fg=self.errorColor)
        self.error_label.grid(row=3, column=1, sticky=tk.W)

        lab_user = tk.Label(self, text="username", bg=self.bgColor, fg=self.fgColor)
        lab_user.grid(row=4, column=0, pady=2, padx=10)

        self.ent_user = tk.Entry(self)
        self.ent_user.grid(row=4, column=1)

        lab_pass = tk.Label(self, text="password", bg=self.bgColor, fg=self.fgColor)
        lab_pass.grid(row=5, column=0)

        self.ent_pass = tk.Entry(self, show="*")
        self.ent_pass.grid(row=5, column=1)

        b_login = tk.Label(self, text="Login", bg=self.bgColor, fg=self.fgColor, font='Helvetica 9 bold')
        b_login.grid(row=7, column=1, pady=10, sticky=tk.E)
        b_login.bind("<Button-1>", lambda event: self.log_in())

        sign_up = tk.Label(self, text="Don't have Account? Sign up", bg=self.bgColor, fg=self.fgColor,
                           font='Helvetica 7 italic')
        sign_up.grid(row=6, columnspan=2, sticky=tk.E)
        sign_up.bind("<Button-1>", lambda event: self.master.change_frame(r.RegisterPage))

    def log_in(self):
        isCorrect = util.verifyLogin(self.ent_user.get(), self.ent_pass.get())
        if isinstance(isCorrect, str):
            self.error_label.config(text=isCorrect)
        else:
            if isCorrect:
                self.master.login = self.ent_user.get()
                self.master.change_frame(mm.MainMenu)
            else:
                self.error_label.config(text="User does not exist")
                self.error_label.config(text="Something went wrong")
