import tkinter as tk
from Resources.Values import strings, colors, dimens, fonts
from Code.Utilities import util


class LoginPage(tk.Frame):

    bgColor = colors.bgColor
    fgColor = colors.fgColor
    errorColor = colors.errorColor

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg=colors.bgColor)
        self.initUI()

    def initUI(self):

        self.error_label = tk.Label(self, text="", bg=self.bgColor, fg=self.errorColor)
        self.error_label.grid(row=3, column=1, columnspan=2, sticky=tk.W)

        lab_user = tk.Label(self, text=strings.userName, bg=self.bgColor, fg=self.fgColor)
        lab_user.grid(row=4, column=0, pady=2, padx=10)

        self.ent_user = tk.Entry(self)
        self.ent_user.grid(row=4, column=1, columnspan=2)

        lab_pass = tk.Label(self, text=strings.password, bg=self.bgColor, fg=self.fgColor)
        lab_pass.grid(row=5, column=0)

        self.ent_pass = tk.Entry(self, show="*")
        self.ent_pass.grid(row=5, column=1, columnspan=2)

        b_login = tk.Label(self, text=strings.loginTitle, bg=self.bgColor, fg=self.fgColor,
                           font=fonts.buttonFont)
        b_login.grid(row=7, column=1,columnspan=2, pady=10, sticky=tk.E)
        b_login.bind("<Button-1>", lambda event: self.log_in())

        sign_upInfo = tk.Label(self, text=strings.dontHaveAccount, bg=self.bgColor, fg=self.fgColor,
                               font=fonts.dontHaveAccountFont)
        sign_upInfo.grid(row=6, column=0, columnspan=2, sticky=tk.E)
        sign_up = tk.Label(self, text=strings.signUp, bg=self.bgColor, fg=self.fgColor,
                           font=fonts.signUpFont)
        sign_up.grid(row=6, column=2, sticky=tk.E)
        sign_up.bind("<Button-1>", lambda event: self.controller.show_frame(strings.registerClass))

    def start(self, args):
        self.controller.geometry("{}x{}+%d+%d".format(dimens.loginWindowWidth, dimens.loginWindowHeigh) %
                                 ((self.winfo_screenwidth() / 2) - 100, (self.winfo_screenheight() / 2) - 50))
        self.controller.setUser("")
        self.ent_user.delete(0, "end")
        self.ent_pass.delete(0, "end")
        self.error_label.config(text="")
        self.ent_user.focus()

    def log_in(self):
        """
        Checks if user entries ar valid
        if yes - will open MainMenu

        :return: None
        """

        isCorrect = util.verifyLogin(self.ent_user.get().strip(), self.ent_pass.get())
        if isinstance(isCorrect, str):
            self.error_label.config(text=isCorrect)
        else:
            if isCorrect:
                self.controller.init(self.ent_user.get())
                self.controller.show_frame(strings.welcomeClass)
            else:
                self.error_label.config(text=strings.errorUserDoesntExist)
                self.error_label.config(text=strings.errorSomethingWrong)
