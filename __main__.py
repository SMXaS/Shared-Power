import tkinter as tk
from tkinter import ttk
from Code.UI.SearchToolPage import SearchToolPage
from Code.UI.AddToolPage import AddToolPage
from Code.UI.WelcomePage import WelcomePage
from Code.UI.MyToolPage import MyToolPage
from Code.UI.ReturnToolPage import ReturnToolPage
from Code.UI.BookToolPage import BookToolPage
from Code.UI.LoginPage import LoginPage
from Code.UI.RegisterPage import RegisterPage
from Resources.Values import strings, colors, dimens, fonts

# TODO clear entries after usage, reset search tool list


class mainMenu(tk.Tk):

    login = ""
    page_name = ""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("{}x{}+%d+%d".format(dimens.mainWindowWidth, dimens.mainWindowHeigh) %
                      ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        self.resizable(False, False)
        self.title(strings.appTitle)

        #############################
        # Defining frames and widgets
        #############################
        mainFrame = tk.Frame(self)
        mainFrame.pack(side="top", fill="both", expand=True)

        self.menuFrame = tk.Frame(mainFrame, bg=colors.bgColor, width=100)
        self.menuFrame.pack(side="left", fill="y")
        menuBorder = ttk.Separator(self.menuFrame, orient="vertical")
        menuBorder.pack(side="right", fill="y")

        # this frame "container" will be dynamic
        container = tk.Frame(mainFrame)
        container.pack(side="right", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Menu frame widgets
        userIMG = tk.PhotoImage(file=strings.account)
        user = tk.Label(self.menuFrame, image=userIMG, bg=colors.bgColor)
        user.image = userIMG
        user.pack(side="top", padx=50, pady=10)

        self.userName = tk.Label(self.menuFrame, bg=colors.bgColor, fg=colors.fgColor)
        self.userName.pack(side="top", padx=5, pady=2)

        divider = ttk.Separator(self.menuFrame, orient="horizontal")
        divider.pack(side="top", fill="x",padx=10, pady=20)

        myToolsButton = tk.Label(self.menuFrame, text=strings.menuMyTools, bg=colors.bgColor, fg=colors.fgColor,
                                 font=fonts.menuButtonFont)
        myToolsButton.bind("<Button-1>", lambda event: self.show_frame(strings.myToolClass))
        myToolsButton.pack(side="top", padx=5, pady=2)

        myBookingsButton = tk.Label(self.menuFrame, text=strings.menuMyBookings, bg=colors.bgColor,
                                    fg=colors.fgColor, font=fonts.menuButtonFont)
        myBookingsButton.bind("<Button-1>", lambda event: self.show_frame(strings.returnToolClass))
        myBookingsButton.pack(side="top", padx=5, pady=2)

        addToolButton = tk.Label(self.menuFrame, text=strings.menuAddTool, bg=colors.bgColor, fg=colors.fgColor,
                                 font=fonts.menuButtonFont)
        addToolButton.bind("<Button-1>", lambda event: self.show_frame(strings.addToolClass))
        addToolButton.pack(side="top", padx=5, pady=2)

        searchToolButton = tk.Label(self.menuFrame, text=strings.menuSearchTool, bg=colors.bgColor,
                                    fg=colors.fgColor, font=fonts.menuButtonFont)

        searchToolButton.bind("<Button-1>", lambda event: self.show_frame(strings.searchToolClass))
        searchToolButton.pack(side="top", padx=5, pady=2)

        logOutButton = tk.Label(self.menuFrame, text=strings.menuLogOut, bg=colors.bgColor, fg=colors.fgColor,
                                font=fonts.menuLogOutFont)
        logOutButton.bind("<Button-1>", lambda event: self.show_frame(strings.loginClass))
        logOutButton.pack(side="bottom", padx=5, pady=10)

        # adding menu buttons to the list for easier highlighting
        self.buttonList = (myToolsButton, myBookingsButton, addToolButton, searchToolButton)

        # disabling menu frame in order to populate login/register pages
        self.menuFrame.pack_forget()

        # setting up external classes
        self.frames = {}

        for F in (SearchToolPage, AddToolPage, WelcomePage, MyToolPage, ReturnToolPage, BookToolPage, LoginPage,
                  RegisterPage):
            self.page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[self.page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # initializing with "LoginPage"
        self.show_frame(strings.loginClass)

    def show_frame(self, page_name, args=[]):
        """
        This is main function in order to change frames
        :param page_name: str(class name which you want to populate)
        :param args: **optional** list(whatever you want to send to the requested frame)
        :return: None
        """

        # pulling the requested frame
        frame = self.frames[page_name]
        frame.tkraise()
        self.page_name = page_name

        # sending arguments and initializing logic
        frame.start(args)

        # adjusting menu button fonts
        self.checkButton()

    def init(self, login):
        """
        This function is setting up window geometry and user
        :param login: str(userName)
        :return: None
        """

        # setting up user name
        self.setUser(login)
        self.userName.config(text=login)

        # populating menu frame
        self.menuFrame.pack(side="left", fill="y")

        # setting up window size
        self.geometry("{}x{}+%d+%d".format(dimens.mainWindowWidth, dimens.mainWindowHeigh) %
                                          ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))

    def setUser(self, user):
        """
        This is separate function in case if you want to reset user name outside this class
        :param user: str(user name)
        :return: None
        """

        self.login = user

    def checkButton(self):
        """
        This function checks which menu button is pressed (based on which frame is called) in order
        to highlight it. It will send buttonList index of that button to 'highlighButton' method
        :return: None
        """

        if self.page_name is strings.myToolClass:
            self.highlightButton(0)
        elif self.page_name is strings.returnToolClass:
            self.highlightButton(1)
        elif self.page_name is strings.addToolClass:
            self.highlightButton(2)
        elif self.page_name is strings.searchToolClass:
            self.highlightButton(3)

    def highlightButton(self, index):
        """
        This function changing fonts for all buttons based on the index
        :param index: int(buttonList index)
        :return: None
        """

        # looping through buttonList and looking for match.
        for i in range(len(self.buttonList)):
            if index == i:
                self.buttonList[i].config(font=fonts.menuButtonPressedFont)
            else:
                self.buttonList[i].config(font=fonts.menuButtonFont)


if __name__ == "__main__":
    app = mainMenu()
    app.mainloop()
