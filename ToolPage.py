import tkinter as tk

class ToolPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.minsize('300','400')
        master.geometry("300x400+%d+%d" % ((self.winfo_screenwidth()/2)-150, (self.winfo_screenheight()/2)-200))
        master.title('Manage Tool')
