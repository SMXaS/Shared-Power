from tkinter import *



root = Tk()

#root.geometry('700x500')

#root.resizable(0,0)

root.title('Login')

usernameLabel = Label(text = "UserName")
passwordLabel = Label(text = "Password")
usernameEntry = Entry()
passwordEntry = Entry(show = "*")

usernameLabel.grid(row = 0, column = 0, sticky=E)
passwordLabel.grid(row = 1, column = 0, sticky=E)
usernameEntry.grid(row = 0, column = 1)
passwordEntry.grid(row = 1, column = 1)





root.mainloop()
