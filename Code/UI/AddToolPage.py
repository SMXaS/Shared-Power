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

    def __init__(self, master, arg):
        tk.Frame.__init__(self, master)
        self.login = arg
        self.filename = ""
        master.minsize('380','260')
        master.geometry("380x260+%d+%d" % ((self.winfo_screenwidth()/2)-150, (self.winfo_screenheight()/2)-200))
        master.title('Add new Tool')

        self.initUI()
        master.bind("<Return>", lambda event: self.checkTool())

    def initUI(self):

        self.errorLabel = tk.Label(self, bg=self.bgColor, fg=self.errorColor)
        self.errorLabel.grid(row=0, column=1, padx=5, pady=2, sticky="WN")

        titleLabel = tk.Label(self, text="*Title", bg=self.bgColor, fg=self.fgColor)
        titleLabel.grid(row=1, column=0, padx=5, pady=2, sticky="E")

        DescriptionLabel = tk.Label(self, text="*Description", bg=self.bgColor, fg=self.fgColor)
        DescriptionLabel.grid(row=2, column=0, padx=5, pady=2, sticky="EN")

        PriceDayLabel = tk.Label(self, text="*Price per Day", bg=self.bgColor, fg=self.fgColor)
        PriceDayLabel.grid(row=3, column=0, padx=5, pady=2, sticky="E")

        PriceHalfDayLabel = tk.Label(self, text="*Price per Half Day",  bg=self.bgColor, fg=self.fgColor)
        PriceHalfDayLabel.grid(row=4, column=0, sticky="E")

        self.imgPath = tk.Label(self, text="...", bg=self.bgColor, fg=self.fgColor)
        self.imgPath.grid(row=5, column=1, padx=5, pady=2, sticky="W")

        self.titleEntry = tk.Entry(self, width=40)
        self.titleEntry.grid(row=1, column=1, padx=5)

        self.descriptionEntry = tk.Text(self, heigh=5, width=30)
        self.descriptionEntry.grid(row=2, column=1)

        self.priceFullDayEntry = tk.Entry(self, width=40)
        self.priceFullDayEntry.grid(row=3, column=1)

        self.priceHalfDay = tk.Entry(self, width=40)
        self.priceHalfDay.grid(row=4, column=1)

        img_btn = tk.Label(self, text="Image", bg=self.bgColor, fg=self.fgColor,
                           font='Helvetica 10 underline bold')
        img_btn.grid(row=5, column=0, sticky="E")
        img_btn.bind("<Button-1>", lambda event: self.setImagePath())

        addIMG = tk.PhotoImage(file="Resources/Drawable/btn_add.png")
        addToolButton = tk.Label(self, image=addIMG, bg=self.bgColor)
        addToolButton.image=addIMG
        addToolButton.grid(row=6, column=1)
        addToolButton.bind("<Button-1>", lambda event: self.checkTool())

        backIMG = tk.PhotoImage(file="Resources/Drawable/btn_back.png")
        backButton = tk.Label(self, image=backIMG, bg=self.bgColor)
        backButton.image = backIMG
        backButton.grid(row=6, column=0, pady=20)
        backButton.bind("<Button-1>", lambda event: self.master.change_frame(mm.MainMenu, self.login))

    def setImagePath(self):
        self.filename = askopenfilename()
        self.imgPath.config(text=util.getFileName(self.filename))

    def checkTool(self):
        tool = []
        tool.append(self.titleEntry.get())
        tool.append(self.descriptionEntry.get("1.0", END))
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