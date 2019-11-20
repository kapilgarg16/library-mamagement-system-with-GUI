from tkinter import*
w=Tk()
w.title("LIBRARY RECORD BOOK")
w.config(bg="black")
w.minsize(height=600,width=600)
def display():
    c1=s1.get()
    c2 =s2.get()
    c3 =s3.get()
    c4 =s4.get()
    lb.insert(0,(c1,c2,c3,c4))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
def display2():
    pass
label=Label(w,text="RECORD BOOK",bg="grey",fg="black",font="arial 20 bold")
label.grid(row=0,column=0,columnspan=4,ipadx=5,ipady=10,padx=10,pady=10,sticky="nswe")
t=iter(["NAME","SUBJECT","ISBN NO.","COLLEGE ID"])
for i in range(4):
    label=Label(w,text=next(t),bg="grey",fg="black",font="arial 12 bold")
    label.grid(row=1,column=i,ipadx=5,ipady=10,padx=10,pady=10,sticky="nswe")
s1=StringVar()
e1=Entry(w,textvariable=s1,bg="#123456",fg="white",font="arial 20 bold")
e1.grid(row=2,column=0,padx=10,pady=10,ipadx=5,ipady=5,sticky="nswe")
s2=StringVar()
e2=Entry(w,textvariable=s2,bg="#123456",fg="white",font="arial 20 bold")
e2.grid(row=2,column=1,padx=10,pady=10,ipadx=5,ipady=5,sticky="nswe")
s3=StringVar()
e3=Entry(w,textvariable=s3,bg="#123456",fg="white",font="arial 20 bold")
e3.grid(row=2,column=2,padx=10,pady=10,ipadx=5,ipady=5,sticky="nswe")
s4=StringVar()
e4=Entry(w,textvariable=s4,bg="#123456",fg="white",font="arial 20 bold")
e4.grid(row=2,column=3,padx=10,pady=10,ipadx=5,ipady=5,sticky="nswe")
key=iter(["INSERT","UPDATE","DELETE","SEARCH","FINE"])
c=iter(["black","black","black","black","red"])
for i in range(5):
    b=Button(w,text=next(key),bg=next(c),fg="white",font="arial 10 bold")
    b.grid(row=i,column=4,ipadx=10,ipady=10,padx=10,pady=10,sticky="nswe")


lb=Listbox(w,bg="#999999",font="arial 20 bold")
lb.grid(row=3,column=0,columnspan=4,padx=10,pady=10,ipadx=5,ipady=10,sticky="nswe")
lb.bind("<<ListboxSelect>>",display2)
b=Button(w,text="SUBMIT",bg="black",fg="white",font="arial 10 bold",command=display)
b.grid(row=4,column=0,columnspan=4,ipadx=10,ipady=10,padx=10,pady=10,sticky="nswe")
for i in range(5):
    w.grid_rowconfigure(i,weight=1)
for i in range(4):
    w.grid_columnconfigure(i,weight=1)
w.mainloop()
