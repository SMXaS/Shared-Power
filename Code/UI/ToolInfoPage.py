import tkinter as tk
from Resources.Values import strings, colors, fonts


class ToolInfoPage(tk.Frame):

    __bgColor = colors.bgColor
    __fgColor = colors.fgColor

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__controller = controller
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__initUI()

    def start(self, args):
        self.tool = args
        self.__populateInfo()

    def __initUI(self):
        frame = tk.Frame(self, bg=self.__bgColor)
        frame.grid(row=0, column=0, pady=40)

        ownerLabel = tk.Label(frame, text=strings.owner, bg=self.__bgColor, fg=self.__fgColor,
                              font=fonts.menuButtonFont)
        ownerLabel.grid(row=0, column=0, padx=5, pady=5, sticky="E")

        self.ownerTxt = tk.Label(frame, bg=self.__bgColor, fg=self.__fgColor)
        self.ownerTxt.grid(row=0, column=4, padx=5, sticky="W")

        titleLabel = tk.Label(frame, text=strings.toolTitle, bg=self.__bgColor, fg=self.__fgColor,
                              font=fonts.menuButtonFont)
        titleLabel.grid(row=1, column=0, padx=5, pady=5, sticky="E")

        self.titleTxt = tk.Label(frame, bg=self.__bgColor, fg=self.__fgColor)
        self.titleTxt.grid(row=1, column=4, padx=5, sticky="W")

        descriptionLabel = tk.Label(frame, text=strings.toolDescription, bg=self.__bgColor, fg=self.__fgColor,
                                    font=fonts.menuButtonFont)
        descriptionLabel.grid(row=2, column=0, padx=5, pady=5, sticky="E")

        self.descriptionTxt = tk.Label(frame, bg=self.__bgColor, fg=self.__fgColor, wraplength=200, justify="left")
        self.descriptionTxt.grid(row=2, column=4, padx=5, columnspan=4, sticky="W")

        conditionLabel = tk.Label(frame, text=strings.toolCondition, bg=self.__bgColor, fg=self.__fgColor,
                                  font=fonts.menuButtonFont)
        conditionLabel.grid(row=3, column=0, padx=5, pady=5, sticky="E")

        self.conditionTxt = tk.Label(frame, bg=self.__bgColor, fg=self.__fgColor)
        self.conditionTxt.grid(row=3, column=4, padx=5, sticky="W")

        priceFullDayLabel = tk.Label(frame, text=strings.priceDay, bg=self.__bgColor, fg=self.__fgColor,
                                     font=fonts.menuButtonFont)
        priceFullDayLabel.grid(row=4, column=0, padx=5, pady=5, sticky="E")

        self.priceFullDayTxt = tk.Label(frame, bg=self.__bgColor, fg=self.__fgColor)
        self.priceFullDayTxt.grid(row=4, column=4, padx=5, pady=5, sticky="W")

        priceHalfDayLabel = tk.Label(frame, text=strings.priceHalfDay, bg=self.__bgColor, fg=self.__fgColor,
                                     font=fonts.menuButtonFont)
        priceHalfDayLabel.grid(row=5, column=0, padx=5, pady=5, sticky="E")

        self.priceHalfDayTxt = tk.Label(frame, bg=self.__bgColor, fg=self.__fgColor)
        self.priceHalfDayTxt.grid(row=5, column=4, padx=5, pady=5, sticky="W")

        dispatchLabel = tk.Label(frame, text=strings.dispatchCost, bg=self.__bgColor, fg=self.__fgColor,
                                 font=fonts.menuButtonFont)
        dispatchLabel.grid(row=6, column=0, padx=5, pady=5, sticky="E")

        self.dispatchTxt = tk.Label(frame, bg=self.__bgColor, fg=self.__fgColor)
        self.dispatchTxt.grid(row=6, column=4, padx=5, pady=20, sticky="W")

        showImg = tk.Label(frame, text=strings.showImage, bg=self.__bgColor, fg=self.__fgColor,
                           font=fonts.addImageFont)
        showImg.grid(row=7, column=0, columnspan=6, padx=5, pady=5, sticky="WE")
        showImg.bind("<Button-1>", lambda event: self.__showImage())

        backIMG = tk.PhotoImage(file=strings.btn_back)
        backButton = tk.Label(frame, image=backIMG, bg=self.__bgColor)
        backButton.image = backIMG
        backButton.bind("<Button-1>", lambda event: self.__controller.show_frame(strings.searchToolClass, "args"))
        backButton.grid(row=8, column=0, padx=10, sticky="W")

        hireIMG = tk.PhotoImage(file=strings.buttonHire)
        hireButton = tk.Label(frame, image=hireIMG, bg=self.__bgColor)
        hireButton.image = hireIMG
        hireButton.bind("<Button-1>", lambda event: self.__controller.show_frame(strings.bookToolClass, self.tool))
        hireButton.grid(row=8, column=1, columnspan=5, padx=10, pady=50, sticky="E")

    def __populateInfo(self):
        """
        populating information about the tool
        :return: None
        """

        self.ownerTxt.config(text=self.tool.getOwner())
        self.titleTxt.config(text=self.tool.getTitle())
        self.descriptionTxt.config(text=self.tool.getDescription())
        self.conditionTxt.config(text=self.tool.getCondition())
        self.priceFullDayTxt.config(text="{}{}".format(strings.currency, self.tool.getPriceFullDay()))
        self.priceHalfDayTxt.config(text="{}{}".format(strings.currency, self.tool.getPriceHalfDay()))
        self.dispatchTxt.config(text="{}{}".format(strings.currency, self.tool.getRiderCharge()))

    def __showImage(self):
        """
        opens new window and shows image of selected item
        :return: None
        """

        imgWindow = tk.Toplevel(self)
        imgWindow.geometry("+300+50")
        imgWindow.resizable(False, False)
        imgWindow.wm_title("Image")
        toolIMG = tk.PhotoImage(file="{}.png".format(self.tool.getImagePath()))
        toolImgLabel = tk.Label(imgWindow, image=toolIMG)
        toolImgLabel.image = toolIMG
        toolImgLabel.grid(row=0, column=0)

