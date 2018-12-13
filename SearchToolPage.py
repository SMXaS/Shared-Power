import MainMenu as mm

import tkinter as tk
import ReadFile as rf
import util
import csv

class SearchToolPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.login = master.login
        self.owner = master.owner
        master.minsize('400','400')
        master.geometry("400x400+%d+%d" % ((self.winfo_screenwidth()/2)-200, (self.winfo_screenheight()/2)-200))
        master.title('Search for Tool')

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
