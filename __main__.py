import tkinter as tk
import ReadFile as rf
import util
import csv

login = 'main'
owner = 'all'
class SharedPower(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Shared Power")
        self.geometry("200x100+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-50))
        self.minsize('200','100')

        self._frame = None
        self.change_frame(StartPage)

    def log_in(self, u_log, u_pass):
        global login
        isCorrect = util.verifyLogin(u_log, u_pass)
        if isCorrect:
            print('Logged in')
            login = u_log.get()
            self.change_frame(MainMenu)
        elif isCorrect == None:
            print('User does not exist')
        else:
            print('wrong password')

        ####################################################
        """
        Modification done
        """
        #####################################################

        """
        if u_log.get() in rf.check_login():

            if u_pass.get() == rf.check_pass(u_log.get()):
                print('Logged in')

                login = u_log.get()
                self.change_frame(MainMenu)

            else:
                print('wrong password')

        else:
            print('user not exist')
            """
        ########################################################

    def log_out(self):
        global login
        login = 'main'
        self.change_frame(StartPage)

    def change_frame(self, f_class):
        ###########################
        #Destroys current frame and replaces it with a new one
        ###########################
        new_frame = f_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0,column=0)

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Log in")
        master.minsize('200','100')
        master.geometry("200x100+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-50))

        u_login = tk.StringVar(self)
        u_password = tk.StringVar(self)

        lab_user = tk.Label(self ,text="username").grid(row=3,column=0)
        ent_user = tk.Entry(self, textvariable = u_login).grid(row=3,column=1)
        lab_pass = tk.Label(self ,text="password").grid(row=4,column=0)
        ent_pass = tk.Entry(self,show="*",textvariable = u_password).grid(row=4,column=1)

        b_login = tk.Button(self, text="Login",command=lambda : master.log_in(u_login, u_password)).grid(row=5,column=0)
        b_reg = tk.Button(self, text="Register",command=lambda : master.change_frame(RegisterPage)).grid(row=5,column=1)

class RegisterPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.minsize(width=280, height=280)
        master.geometry("280x270+%d+%d" % ((self.winfo_screenwidth()/2)-100, (self.winfo_screenheight()/2)-50))

        """I take stuff from Adam RegisterUiGrid and modify a bit"""
        master.title('Register')

        firstNameLabel = tk.Label(self ,text = "First Name").grid(row = 0, column = 0, sticky="E")
        lastNameLabel = tk.Label(self ,text = "Last Name").grid(row = 1, column = 0, sticky="E")
        userNameLabel = tk.Label(self ,text = "User Name").grid(row = 2, column = 0, sticky="E")
        postCodeLabel = tk.Label(self ,text = "Post Code").grid(row = 3, column = 0, sticky="E")
        streetNameLabel = tk.Label(self ,text = "Street Name").grid(row = 4, column = 0, sticky="E")
        houseNumberLabel = tk.Label(self ,text = "House Number").grid(row = 5, column = 0, sticky="E")
        emailLabel = tk.Label(self ,text = "Email").grid(row = 6, column = 0, sticky="E")
        emailConfirmLabel = tk.Label(self ,text = "Email Confirmation").grid(row = 7, column = 0, sticky="E")
        passwordLabel = tk.Label(self ,text = "Password").grid(row = 8, column = 0, sticky="E")
        passwordConfirmationLabel = tk.Label(self ,text = "Password Confirmation").grid(row = 9, column = 0)

        self.u_fName = tk.StringVar(self)
        self.u_lName = tk.StringVar(self)
        self.u_userName = tk.StringVar(self)
        self.u_postCode = tk.StringVar(self)
        self.u_stAddress = tk.StringVar(self)
        self.u_houseNumber = tk.StringVar(self)
        self.u_email = tk.StringVar(self)
        self.u_emailVerify = tk.StringVar(self)
        self.u_password = tk.StringVar(self)
        self.u_passwordVerify = tk.StringVar(self)

        firstNameEntry = tk.Entry(self, textvariable = self.u_fName).grid(row = 0, column = 1)
        lastNameEntry = tk.Entry(self, textvariable = self.u_lName).grid(row = 1, column = 1)
        userNameEntry = tk.Entry(self, textvariable = self.u_userName).grid(row = 2, column = 1)
        postCodeEntry = tk.Entry(self, textvariable = self.u_postCode).grid(row = 3, column = 1)
        streetNameEntry = tk.Entry(self, textvariable = self.u_stAddress).grid(row = 4, column = 1)
        houseNumberEntry = tk.Entry(self, textvariable = self.u_houseNumber).grid(row = 5, column = 1)
        emailEntry = tk.Entry(self, textvariable = self.u_email).grid(row = 6, column = 1)
        emailConfirmEntry = tk.Entry(self, textvariable = self.u_emailVerify).grid(row = 7, column = 1)
        passwordEntry = tk.Entry(self, show = "*", textvariable = self.u_password).grid(row = 8, column = 1)
        passwordConfirmationEntry = tk.Entry(self, show = "*", textvariable = self.u_passwordVerify).grid(row = 9, column = 1)

        backButton = tk.Button (self, text = "Back",command=lambda : master.change_frame(StartPage)).grid(row = 10, column =1, columnspan=2)
        createAccountButton = tk.Button (self, text = "Create Account", command=lambda : self.checkRegistration(master)).grid(row = 10, column =0, columnspan=2)

        #######################################################
        """
        same as login. Will send data to login class, verify it and return something and add some code

        """
    #######################################
    def checkRegistration(self, master):
        global login
        user = []
        user.append(self.u_fName.get())
        user.append(self.u_lName.get())
        user.append(self.u_userName.get())
        user.append(self.u_postCode.get())
        user.append(self.u_stAddress.get())
        user.append(self.u_houseNumber.get())
        user.append(self.u_email.get())
        user.append(self.u_emailVerify.get())
        user.append(self.u_password.get())
        user.append(self.u_passwordVerify.get())

        isCorrect = util.verifyRegistration(user)
        if isCorrect:
            print()
            login = self.u_userName.get()
            master.change_frame(MainMenu)
        elif isCorrect == None:
            print('User already exist')
        else:
            print('Incorrect')
    #######################################

class MainMenu(tk.Frame):

    def __init__(self, master):
        global login
        tk.Frame.__init__(self, master)
        master.minsize(width=500, height=500)
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth()/2)-350, (self.winfo_screenheight()/2)-250))

        ###########################
        # TOP frame start here
        ###########################
        header=tk.Frame(self,bg="red")
        header.grid(row=0,column=0,columnspan=2,sticky=tk.N+tk.E+tk.W)
        header.grid_columnconfigure(0, weight=1)
        header.grid_rowconfigure(0,weight=1)

        Label = tk.Label(header ,text = "Main menu for user: "+login).grid(row=0,column=0, sticky=tk.W)
        b_logout = tk.Button(header, text="Log Out",command=lambda : master.log_out()).grid(row=0,column=5, sticky=tk.E)

        ###########################
        # LEFT frame start here
        ###########################
        left=tk.Frame(self,bg="blue")
        left.grid(row=1,column=0)
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

            itemsa = [i for i, x in enumerate(my_dict['owner']) if x == login]
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

        tk.Button(left, text="Add tool", command=lambda : master.change_frame(AddToolPage)).grid(row=4,column=0)

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

            itemsa = [i for i, x in enumerate(my_dict['owner']) if x == login]
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
        tk.Button(self, text="Hire new tool", command=lambda : master.change_frame(SearchToolPage)).grid(row=2,column=2)

class AddToolPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.minsize('300','400')
        master.geometry("300x400+%d+%d" % ((self.winfo_screenwidth()/2)-150, (self.winfo_screenheight()/2)-200))
        master.title('Add new Tool')

        ###########################
        # HEADER frame start here
        ###########################
        header=tk.Frame(self,bg="red")
        header.grid(row=0,column=0,columnspan=2,sticky=tk.N+tk.E+tk.W)
        header.grid_columnconfigure(0, weight=1)
        header.grid_rowconfigure(0,weight=1)

        Label = tk.Label(header ,text = "Main menu for user: "+login).grid(row=0,column=0, sticky=tk.W)
        b_logout = tk.Button(header, text="Log Out",command=lambda : master.log_out()).grid(row=0,column=5, sticky=tk.E)

        ###########################
        # MID frame start here
        ###########################
        mid=tk.Frame(self)
        mid.grid(row=1,column=0)
        mid.grid_columnconfigure(0, weight=1)
        mid.grid_rowconfigure(0,weight=1)

        tk.Label(mid ,text = "Title").grid(row = 0, column = 0, sticky="E")
        tk.Label(mid ,text = "Description").grid(row = 1, column = 0, sticky="E")
        tk.Label(mid ,text = "Price per Day").grid(row = 2, column = 0, sticky="E")
        tk.Label(mid ,text = "Price per Half Day").grid(row = 3, column = 0, sticky="E")
        tk.Label(mid ,text = "Image").grid(row = 4, column = 0, sticky="E")

        titleEntry = tk.Entry(mid).grid(row = 0, column = 1)
        descriptionEntry = tk.Entry(mid).grid(row = 1, column = 1)         #Prabobly text box instad of entry box
        priceFullDayEntry = tk.Entry(mid).grid(row = 2, column = 1)
        priceHalfDay = tk.Entry(mid).grid(row = 3, column = 1)
        imgPath = tk.Entry(mid).grid(row = 4, column = 1)                  #Prabobly something else than entry box

        ###########################
        # BOTTOM frame start here
        ###########################
        bot=tk.Frame(self)
        bot.grid(row=2,column=0)
        bot.grid_columnconfigure(0, weight=1)
        bot.grid_rowconfigure(0,weight=1)

        createToolButton = tk.Button (bot, text = "Add tool").grid(row = 6, column =0)
        backButton = tk.Button (bot, text = "Back",command=lambda : master.change_frame(MainMenu)).grid(row = 6, column =1)

class ToolPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.minsize('300','400')
        master.geometry("300x400+%d+%d" % ((self.winfo_screenwidth()/2)-150, (self.winfo_screenheight()/2)-200))
        master.title('Manage Tool')

        ###########################
        # Page to fill with tool details if 'more' button next to the tool will be pressed
        ###########################

class SearchToolPage(tk.Frame):
    global owner
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.minsize('400','400')
        master.geometry("400x400+%d+%d" % ((self.winfo_screenwidth()/2)-200, (self.winfo_screenheight()/2)-200))
        master.title('Search for Tool')

        def set_table():
            with open("Data/tools.csv", 'r') as f:
                l = list(csv.reader(f))
                my_dict = {i[0]:[x for x in i[1:]] for i in zip(*l)}

                if owner == 'all':
                    items = [i for i, x in enumerate(my_dict['availability']) if x == 'yes']
                    print_table(my_dict,items)
                else:
                    itemsa = [i for i, x in enumerate(my_dict['owner']) if x == owner]
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

        Label = tk.Label(header ,text = "Main menu for user: "+login).grid(row=0,column=0, sticky=tk.W)
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
        owner_var.set(owner) # set the default option

        popupMenu = tk.OptionMenu(search, owner_var, *choices)
        tk.Label(search, text="Choose Owner").grid(row = 1, column = 1)
        popupMenu.grid(row = 2, column =1)

        def change_owner(*args):
            global owner
            owner = owner_var.get()

        def reset():
            global owner
            owner = 'all'
            owner_var.set(owner)
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

        backButton = tk.Button (self, text = "Back",command=lambda : master.change_frame(MainMenu)).grid(row = 3, column =0)

"""Use:
class NAME OF FRAME(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

to create new frames

"""


app = SharedPower()
app.mainloop()
