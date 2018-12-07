from tkinter import *



root = Tk()

root.geometry('700x500')

root.resizable(0,0)

root.title('Register')



usernameLabel = Label(root, text = "Username")



passwordLabel = Label(root, text = "Password")


confirmPasswordLabel = Label(root, text = "Password Confirmation")

emailLabel = Label(root, text = "Email address")

confirmEmailLabel = Label(root, text = "Email address Confirmation")


usernameEntry = Entry(root)

emailEntry = Entry(root)

confirmEmailEntry = Entry(root)



passwordEntry = Entry(root, show = '*')

confirmPasswordEntry = Entry(root, show = '*')



loginButton = Button(root, text="Login")



registerButton = Button(root, text='Register')





usernameLabel.place(x=250, y=100)

passwordLabel.place(x=253, y=120)

confirmPasswordLabel.place(x=180, y=140)

usernameEntry.place(x=315, y=100)

passwordEntry.place(x=315, y=120)

confirmPasswordEntry.place(x=315, y=140)

emailLabel.place(x=231, y=160)

emailEntry.place(x=315, y=160)

confirmEmailLabel.place(x=158, y=180)

confirmEmailEntry.place(x=315, y=180)

registerButton.place(x=386, y=210)





root.mainloop()
