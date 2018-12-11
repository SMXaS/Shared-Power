import tkinter as tk
import ReadFile as rf
import csv

user_path ="Data/users.csv"
login = 'main'
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
        global user_path
        if u_log.get() in rf.check_login():

            if u_pass.get() == rf.check_pass(u_log.get()):
                print('Logged in')

                login = u_log.get()
                self.change_frame(MainMenu)

            else:
                print('wrong password')

        else:
            print('user not exist')

    def log_out(self):
        global login
        login = 'main'
        self.change_frame(StartPage)

    def change_frame(self, f_class):
        """Destroys current frame and replaces it with a new one"""
        new_frame = f_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

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

        firstNameEntry = tk.Entry(self).grid(row = 0, column = 1)
        lastNameEntry = tk.Entry(self).grid(row = 1, column = 1)
        userNameEntry = tk.Entry(self).grid(row = 2, column = 1)
        postCodeEntry = tk.Entry(self).grid(row = 3, column = 1)
        streetNameEntry = tk.Entry(self).grid(row = 4, column = 1)
        houseNumberEntry = tk.Entry(self).grid(row = 5, column = 1)
        emailEntry = tk.Entry(self).grid(row = 6, column = 1)
        emailConfirmEntry = tk.Entry(self).grid(row = 7, column = 1)
        passwordEntry = tk.Entry(self, show = "*").grid(row = 8, column = 1)
        passwordConfirmationEntry = tk.Entry(self, show = "*").grid(row = 9, column = 1)

        createAccountButton = tk.Button (self, text = "Create Account").grid(row = 10, column =0, columnspan=2)

class MainMenu(tk.Frame):

    def __init__(self, master):
        global login
        tk.Frame.__init__(self, master)
        master.geometry("700x500+%d+%d" % ((self.winfo_screenwidth()/2)-350, (self.winfo_screenheight()/2)-250))
        master.minsize(width=500, height=500)


        root=tk.Frame(self)
        root.grid(row=0,column=0,sticky=tk.N+tk.E+tk.W)
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0,weight=1)
        ###########################
        # TOP frame start here
        ###########################
        header=tk.Frame(root,bg="red")
        header.grid(row=0,column=0,columnspan=2,sticky=tk.N+tk.E+tk.W)
        header.grid_columnconfigure(0, weight=1)
        header.grid_rowconfigure(0,weight=1)

        Label = tk.Label(header ,text = "Main menu for user: "+login).grid(row=0,column=0, sticky=tk.W)
        b_logout = tk.Button(header, text="Log Out",command=lambda : master.log_out()).grid(row=0,column=5, sticky=tk.E)

        ###########################
        # LEFT frame start here
        ###########################
        left=tk.Frame(root,bg="blue")
        left.grid(row=1,column=0)
        left.grid_columnconfigure(0, weight=1)
        left.grid_rowconfigure(0,weight=1)

        tlabel=tk.Label(left,text="Your Tools").grid(row=0,column=0,columnspan=5)

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

                tk.Label(left, text=head[list(my_dict.keys()).index(x)],borderwidth=2, relief="groove",width=6,padx=5,pady=5).grid(row=3,column=list(my_dict.keys()).index(x))

                y=0

                while y<len(items):
                    tk.Label(left ,text =my_dict[x][items[y]], borderwidth=2, relief="ridge",width=6,padx=5,pady=5).grid(row=4+y,column=list(my_dict.keys()).index(x))
                    tk.Button(left, text="more").grid(row=4+y,column=8)
                    y=y+1



        ###########################
        # RIGHT frame start here
        ###########################
        right=tk.Frame(root,bg="green")
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
                    tk.Button(right, text="more").grid(row=4+y,column=8)
                    y=y+1


        ###########################
        # RIGHT2 frame start here
        ###########################
        right2=tk.Frame(root,bg="yellow")
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


        switch_button=tk.Button(root,text="Switch",command=switch)
        switch_button.grid(row=2,column=1)


        """
        What we need in MainMenu?
        Your Tools and Hire tool only?
        """


"""Use:
class NAME OF FRAME(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

to create new frames

"""

app = SharedPower()
app.mainloop()
