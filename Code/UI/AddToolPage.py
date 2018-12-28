from Code.UI import MainMenu as mm
from Code.addTool import addTool
import tkinter as tk
from tkinter import END
from Code.Utilities import util
import Resources.Values.values as values
from tkinter.filedialog import askopenfilename


class AddToolPage(tk.Frame):

    bgColor = values.bgColor
    fgColor = values.fgColor
    errorColor = values.errorColor
    width = values.mainWindowWidth
    heigh = values.mainWindowHeigh

    def __init__(self, master, arg):
        """
        :param master: master
        :param arg: user login
        """

        tk.Frame.__init__(self, master)
        self.login = arg
        self.filename = ""
        master.geometry("{}x{}+%d+%d".format(self.width, self.heigh) % ((self.winfo_screenwidth()/2)-350,
                                                                        (self.winfo_screenheight()/2)-250))
        master.title(values.addToolTitle)

        self.initUI()
        master.bind("<Return>", lambda event: self.checkTool())

    def initUI(self):

        self.errorLabel = tk.Label(self, bg=self.bgColor, fg=self.errorColor)
        self.errorLabel.grid(row=0, column=1, padx=5, pady=2, sticky="WN")

        titleLabel = tk.Label(self, text="{}{}".format(values.asterix, values.toolTitle), bg=self.bgColor, fg=self.fgColor)
        titleLabel.grid(row=1, column=0, padx=5, pady=2, sticky="E")

        DescriptionLabel = tk.Label(self, text="{}{}".format(values.asterix, values.toolDescription), bg=self.bgColor, fg=self.fgColor)
        DescriptionLabel.grid(row=2, column=0, padx=5, pady=2, sticky="EN")

        PriceDayLabel = tk.Label(self, text="{}{}".format(values.asterix, values.priceDay), bg=self.bgColor, fg=self.fgColor)
        PriceDayLabel.grid(row=3, column=0, padx=5, pady=2, sticky="E")

        PriceHalfDayLabel = tk.Label(self, text="{}{}".format(values.asterix, values.priceHalfDay),  bg=self.bgColor, fg=self.fgColor)
        PriceHalfDayLabel.grid(row=4, column=0, sticky="E")

        toolConditionLabel = tk.Label(self, text="{}{}".format(values.asterix, values.toolCondition), bg=self.bgColor, fg=self.fgColor)
        toolConditionLabel.grid(row=5, column=0, sticky="E")

        self.imgPath = tk.Label(self, text=values.emptyIMGPath, bg=self.bgColor, fg=self.fgColor)
        self.imgPath.grid(row=6, column=1, padx=5, pady=2, sticky="W")

        self.titleEntry = tk.Entry(self, width=40)
        self.titleEntry.grid(row=1, column=1, padx=5)

        self.descriptionEntry = tk.Text(self, heigh=5, width=30)
        self.descriptionEntry.grid(row=2, column=1)

        self.priceFullDayEntry = tk.Entry(self, width=40)
        self.priceFullDayEntry.grid(row=3, column=1)

        self.priceHalfDay = tk.Entry(self, width=40)
        self.priceHalfDay.grid(row=4, column=1)

        self.toolConditionEntry = tk.Entry(self, width=40)
        self.toolConditionEntry.grid(row=5, column=1)

        img_btn = tk.Label(self, text="{}{}".format(values.asterix, values.image), bg=self.bgColor, fg=self.fgColor,
                           font=values.addImageFont)
        img_btn.grid(row=6, column=0, sticky="E")
        img_btn.bind("<Button-1>", lambda event: self.setImagePath())

        addIMG = tk.PhotoImage(file=values.buttonAdd)
        addToolButton = tk.Label(self, image=addIMG, bg=self.bgColor)
        addToolButton.image=addIMG
        addToolButton.grid(row=7, column=1)
        addToolButton.bind("<Button-1>", lambda event: self.checkTool())

        backIMG = tk.PhotoImage(file=values.buttonBack)
        backButton = tk.Label(self, image=backIMG, bg=self.bgColor)
        backButton.image = backIMG
        backButton.grid(row=7, column=0, pady=20)
        backButton.bind("<Button-1>", lambda event: self.master.change_frame(mm.MainMenu, self.login))

    def setImagePath(self):
        self.filename = askopenfilename()
        self.imgPath.config(text=util.getFileName(self.filename))

    def checkTool(self):
        tool = []
        tool.append(self.titleEntry.get())
        tool.append(self.descriptionEntry.get("1.0", END))
        tool.append(self.toolConditionEntry.get())
        tool.append(self.priceFullDayEntry.get())
        tool.append(self.priceHalfDay.get())
        tool.append(self.filename)

        isCorrect = util.verifyTool(tool)
        if isinstance(isCorrect, str):
            self.errorLabel.config(text=isCorrect)
        else:
            if isCorrect:
                add = addTool(self.login)
                add.add(tool)
                self.master.change_frame(mm.MainMenu, self.login)