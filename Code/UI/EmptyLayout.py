import tkinter as tk
from Resources.Values import strings, colors, fonts


class EmptyLayout(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.config(bg=colors.bgColor)

        emptyLabel = tk.Label(self, text="Your list is empty..", bg=colors.bgColor, fg=colors.fgColor,
                              font=fonts.welcomeFont)
        emptyLabel.grid(row=0, column=0)

    def start(self, args):
        pass
