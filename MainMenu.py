import AddToolPage as at
import SearchToolPage as st
import tkinter as tk
import csv
import Resources.Values.values as values

class MainMenu(tk.Frame):

    bgColor = values.bgColor
    fgColor = values.fgColor

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.login = master.login

        master.minsize(width=500, height=500)
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth()/2)-250, (self.winfo_screenheight()/2)-150))
        master.title("Main Menu")
        #################################################
        # menu
        #################################################


        ###########################
        # TOP frame start here
        ###########################
        header=tk.Frame(self,bg="red")
        header.grid(row=0,column=0,columnspan=2,sticky=tk.N+tk.E+tk.W)
        header.grid_columnconfigure(0, weight=1)
        header.grid_rowconfigure(0,weight=1)

        Label = tk.Label(header ,text = "Main menu for user: "+self.login).grid(row=0,column=0, sticky=tk.W)
        b_logout = tk.Button(header, text="Log Out",command=lambda : master.log_out()).grid(row=0,column=5, sticky=tk.E)

        ###########################
        # LEFT frame start here
        ###########################
        left=tk.Frame(self,bg="blue")
        left.grid(row=2,column=0)
        left.grid_columnconfigure(0, weight=1)
        left.grid_rowconfigure(0,weight=1)

        ###########################
        # LEFT frame 1st row 'Your Tools' label
        ###########################

        tlabel=tk.Label(left,text="Your Tools").grid(row=0,column=0,columnspan=5)

        ###########################
        # LEFT frame 2nd row 'Your available tools'
        ###########################
        table_your_tools=tk.Frame(left,bg="pink")
        table_your_tools.grid(row=1,column=0)

        tlabel=tk.Label(table_your_tools,text="Your Tools to rent").grid(row=0,column=0,columnspan=5)
        with open("Data/tools.csv", 'r') as f:
            l = list(csv.reader(f))
            my_dict = {i[0]:[x for x in i[1:]] for i in zip(*l)}

            itemsa = [i for i, x in enumerate(my_dict['owner']) if x == self.login]
            itemsb = [i for i, x in enumerate(my_dict['availability']) if x == 'yes']
            items = list(set(itemsa).intersection(itemsb))
            print(itemsa)
            print(itemsb)
            print(items)

            del my_dict["availability"]
            del my_dict["imgPath"]
            del my_dict['owner']
            del my_dict['ID']

            head = ['Name','Discr','PpD','PpHD','next1','next2']

            for x in my_dict:

                tk.Label(table_your_tools, text=head[list(my_dict.keys()).index(x)],borderwidth=2, relief="groove",width=6,padx=5,pady=5).grid(row=3,column=list(my_dict.keys()).index(x))

                y=0

                while y<len(items):
                    tk.Label(table_your_tools ,text =my_dict[x][items[y]], borderwidth=2, relief="ridge",width=6,padx=5,pady=5).grid(row=4+y,column=list(my_dict.keys()).index(x))
                    tk.Button(table_your_tools, text="more").grid(row=4+y,column=8)
                    y=y+1

        ###########################
        # LEFT frame 3rd row 'Add tool' button
        ###########################

        tk.Button(left, text="Add tool", command=lambda : master.change_frame(at.AddToolPage)).grid(row=4,column=0)

        ###########################
        # RIGHT frame start here
        ###########################
        right=tk.Frame(self,bg="green")
        right.grid(row=1,column=1)

        right.isgridded=True #Dynamically add "isgridded" attribute.
        tlabel=tk.Label(right,text="Your booked Tools will be here... maybe").grid(row=0,column=0,columnspan=5)

        with open("Data/tools.csv", 'r') as f:
            l = list(csv.reader(f))
            my_dict = {i[0]:[x for x in i[1:]] for i in zip(*l)}

            itemsa = [i for i, x in enumerate(my_dict['owner']) if x == self.login]
            itemsb = [i for i, x in enumerate(my_dict['availability']) if x == 'no']
            items = list(set(itemsa).intersection(itemsb))
            print(itemsa)
            print(itemsb)
            print(items)

            del my_dict["availability"]
            del my_dict["imgPath"]
            del my_dict['owner']
            del my_dict['ID']

            head = ['Name','Discr','PpD','PpHD','next1','next2']

            for x in my_dict:

                tk.Label(right, text=head[list(my_dict.keys()).index(x)],borderwidth=2, relief="groove",width=6,padx=5,pady=5).grid(row=3,column=list(my_dict.keys()).index(x))

                y=0

                while y<len(items):
                    tk.Label(right ,text =my_dict[x][items[y]], borderwidth=2, relief="ridge",width=6,padx=5,pady=5).grid(row=4+y,column=list(my_dict.keys()).index(x))
                    tk.Button(right, text="more/manage").grid(row=4+y,column=8)
                    y=y+1

        ###########################
        # RIGHT2 frame start here
        ###########################
        right2=tk.Frame(self,bg="yellow")
        right2.isgridded=False
        right2_label=tk.Label(right2,text="text2")
        right2_label.grid(row=0,column=0)

        def switch():
            print ("Called")
            if(right.isgridded):
                right.isgridded=False
                right.grid_forget()
                right2.isgridded=True
                right2.grid(row=1,column=1)
            else:
                right2.isgridded=False
                right2.grid_forget()
                right.isgridded=True
                right.grid(row=1,column=1)

        switch_button=tk.Button(self,text="Switch",command=switch)
        switch_button.grid(row=2,column=1)
        tk.Button(self, text="Hire new tool", command=lambda : master.change_frame(st.SearchToolPage)).grid(row=2,column=2)
