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
    add_tool = True
    __toolObject = None

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.__controller = controller
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.__initUI()

    def start(self, args):
        self.clearEntries()
        self.__addTool = AddTool(self.__controller.login, self.errorLabel)
        if args:
            self.add_tool = False
            self.__filename = "{}.png".format(args.getImagePath())
            self.__toolObject = args
            self.__editTool()
        else:
            self.add_tool = True

        if self.add_tool:
            addIMG = tk.PhotoImage(file=strings.buttonAdd)
        else:
            addIMG = tk.PhotoImage(file=strings.buttonEdit)
            self.__controller.addToolButton.config(text=strings.editToolTitle)

        addToolButton = tk.Label(self.frame, image=addIMG, bg=self.__bgColor)
        addToolButton.image = addIMG
        addToolButton.grid(row=8, column=1, pady=20)
        addToolButton.bind("<Button-1>", lambda event: self.__add())

    def __initUI(self):

        self.frame = tk.Frame(self, bg=self.__bgColor)
        self.frame.grid(row=0, column=0, pady=51)

        self.errorLabel = tk.Label(self.frame, bg=self.__bgColor, fg=self.__errorColor)
        self.errorLabel.grid(row=0, column=0, padx=5, pady=2, sticky="WN")

        titleLabel = tk.Label(self.frame, text="{}{}".format(strings.asterisk, strings.toolTitle),
                              bg=self.__bgColor, fg=self.__fgColor)
        titleLabel.grid(row=1, column=0, padx=5, pady=2, sticky="E")

        DescriptionLabel = tk.Label(self.frame, text="{}{}".format(strings.asterisk, strings.toolDescription),
                                    bg=self.__bgColor, fg=self.__fgColor)
        DescriptionLabel.grid(row=2, column=0, padx=5, pady=2, sticky="EN")

        PriceDayLabel = tk.Label(self.frame, text="{}{}".format(strings.asterisk, strings.priceDay),
                                 bg=self.__bgColor, fg=self.__fgColor)
        PriceDayLabel.grid(row=3, column=0, padx=5, pady=2, sticky="E")

        PriceHalfDayLabel = tk.Label(self.frame, text="{}{}".format(strings.asterisk, strings.priceHalfDay),
                                     bg=self.__bgColor, fg=self.__fgColor)
        PriceHalfDayLabel.grid(row=4, column=0, sticky="E")

        riderCharge = tk.Label(self.frame, text="{}{}".format(strings.asterisk, strings.dispatchCharge),
                               bg=self.__bgColor, fg=self.__fgColor)
        riderCharge.grid(row=5, column=0, sticky="E")

        toolConditionLabel = tk.Label(self.frame, text="{}{}".format(strings.asterisk, strings.toolCondition),
                                      bg=self.__bgColor, fg=self.__fgColor)
        toolConditionLabel.grid(row=6, column=0, sticky="E")

        self.imgPath = tk.Label(self.frame, text=strings.emptyIMGPath, bg=self.__bgColor, fg=self.__fgColor)
        self.imgPath.grid(row=7, column=1, padx=5, pady=2, sticky="W")

        self.titleEntry = tk.Entry(self.frame, width=40)
        self.titleEntry.grid(row=1, column=1, padx=5)

        self.descriptionEntry = tk.Text(self.frame, heigh=5, width=30)
        self.descriptionEntry.grid(row=2, column=1)

        self.priceFullDayEntry = tk.Entry(self.frame, width=40)
        self.priceFullDayEntry.grid(row=3, column=1)

        self.priceHalfDayEntry = tk.Entry(self.frame, width=40)
        self.priceHalfDayEntry.grid(row=4, column=1)

        self.riderChargeEntry = tk.Entry(self.frame, width=40)
        self.riderChargeEntry.grid(row=5, column=1)

        self.toolConditionEntry = tk.Entry(self.frame, width=40)
        self.toolConditionEntry.grid(row=6, column=1)

        img_btn = tk.Label(self.frame, text="{}{}".format(strings.asterisk, strings.image),
                           bg=self.__bgColor, fg=self.__fgColor, font=fonts.addImageFont)
        img_btn.grid(row=7, column=0, sticky="E")
        img_btn.bind("<Button-1>", lambda event: self.__setImgPath())

    def __editTool(self):

        self.titleEntry.insert(0, self.__toolObject.getTitle())
        self.descriptionEntry.insert("1.0", self.__toolObject.getDescription())
        self.toolConditionEntry.insert(0, self.__toolObject.getCondition())
        self.priceFullDayEntry.insert(0, self.__toolObject.getPriceFullDay())
        self.priceHalfDayEntry.insert(0, self.__toolObject.getPriceHalfDay())
        self.riderChargeEntry.insert(0, self.__toolObject.getRiderCharge())
        self.imgPath.config(text=util.getFileName("{}.png".format(self.__toolObject.getImagePath())))

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
        tool.append(self.priceHalfDayEntry.get())
        tool.append(self.riderChargeEntry.get())
        tool.append(self.__filename)
        if not self.add_tool:
            tool.append(self.__toolObject.getID())
        if self.__addTool.add(tool, self.add_tool):
            self.clearEntries()
            self.__controller.show_frame(strings.myToolClass)

    def clearEntries(self):
        self.titleEntry.delete(0, "end")
        self.descriptionEntry.delete("1.0", "end")
        self.riderChargeEntry.delete(0, "end")
        self.imgPath.config(text="")
        self.toolConditionEntry.delete(0, "end")
        self.priceFullDayEntry.delete(0, "end")
        self.priceHalfDayEntry.delete(0, "end")
        self.titleEntry.focus()
