import tkinter as tk
import Resources.Values.values as values

class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.config(bg=values.bgColor)

        welcomeLabel = tk.Label(self, text=values.welcomeText, bg=values.bgColor, fg=values.fgColor,
                                font=values.welcomeFont)
        welcomeLabel.grid(row=0, column=0)

    def start(self, args):
        pass
