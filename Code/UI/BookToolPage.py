import tkinter as tk
from Code.UI import SearchToolPage as sp
import Resources.Values.values as values


# Do not use PIL. This is external library


class BookToolPage(tk.Frame):
    bgColor = values.bgColor
    fgColor = values.fgColor

    def __init__(self, master, tool):
        self.login = tool[0]
        tk.Frame.__init__(self, master)

        self.tool = tool[1]
        self.master=master
        self.owner = master.owner
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title('Search for Tool')

        self.initUI()

    def initUI(self):
        ##############################################################################
        # self.tool holds entire object (include ID, owner, title, description etc.)
        # You don't need to call dict in order to get it as it is double job
        # how to access:
        #   self.tool.getID()
        #   self.tool.getOwner()
        #   self.tool.getTitle()
        #   ...
        ##############################################################################

        ownerLabel = tk.Label(self, text="Owner: \t"+self.tool.getOwner(), bg=self.bgColor, fg=self.fgColor)
        ownerLabel.grid(row=1, column=0, padx=5, pady=2, sticky="E")

        titleLabel = tk.Label(self, text="title: \t"+self.tool.getTitle(), bg=self.bgColor, fg=self.fgColor)
        titleLabel.grid(row=2, column=0, padx=5, pady=2, sticky="E")

        descriptionLabel = tk.Label(self, text="description: \t"+self.tool.getDescription(), bg=self.bgColor, fg=self.fgColor)
        descriptionLabel.grid(row=3, column=0, padx=5, pady=2, sticky="E")

        priceFullDayLabel = tk.Label(self, text="priceFullDay: \t"+self.tool.getPriceFullDay(), bg=self.bgColor, fg=self.fgColor)
        priceFullDayLabel.grid(row=4, column=0, padx=5, pady=2, sticky="E")

        priceHalfDayLabel = tk.Label(self, text="priceHalfDay: \t"+self.tool.getPriceHalfDay(), bg=self.bgColor, fg=self.fgColor)
        priceHalfDayLabel.grid(row=5, column=0, padx=5, pady=2, sticky="E")

        ########################################################################################
        # I cant find a way how to resize image, so maybe open it in new window? onClick event
        #######################################
        # path = "{}.png".format(self.tool.getImagePath())
        # img = tk.PhotoImage(file=path)
        # imgPathLabel = tk.Label(self, image=img)
        # imgPathLabel.img = img
        # imgPathLabel.grid(row=6, column=0, padx=5, pady=2, sticky="E")
        #########################################################################################

        HireDayLabel = tk.Label(self, text="Date(DD/MM/YYYY): ", bg=self.bgColor, fg=self.fgColor)  #Maybe calender pop-up later on
        HireDayLabel.grid(row=7, column=0, padx=5, pady=2, sticky="E")

        HireDayEntry = tk.StringVar(self)
        HireDayEntry = tk.Entry(self, textvariable=HireDayEntry).grid(row=7, column=1)

        HireTimeLabel = tk.Label(self, text="Time(halfDays?): ", bg=self.bgColor, fg=self.fgColor)
        HireTimeLabel.grid(row=8, column=0, padx=5, pady=2, sticky="E")

        HireTimeLabel = tk.StringVar(self)
        HireTimeLabel = tk.Entry(self, textvariable=HireTimeLabel).grid(row=8, column=1)


        #TODO
        # TODO check github issue section
        # Checkbox "first half" or "secand half" of day?
        # If file name == "ID" not exist make one
        # If exist compere date //in util?
        # file name == "ID"
        # Keys: HireBy,startDate,endDate,confirmedEndDate anything else? Owner(or find by tool ID)


        backButton = tk.Button(self, text="back", command=lambda: self.master.change_frame(sp.SearchToolPage, self.login))
        backButton.grid(row=0, column=0)
