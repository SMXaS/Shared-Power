from Code.AddTool import AddTool
import tkinter as tk
from tkinter import END
from Resources.Values import strings, colors, dimens, fonts
from tkinter.filedialog import askopenfilename
import Code.Utilities.util as util


class AddToolPage(tk.Frame):

    __bgColor = colors.bgColor
    __fgColor = colors.fgColor
    __errorColor = colors.errorColor
    __width = dimens.mainWindowWidth
    __heigh = dimens.mainWindowHeigh
    __filename = ""

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.__controller = controller
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.__initUI()

    def start(self, args):
        self.__addTool = AddTool(self.__controller.login, self.errorLabel)

    def __initUI(self):

        frame = tk.Frame(self, bg=self.__bgColor)
        frame.grid(row=0, column=0, pady=40)

        self.errorLabel = tk.Label(self, bg=self.__bgColor, fg=self.__errorColor)
        self.errorLabel.grid(row=0, column=0, padx=5, pady=2, sticky="WN")

        titleLabel = tk.Label(frame, text="{}{}".format(strings.asterix, strings.toolTitle),
                              bg=self.__bgColor, fg=self.__fgColor)
        titleLabel.grid(row=1, column=0, padx=5, pady=2, sticky="E")

        DescriptionLabel = tk.Label(frame, text="{}{}".format(strings.asterix, strings.toolDescription),
                                    bg=self.__bgColor, fg=self.__fgColor)
        DescriptionLabel.grid(row=2, column=0, padx=5, pady=2, sticky="EN")

        PriceDayLabel = tk.Label(frame, text="{}{}".format(strings.asterix, strings.priceDay),
                                 bg=self.__bgColor, fg=self.__fgColor)
        PriceDayLabel.grid(row=3, column=0, padx=5, pady=2, sticky="E")

        PriceHalfDayLabel = tk.Label(frame, text="{}{}".format(strings.asterix, strings.priceHalfDay),
                                     bg=self.__bgColor, fg=self.__fgColor)
        PriceHalfDayLabel.grid(row=4, column=0, sticky="E")

        riderCharge = tk.Label(frame, text="{}{}".format(strings.asterix, strings.dispatchCharge),
                               bg=self.__bgColor, fg=self.__fgColor)
        riderCharge.grid(row=5, column=0, sticky="E")

        toolConditionLabel = tk.Label(frame, text="{}{}".format(strings.asterix, strings.toolCondition),
                                      bg=self.__bgColor, fg=self.__fgColor)
        toolConditionLabel.grid(row=6, column=0, sticky="E")

        self.imgPath = tk.Label(frame, text=strings.emptyIMGPath, bg=self.__bgColor, fg=self.__fgColor)
        self.imgPath.grid(row=7, column=1, padx=5, pady=2, sticky="W")

        self.titleEntry = tk.Entry(frame, width=40)
        self.titleEntry.grid(row=1, column=1, padx=5)

        self.descriptionEntry = tk.Text(frame, heigh=5, width=30)
        self.descriptionEntry.grid(row=2, column=1)

        self.priceFullDayEntry = tk.Entry(frame, width=40)
        self.priceFullDayEntry.grid(row=3, column=1)

        self.priceHalfDay = tk.Entry(frame, width=40)
        self.priceHalfDay.grid(row=4, column=1)

        self.riderChargeEntry = tk.Entry(frame, width=40)
        self.riderChargeEntry.grid(row=5, column=1)

        self.toolConditionEntry = tk.Entry(frame, width=40)
        self.toolConditionEntry.grid(row=6, column=1)

        img_btn = tk.Label(frame, text="{}{}".format(strings.asterix, strings.image),
                           bg=self.__bgColor, fg=self.__fgColor, font=fonts.addImageFont)
        img_btn.grid(row=7, column=0, sticky="E")
        img_btn.bind("<Button-1>", lambda event: self.__setImgPath())

        addIMG = tk.PhotoImage(file=strings.buttonAdd)
        addToolButton = tk.Label(frame, image=addIMG, bg=self.__bgColor)
        addToolButton.image=addIMG
        addToolButton.grid(row=8, column=1)
        addToolButton.bind("<Button-1>", lambda event: self.__add())

    def __setImgPath(self):
        self.__filename = askopenfilename()
        self.imgPath.config(text=util.getFileName(self.__filename))

    def __add(self):
        tool = []
        description = self.descriptionEntry.get("1.0", END)[:-1]

        tool.append(self.titleEntry.get())
        tool.append(description)
        tool.append(self.toolConditionEntry.get())
        tool.append(self.priceFullDayEntry.get())
        tool.append(self.priceHalfDay.get())
        tool.append(self.riderChargeEntry.get())
        tool.append(self.__filename)

        if self.__addTool.add(tool):
            pass
            # TODO  clear entries include error message
            # TODO go back to myToolPage
