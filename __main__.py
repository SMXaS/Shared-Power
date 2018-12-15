import StartPage as sp
import MainMenu as mm
import tkinter as tk
import ReadFile as rf
import util
import csv

class SharedPower(tk.Tk):
    login = 'master'

    #Search atributes:
    owner = 'all'

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Shared Power")
        self.geometry("200x100+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-50))
        self.minsize('200','100')

        self.login = self.login

        self._frame = None
        self.change_frame(sp.StartPage)

    def log_in(self, u_log, u_pass):
        isCorrect = util.verifyLogin(u_log, u_pass)
        if isCorrect:
            print('Logged in')
            self.login = u_log.get()
            self.change_frame(mm.MainMenu)
        elif isCorrect == None:
            print('User does not exist')
        else:
            print('wrong password')

    def log_out(self):
        self.login = 'main'
        self.change_frame(sp.StartPage)

    def change_frame(self, f_class):
        ###########################
        #Destroys current frame and replaces it with a new one
        ###########################
        new_frame = f_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0,column=0)

"""Use:
class NAME OF FRAME(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

to create new frames

"""


app = SharedPower()
app.mainloop()
