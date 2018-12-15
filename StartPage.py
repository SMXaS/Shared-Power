import RegisterPage as r
import MainMenu as mm
import tkinter as tk
import ReadFile as rf
import util
import csv

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Log in")
        master.minsize('200','100')
        master.geometry("200x100+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-50))

        u_login = tk.StringVar(self)
        u_password = tk.StringVar(self)

        lab_user = tk.Label(self ,text="username").grid(row=3,column=0)
        ent_user = tk.Entry(self, textvariable = u_login).grid(row=3,column=1)
        lab_pass = tk.Label(self ,text="password").grid(row=4,column=0)
        ent_pass = tk.Entry(self,show="*",textvariable = u_password).grid(row=4,column=1)

        b_login = tk.Button(self, text="Login",command=lambda : self.log_in(u_login, u_password)).grid(row=5,column=0)
        b_reg = tk.Button(self, text="Register",command=lambda : master.change_frame(r.RegisterPage)).grid(row=5,column=1)

    def log_in(self, u_log, u_pass):
        isCorrect = util.verifyLogin(u_log, u_pass)
        if isCorrect:
            print('Logged in')
            self.master.login = u_log.get()
            self.master.change_frame(mm.MainMenu)
        elif isCorrect == None:
            print('User does not exist')
        else:
            print('wrong password')