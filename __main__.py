import tkinter as tk
from tkinter import ttk
from Code.UI.SearchToolPage import SearchToolPage
from Code.UI.WelcomePage import WelcomePage
from Code.UI.MyToolPage import MyToolPage
from Code.UI.BookToolPage import BookToolPage
from Code.UI.LoginPage import LoginPage
from Code.UI.RegisterPage import RegisterPage
from Code.UI.ToolInfoPage import ToolInfoPage
from Code.UI.MyProfilePage import MyProfilePage
from Resources.Values import strings, colors, dimens, fonts


class mainMenu(tk.Tk):

    login = ""
    page_name = ""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title(strings.appTitle)

        #############################
        # Defining frames and widgets
        #############################
        mainFrame = tk.Frame(self)
        mainFrame.pack(side="top", fill="both", expand=True)

        self.menuFrame = tk.Frame(mainFrame, bg=colors.menuBgColor, width=100)
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
        user = tk.Label(self.menuFrame, image=userIMG, bg=colors.menuBgColor)
        user.image = userIMG
        user.pack(side="top", padx=50, pady=10)

        self.userName = tk.Label(self.menuFrame, bg=colors.menuBgColor, fg=colors.fgColor)
        self.userName.pack(side="top", padx=5, pady=2)

        divider = ttk.Separator(self.menuFrame, orient="horizontal")
        divider.pack(side="top", fill="x", padx=10, pady=10)

        myProfileFrame = tk.Frame(self.menuFrame, bg=colors.menuBgColor)
        myProfileFrame.pack(side="top", fill="x", pady=10)

        toolIMG = tk.PhotoImage(file=strings.tool_img)
        tool = tk.Label(myProfileFrame, image=toolIMG, bg=colors.menuBgColor)
        tool.image = toolIMG
        tool.pack(side="top", padx=5, pady=2)

        myProfileButton = tk.Label(myProfileFrame, text=strings.myProfile, bg=colors.menuBgColor,
                                   fg=colors.fgColor, font=fonts.menuButtonFont)
        myProfileButton.pack(side="top", padx=5, pady=5)

        myProfileFrame.bind("<Button-1>", lambda event: self.show_frame(strings.myProfileClass))
        myProfileButton.bind("<Button-1>", lambda event: self.show_frame(strings.myProfileClass))
        tool.bind("<Button-1>", lambda event: self.show_frame(strings.myProfileClass))

        searchToolFrame = tk.Frame(self.menuFrame, bg=colors.menuBgColor)
        searchToolFrame.pack(side="top", fill="x")

        searchIMG = tk.PhotoImage(file=strings.search_img)
        search = tk.Label(searchToolFrame, image=searchIMG, bg=colors.menuBgColor)
        search.image = searchIMG
        search.pack(side="top", padx=5, pady=2)

        searchToolButton = tk.Label(searchToolFrame, text=strings.menuSearchTool, bg=colors.menuBgColor,
                                    fg=colors.fgColor, font=fonts.menuButtonFont)
        searchToolButton.pack(side="top", padx=5, pady=5)

        searchToolFrame.bind("<Button-1>", lambda event: self.show_frame(strings.searchToolClass))
        search.bind("<Button-1>", lambda event: self.show_frame(strings.searchToolClass))
        searchToolButton.bind("<Button-1>", lambda event: self.show_frame(strings.searchToolClass))

        logOutButton = tk.Label(self.menuFrame, text=strings.menuLogOut, bg=colors.menuBgColor, fg=colors.fgColor,
                                font=fonts.menuLogOutFont)
        logOutButton.bind("<Button-1>", lambda event: self.show_frame(strings.loginClass))
        logOutButton.pack(side="bottom", padx=5, pady=10)

        # adding menu buttons to the list for easier highlighting
        self.buttonList = (myProfileButton, searchToolButton)
        self.labelList = (tool, search)
        self.frameList = (myProfileFrame, searchToolFrame)

        # disabling menu frame in order to populate login/register pages
        self.menuFrame.pack_forget()

        # setting up external classes
        self.frames = {}

        for F in (SearchToolPage, WelcomePage, MyToolPage, BookToolPage, LoginPage,
                  RegisterPage, ToolInfoPage, MyProfilePage):
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
        self.geometry("{}x{}+%d+%d".format(int(self.winfo_screenwidth()*0.8), int(self.winfo_screenheight()*0.8)) %
                                          ((self.winfo_screenwidth() / 2) - int(self.winfo_screenwidth()*0.4), (self.winfo_screenheight() / 2) - int(self.winfo_screenheight()*0.4)))
        self.minsize(dimens.mainWindowWidth, dimens.mainWindowHeigh)
        self.maxsize(self.winfo_screenwidth(), self.winfo_screenheight())
        self.resizable(True, True)

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

        if self.page_name is strings.myProfileClass:
            self.highlightButton(0)
        elif self.page_name is strings.searchToolClass or self.page_name is strings.toolInfoPage \
                or self.page_name is strings.bookToolClass:
            self.highlightButton(1)
        else:
            self.highlightButton(-1)

        """
        if self.__page_name is strings.myToolClass:
            self.highlightButton(0)
        elif self.__page_name is strings.returnToolClass:
            self.highlightButton(1)
        elif self.__page_name is strings.addToolClass:
            self.highlightButton(2)
        elif self.__page_name is strings.searchToolClass:
            self.highlightButton(3)
        elif self.__page_name is strings.invoiceClass:
            self.highlightButton(4)
        """

    def highlightButton(self, index):
        """
        This function changes colors for all menu items based on the index
        :param index: int(buttonList index)
        :return: None
        """
        if index < 0:
            for i in range(len(self.buttonList)):
                self.buttonList[i].config(bg=colors.menuBgColor)
                self.labelList[i].config(bg=colors.menuBgColor)
                self.frameList[i].config(bg=colors.menuBgColor)
        else:
            # looping through buttonList and looking for match.
            for i in range(len(self.buttonList)):
                if index == i:
                    self.buttonList[i].config(bg=colors.bgColor)
                    self.labelList[i].config(bg=colors.bgColor)
                    self.frameList[i].config(bg=colors.bgColor)
                else:
                    self.labelList[i].config(bg=colors.menuBgColor)
                    self.frameList[i].config(bg=colors.menuBgColor)
                    self.buttonList[i].config(bg=colors.menuBgColor)


if __name__ == "__main__":
    app = mainMenu()
    app.mainloop()
