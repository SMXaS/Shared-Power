import tkinter as tk
import Resources.Values.values as values
import csv
import ReadFile as rf
from PIL import ImageTk, Image

class BookToolPage(tk.Frame):
    placeHolder = []
    bgColor = values.bgColor
    fgColor = values.fgColor

    def __init__(self, master, tool):
        tk.Frame.__init__(self, master)
        self.tool = tool
        self.master=master
        self.login = master.login
        self.owner = master.owner
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title('Search for Tool')

        self.initUI()

    def initUI(self):
        tool = rf.get_tool("ID",self.tool.getID())

        print("tool=\n",tool)
        ownerLabel = tk.Label(self, text="Owner: \t"+tool[1], bg=self.bgColor, fg=self.fgColor)
        ownerLabel.grid(row=1, column=0, padx=5, pady=2, sticky="E")

        titleLabel = tk.Label(self, text="title: \t"+tool[2], bg=self.bgColor, fg=self.fgColor)
        titleLabel.grid(row=2, column=0, padx=5, pady=2, sticky="E")

        descriptionLabel = tk.Label(self, text="description: \t"+tool[3], bg=self.bgColor, fg=self.fgColor)
        descriptionLabel.grid(row=3, column=0, padx=5, pady=2, sticky="E")

        priceFullDayLabel = tk.Label(self, text="priceFullDay: \t"+tool[4], bg=self.bgColor, fg=self.fgColor)
        priceFullDayLabel.grid(row=4, column=0, padx=5, pady=2, sticky="E")

        priceHalfDayLabel = tk.Label(self, text="priceHalfDay: \t"+tool[5], bg=self.bgColor, fg=self.fgColor)
        priceHalfDayLabel.grid(row=5, column=0, padx=5, pady=2, sticky="E")


        img = Image.open(tool[6]+".jpeg")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        imgPathLabel = tk.Label(self, image=img)
        imgPathLabel.img = img
        imgPathLabel.grid(row=6, column=0, padx=5, pady=2, sticky="E")

        HireDayLabel = tk.Label(self, text="Date(DD/MM/YYYY): ", bg=self.bgColor, fg=self.fgColor)  #Maybe calender pop-up later on
        HireDayLabel.grid(row=7, column=0, padx=5, pady=2, sticky="E")

        HireDayEntry = tk.StringVar(self)
        HireDayEntry = tk.Entry(self, textvariable=HireDayEntry).grid(row=7, column=1)

        HireTimeLabel = tk.Label(self, text="Time(halfDays?): ", bg=self.bgColor, fg=self.fgColor)
        HireTimeLabel.grid(row=8, column=0, padx=5, pady=2, sticky="E")

        HireTimeLabel = tk.StringVar(self)
        HireTimeLabel = tk.Entry(self, textvariable=HireTimeLabel).grid(row=8, column=1)


        #TODO
        #Checkbox "first half" or "secand half" of day?
        #If file name == "ID" not exist make one
        #If exist compere date //in util?
        #file name == "ID"
        #Keys: HireBy,startDate,endDate,confirmedEndDate anything else? Owner(or find by tool ID)






