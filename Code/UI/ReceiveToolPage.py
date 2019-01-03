import tkinter as tk
from tkinter import ttk
from Resources.Values import strings, colors, fonts
from Code.ReceiveTool import ReceiveTool


class ReceiveToolPage(tk.Frame):

    __bookingList = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__controller = controller
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.__initUI()

    def start(self, args):
        self.__receiveTool = ReceiveTool(self.__tree, self.__errorLabel, self.__controller.login)
        menuFrame = self.__controller.getMenuFrame(self)
        menuFrame.grid(row=0, column=0, sticky="WN")
        self.__receiveTool.populateList()

    def __initUI(self):
        frame = tk.Frame(self, bg=colors.bgColor)
        frame.grid(row=1, column=0, sticky="", pady=19)

        self.__tree = ttk.Treeview(frame, columns=(strings.priceDay, strings.priceHalfDay, "test"))

        mScrollBar = ttk.Scrollbar(frame, orient='vertical', command=self.__tree.yview)
        self.__tree.configure(yscrollcommand=mScrollBar.set)

        self.__errorLabel = tk.Label(frame, bg=colors.bgColor, fg=colors.errorColor)
        self.__errorLabel.grid(row=0, column=0, columnspan=2, sticky="WN")

        self.__tree.heading('#0', text=strings.tool)
        self.__tree.heading('#1', text=strings.hireDate)
        self.__tree.heading('#2', text=strings.returnDate)
        self.__tree.heading('#3', text="state")
        self.__tree.column('#1', minwidth=20, width=150, stretch=tk.YES)
        self.__tree.column('#2', minwidth=20, width=150, stretch=tk.YES)
        self.__tree.column('#0', minwidth=20, width=150, stretch=tk.YES)
        self.__tree.column('#3', minwidth=20, width=150, stretch=tk.YES)
        self.__tree.grid(row=1, column=0, columnspan=4, pady=20, sticky="N")

        mScrollBar.grid(row=1, column=5, pady=20, sticky='WNS')

        backIMG = tk.PhotoImage(file=strings.buttonBack)
        backButton = tk.Label(frame, image=backIMG, bg=colors.bgColor)
        backButton.image = backIMG
        backButton.bind("<Button-1>", lambda event: self.__controller.show_frame(strings.myToolClass))
        backButton.grid(row=2, column=1, padx=10, sticky="W")

        receiveButton = tk.Label(frame, text=strings.receiveItem, bg=colors.bgColor, fg=colors.fgColor,
                                 font=fonts.buttonFont)
        receiveButton.grid(row=2, column=2)
        receiveButton.bind("<Button-1>", lambda event: self.__receiveTool.receiveItem())

        damageButton = tk.Label(frame, text=strings.declareAsDamaged, bg=colors.bgColor, fg=colors.fgColor,
                                font=fonts.buttonFont)
        damageButton.grid(row=2, column=3)
        damageButton.bind("<Button-1>", lambda event: self.__receiveTool.damageItem())
