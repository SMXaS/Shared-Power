import tkinter as Tk                # It was delive in time


def selection(event):
    w = event.widget
    #a= Tk.curserlection()            # Do not mess with my work
    idx = int(w.curselection()[0])    # Sorry, I did..
    value = w.get(idx)
    print(value)
    #for i in a:
     #   print (Tk.get(i))           # Hi eddy is not working

Top = Tk.Tk()
Top.geometry("200x200+%d+%d" % ((Top.winfo_screenwidth()/2)-100, (Top.winfo_screenheight()/2)-50))
Top.minsize('200','200')

listboxA = []
for i in range(20):
    test = "{} {}".format(i, "test")
    listboxA.append(test)


#Create Return tool listbox

Listbox=Tk.Listbox(Top ,selectmode="EXTENDED") #Selectmode by pressing
Listbox.bind('<<ListboxSelect>>', selection)

Listbox.insert(Tk.END)
for i in listboxA:
    Listbox.insert(Tk.END, i)

Listbox.pack()

Top.mainloop()
