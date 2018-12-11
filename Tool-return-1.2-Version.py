import tkinter as Tk                # It was delive in time



def selection():
    a= Tk.curselection()            # Do not mess with my work
    print(a)
    for i in a:
        print (Tk.get(i))           # Hi eddy is not working

Top = Tk.Tk()
Top.geometry("200x200+%d+%d" % ((Top.winfo_screenwidth()/2)-100, (Top.winfo_screenheight()/2)-50))
Top.minsize('200','200')

listboxA=["return tool","mode to return","arrage rider","drop item"]


#Create Return tool listbox

Listbox=Tk.Listbox(Top ,selectmode="EXTENDED") #Selectmode by pressing
b=Tk.Button(Top,text="Press" ,command=selection )

Listbox.insert(Tk.END,)
for i in listboxA:
    Listbox.insert(Tk.END,i)

Listbox.pack()

b.pack()

Top.mainloop()
