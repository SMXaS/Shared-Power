import tkinter as tk
from Resources.Values import strings, colors, dimens, fonts
from Code.MyInvoice import MyInvoice


class InvoicePage(tk.Frame):

    def __init__(self, parent, controller):
        """
        :param master: master
        :param arg: login
        """
        self.login = controller.login
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.__initUI()

    def start(self, args):
        MyInvoice(self.controller.login).showInvoice(self.invoiceText, self.totalLabel)

    def __initUI(self):
        frame = tk.Frame(self, bg=colors.bgColor)
        frame.grid(row=0, column=0, pady=40)

        # TODO drop down menu with year/month

        self.invoiceText = tk.Text(frame, heigh=20, width=75)
        self.invoiceText.grid(row=1, column=0)
        mScrollBar = tk.Scrollbar(frame)
        mScrollBar.grid(row=1, column=1, sticky="NS")

        mScrollBar.config(command=self.invoiceText.yview)
        self.invoiceText.config(yscrollcommand=mScrollBar.set)

        self.totalLabel = tk.Label(frame, text=strings.totalCost, bg=colors.bgColor, fg=colors.fgColor,
                                   font=fonts.buttonFont)
        self.totalLabel.grid(row=2, column=0, padx=5, pady=10, sticky="E")
