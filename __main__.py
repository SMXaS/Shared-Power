import StartPage as sp
import tkinter as tk
import Values.values as values


class SharedPower(tk.Tk):
    login = 'master'
    bgColor = values.bgColor
    # Search atributes:
    owner = 'all'

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Shared Power")
        self.configure(background='#0D47A1')
        self.geometry("200x100+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-20))
        self.minsize('200', '100')

        self.login = self.login

        self._frame = None
        self.change_frame(sp.StartPage)


    def log_out(self):
        self.login = 'main'
        self.change_frame(sp.StartPage)

    def change_frame(self, f_class):
        ###########################
        # Destroys current frame and replaces it with a new one
        ###########################
        new_frame = f_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.configure(background=self.bgColor)
        self._frame.grid(row=0,column=0)

"""Use:
class NAME OF FRAME(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

to create new frames

"""


app = SharedPower()
app.mainloop()
