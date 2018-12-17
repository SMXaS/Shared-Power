import MainMenu as mm
import tkinter as tk
from tkinter import ttk
import csv
import BookToolPage as bk
import Resources.Values.values as values
import util


class SearchToolPage(tk.Frame):
    placeHolder = []
    bgColor = values.bgColor
    fgColor = values.fgColor

    def __init__(self, master, arg):
        tk.Frame.__init__(self, master)
        self.login = master.login
        self.owner = master.owner
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        master.title('Search for Tool')

        self.initUI()

    def initUI(self):
        self.master.columnconfigure(0, weight=1)

        backIMG = tk.PhotoImage(file="Resources/Drawable/btn_back.png")
        backButton = tk.Label(self, image=backIMG, bg=self.bgColor)
        backButton.image = backIMG
        backButton.bind("<Button-1>", lambda event: self.master.change_frame(mm.MainMenu))
        backButton.grid(row=0, column=0, sticky=tk.W)

        self.searchEntry = tk.Entry(self, width=80)
        self.searchEntry.grid(row=0, column=1, padx=5, pady=20, sticky="N")

        # TODO add fonts
        searchButton = tk.Label(self, text="Search", bg=self.bgColor, fg=self.fgColor)
        searchButton.grid(row=0, column=2)
        searchButton.bind("<Button-1>", lambda event: self.retriveData())

        self.tree = ttk.Treeview(self, columns=("Full day price", "Half day price"))
        self.tree.heading('#0', text='Title')
        self.tree.heading('#1', text='Full day price')
        self.tree.heading('#2', text='Half day price')
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=20, sticky="N")

        hireIMG = tk.PhotoImage(file="Resources/Drawable/btn_hire.png")
        hireButton = tk.Label(self, image=hireIMG, bg=self.bgColor)
        hireButton.image = hireIMG
        hireButton.bind("<Button-1>", lambda event: self.selectItem())
        hireButton.grid(row=2, column=0, columnspan=3, padx=10, pady=40)

    def selectItem(self):
        curItem = self.tree.focus()
        index = int(curItem[-1:])
        if curItem:
            index -= 1
        self.master.change_frame(bk.BookToolPage, self.placeHolder[index])


    def retriveData(self):
        self.placeHolder.clear()
        with open("Data/tools.csv", 'r') as f:
            l = list(csv.reader(f))
            my_dict = {i[0]: [x for x in i[1:]] for i in zip(*l)}
            if not self.searchEntry.get():
                items = [i for i, x in enumerate(my_dict['availability']) if x == 'yes']
            else:
                itemsa = [i for i, x in enumerate(my_dict['title']) if self.searchEntry.get().lower() in x]
                itemsb = [i for i, x in enumerate(my_dict['availability']) if x == 'yes']
                items = list(set(itemsa).intersection(itemsb))
            for i in range(len(items)):
                self.placeHolder.append(util.convertToObj(my_dict, items[i]))
            self.populateData()

    def populateData(self):

        self.tree.delete(*self.tree.get_children())

        if self.placeHolder:
            for i in range(len(self.placeHolder)):
                self.tree.insert('', 'end', text=self.placeHolder[i].getTitle(),
                                 values=(self.placeHolder[i].getPriceFullDay(),
                                         self.placeHolder[i].getPriceHalfDay()),
                                 tags=self.placeHolder[i].getID())

        """
        def set_table():
            with open("Data/tools.csv", 'r') as f:
                l = list(csv.reader(f))
                my_dict = {i[0]:[x for x in i[1:]] for i in zip(*l)}

                if self.owner == 'all':
                    items = [i for i, x in enumerate(my_dict['availability']) if x == 'yes']
                    print_table(my_dict,items)
                else:
                    itemsa = [i for i, x in enumerate(my_dict['owner']) if x == self.owner]
                    itemsb = [i for i, x in enumerate(my_dict['availability']) if x == 'yes']
                    items = list(set(itemsa).intersection(itemsb))
                    print_table(my_dict,items)

        def print_table(my_dict,items):
            del my_dict["availability"]
            del my_dict["imgPath"]
            del my_dict['ID']

            head = ['Owner','Name','Discr','PpD','PpHD','next1','next2']

            for x in my_dict:

                tk.Label(table, text=head[list(my_dict.keys()).index(x)],borderwidth=2, relief="groove",width=6,padx=5,pady=5).grid(row=3,column=list(my_dict.keys()).index(x))
                y=0
                while y<len(items):
                    tk.Label(table ,text =my_dict[x][items[y]], borderwidth=2, relief="ridge",width=6,padx=5,pady=5).grid(row=4+y,column=list(my_dict.keys()).index(x))
                    tk.Button(table, text="more/hire").grid(row=4+y,column=8)
                    y=y+1

        ###########################
        # HEADER frame start here
        ###########################
        header=tk.Frame(self,bg="red")
        header.grid(row=0,column=0,columnspan=2,sticky=tk.N+tk.E+tk.W)
        header.grid_columnconfigure(0, weight=1)
        header.grid_rowconfigure(0,weight=1)

        Label = tk.Label(header ,text = "Main menu for user: "+self.login).grid(row=0,column=0, sticky=tk.W)
        b_logout = tk.Button(header, text="Log Out",command=lambda : master.log_out()).grid(row=0,column=5, sticky=tk.E)

        ###########################
        # SEARCH frame start here
        ###########################
        search=tk.Frame(self)
        search.grid(row=1,column=0)
        search.grid_columnconfigure(0, weight=1)
        search.grid_rowconfigure(0,weight=1)

        owner_var = tk.StringVar(self)

        # Dictionary with options
        choices = set(rf.get_allfromcolumn('owner'))
        owner_var.set(self.owner) # set the default option

        popupMenu = tk.OptionMenu(search, owner_var, *choices)
        tk.Label(search, text="Choose Owner").grid(row = 1, column = 1)
        popupMenu.grid(row = 2, column =1)

        def change_owner(*args):
            master.owner = owner_var.get()

        def reset():
            master.owner = 'all'
            owner_var.set(master.owner)
            master.change_frame(SearchToolPage)

        # link function to change dropdown
        owner_var.trace('w', change_owner)
        resetB = tk.Button(search, text="Reset", command=lambda : reset()).grid(row=2,column=3, rowspan =2, sticky=tk.E)
        searchB = tk.Button(search, text="Search", command=lambda : master.change_frame(SearchToolPage)).grid(row=2,column=2, rowspan =2, sticky=tk.E)

        ###########################
        # TABLE frame start here
        ###########################
        table=tk.Frame(self)
        table.grid(row=2,column=0)
        table.grid_columnconfigure(0, weight=1)
        table.grid_rowconfigure(0,weight=1)

        set_table()

        backButton = tk.Button (self, text = "Back",command=lambda : master.change_frame(mm.MainMenu)).grid(row = 3, column =0)

        """