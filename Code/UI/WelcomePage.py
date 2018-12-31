import tkinter as tk
from Resources.Values import strings, colors, fonts


class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.config(bg=colors.bgColor)

        welcomeLabel = tk.Label(self, text=strings.welcomeText, bg=colors.bgColor, fg=colors.fgColor,
                                font=fonts.welcomeFont)
        welcomeLabel.grid(row=0, column=0)
        poweredByLabel = tk.Label(self, text="Powered by ", bg=colors.bgColor, fg=colors.fgColor)
        poweredByLabel.grid(row=1, column=0, sticky="SE")
        ownerLabel = tk.Label(self, text="Wood Division", bg=colors.bgColor, fg=colors.fgColor,
                              font=fonts.owners)
        ownerLabel.grid(row=1, column=1, sticky="SE")

    def start(self, args):
        pass
