from tkinter import *

def f1show():
    searchToolFrame.grid()
    welcomeFrame.grid_remove()
def f2show():
    welcomeFrame.grid()
    searchToolFrame.grid_remove()




root = Tk()
root.title('SharedPower')
root.geometry('{}x{}'.format(850, 650))

#Frame Creation

menuFrame = Frame(root, bg='cyan', width=225, height=650,padx=3, pady=3)
searchToolFrame = Frame(root, bg='pink', width=625, height=650,padx=3, pady=3)
welcomeFrame = Frame(root, bg='green', width=625, height=650,padx=3, pady=3)



#Frame Placement

menuFrame.grid(row=0, column=0, sticky="nsw")
searchToolFrame.grid(row=0, column=1, sticky="nse")
searchToolFrame.grid_remove()
welcomeFrame.grid(row=0, column=1, sticky="nse")
#welcomeFrame.grid_remove()

#Welcome Frame Widget Population

welcomeLabel = Label(welcomeFrame,text="Welcome to Shared Power",bg="green",width=87)


#Welcome Frame Widget Placement

welcomeLabel.grid(row=0,column=1)



#Menu Frame Widget Population

profileNameLabel = Label(menuFrame, text="Profile Name", bg='cyan',width=12)
#profilePhoto = PhotoImage(file="profile.png")
#profilePhoto = profilePhoto.subsample(10)
#profilePhotoLabel = Label(menuFrame, image=profilePhoto)
deviderLabel = Label(menuFrame, text = "______________________________",bg="cyan")
MyToolsButton = Button(menuFrame, text = "My Tools",command=f1show)
MyBookingsButton = Button(menuFrame, text = "My Bookings",command=f2show)
invoiceLabel = Label(menuFrame, text = "Invoice",bg='cyan')
logoutLabel = Label(menuFrame, text = "Logout",bg="cyan", height= 58)



#Menu Frame Widget Placement


profileNameLabel.grid(row=0, column=0)
#profilePhotoLabel.grid(row=0, column=1)
deviderLabel.grid(row=1, column = 0, columnspan=2)
MyToolsButton.grid(row=2, column = 0, columnspan=2)
MyBookingsButton.grid(row=3,column = 0, columnspan=2)
invoiceLabel.grid(row=4, column = 0, columnspan=2)
logoutLabel.grid(row=5, column = 0, columnspan=2,sticky="S")

#Display Frame Widget population

sizeHolderLabel = Label(searchToolFrame, text="Profile Name", bg='pink',fg='pink',width=87,height = 5 )
searchBarEntry = Entry(searchToolFrame, width = 70,)
separatorLabel = Label(searchToolFrame, text="Profile Name", bg='pink',fg='pink',width=12,)
toolList = Listbox(searchToolFrame, height = 25, width =70,)
listScrollBar = Scrollbar(searchToolFrame, command = toolList.yview())

#Display Frame Widget Placement

sizeHolderLabel.grid(row=0,column=3)
searchBarEntry.grid(row=1, column=1)
separatorLabel.grid(row=2, column=0)
toolList.grid(row=3,column = 1)
listScrollBar.grid(row = 3, column=2)







root.mainloop()

