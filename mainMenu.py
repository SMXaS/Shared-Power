import tkinter as tk
from Code.UI.SearchToolPage import SearchToolPage
from Code.UI.AddToolPage import AddToolPage
from Code.UI.WelcomePage import WelcomePage
from Code.UI.MyToolPage import MyToolPage
from Code.UI.ReturnToolPage import ReturnToolPage
from Code.UI.BookToolPage import BookToolPage
import Resources.Values.values as values


class mainMenu(tk.Tk):

    login = "test"
    page_name = ""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("{}x{}+%d+%d".format(values.mainWindowWidth, values.mainWindowHeigh) %
                      ((self.winfo_screenwidth() / 2) - 350, (self.winfo_screenheight() / 2) - 250))
        self.title(values.appTitle)

        mainFrame = tk.Frame(self)
        mainFrame.pack(side="top", fill="both", expand=True)

        menuFrame = tk.Frame(mainFrame, bg=values.bgColor)
        menuFrame.pack(side="left", fill="y")
        menuBorder = tk.Label(menuFrame, relief=tk.SUNKEN, borderwidth=0, bg=values.fgColor)
        menuBorder.pack(side="right", fill="y")

        container = tk.Frame(mainFrame)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        myToolsButton = tk.Label(menuFrame, text=values.menuMyTools, bg=values.bgColor, fg=values.fgColor)
        myToolsButton.bind("<Button-1>", lambda event: self.show_frame("MyToolPage"))
        myToolsButton.pack(side="top", padx=5, pady=2)

        myBookingsButton = tk.Label(menuFrame, text=values.menuMyBookings, bg=values.bgColor, fg=values.fgColor)
        myBookingsButton.bind("<Button-1>", lambda event: self.show_frame("ReturnToolPage"))
        myBookingsButton.pack(side="top", padx=5, pady=2)

        addToolButton = tk.Label(menuFrame, text=values.menuAddTool, bg=values.bgColor, fg=values.fgColor)
        addToolButton.bind("<Button-1>", lambda event: self.show_frame("AddToolPage"))
        addToolButton.pack(side="top", padx=5, pady=2)

        searchToolButton = tk.Label(menuFrame, text=values.menuSearchTool, bg=values.bgColor, fg=values.fgColor)
        searchToolButton.bind("<Button-1>", lambda event: self.show_frame("SearchToolPage"))
        searchToolButton.pack(side="top", padx=5, pady=2)

        self.frames = {}

        for F in (SearchToolPage, AddToolPage, WelcomePage, MyToolPage, ReturnToolPage, BookToolPage):
            self.page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[self.page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")

    def show_frame(self, page_name, args=[]):
        frame = self.frames[page_name]
        frame.tkraise()
        self.page_name = page_name
        frame.start(args)


if __name__ == "__main__":
    app = mainMenu()
    app.mainloop()
