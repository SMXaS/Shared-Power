from tkinter import *



root = Tk()

#root.geometry('700x500')

#root.resizable(0,0)

root.title('Register')
firstNameLabel = Label(text = "First Name")
lastNameLabel = Label(text = "Last Name")
userNameLabel = Label(text = "User Name")
postCodeLabel = Label(text = "Post Code")
streetNameLabel = Label(text = "Street Name")
houseNumberLabel = Label(text = "House Number")
emailLabel = Label(text = "Email")
emailConfirmLabel = Label(text = "Email Confirmation")
passwordLabel = Label(text = "Password")
passwordConfirmationLabel = Label(text = "Password Confirmation")

firstNameEntry = Entry()
lastNameEntry = Entry()
userNameEntry = Entry()
postCodeEntry = Entry()
streetNameEntry = Entry()
houseNumberEntry = Entry()
emailEntry = Entry()
emailConfirmEntry = Entry()
passwordEntry = Entry(show = "*")
passwordConfirmationEntry = Entry(show = "*")

createAccountButton = Button (text = "Create Account")

firstNameLabel.grid(row = 0, column = 0, sticky=E)
lastNameLabel.grid(row = 1, column = 0, sticky=E)
userNameLabel.grid(row = 2, column = 0, sticky=E)
postCodeLabel.grid(row = 3, column = 0, sticky=E)
streetNameLabel.grid(row = 4, column = 0, sticky=E)
houseNumberLabel.grid(row = 5, column = 0, sticky=E)
emailLabel.grid(row = 6, column = 0, sticky=E)
emailConfirmLabel.grid(row = 7, column = 0, sticky=E)
passwordLabel.grid(row = 8, column = 0, sticky=E)
passwordConfirmationLabel.grid(row = 9, column = 0, sticky=E)

firstNameEntry.grid(row = 0, column = 1)
lastNameEntry.grid(row = 1, column = 1)
userNameEntry.grid(row = 2, column = 1)
postCodeEntry.grid(row = 3, column = 1)
streetNameEntry.grid(row = 4, column = 1)
houseNumberEntry.grid(row = 5, column = 1)
emailEntry.grid(row = 6, column = 1)
emailConfirmEntry.grid(row = 7, column = 1)
passwordEntry.grid(row = 8, column = 1)
passwordConfirmationEntry.grid(row = 9, column = 1)

createAccountButton.grid(row = 10, column =1)





root.mainloop()
