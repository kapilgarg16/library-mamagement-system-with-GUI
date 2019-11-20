from tkinter import*
w=Tk()
w.title("login & Registration")
w.config(bg="#123456")

#FRAME1
f1=Frame(w,bg="black")
f1.pack(side=LEFT,expand=YES,fill=BOTH)
#FRAME2
f2=Frame(w,bg="black")
f2.pack(side=LEFT,expand=YES,fill=BOTH)

#REGISTRATION FORM..

img4=PhotoImage(file="kapil3.png")
panel=Label(f1,image=img4,height=80,width=650)
panel.grid(row=0,column=1,columnspan=2,padx=8,pady=14)

img7=PhotoImage(file="kapilg.png")
panel7=Label(f1,image=img7,height=950,width=120)
panel7.grid(row=0,column=0,rowspan=18,ipady=10,pady=10)

l1=Label(f1,text="REGISTRATION",bg="brown",fg="white",font="arial 20 bold")
l1.grid(row=1,column=1,columnspan=2,ipadx=5,ipady=10,padx=10,pady=10,sticky="nswe")
l2=Label(f1,text="STUDENT_NAME",bg="black",fg="white",font="arial 16 bold")
l2.grid(row=2,column=1,ipadx=5,columnspan=2,ipady=10,padx=10,pady=10,sticky="nswe")
s1=StringVar()
e1=Entry(f1,textvariable=s1,bg="#123456",fg="white",font="arial 16")
e1.grid(row=3,column=1,padx=10,columnspan=2,ipadx=5,ipady=5,sticky="nswe")
l3=Label(f1,text="COLLEGE ID",bg="black",fg="white",font="arial 16 bold")
l3.grid(row=4,column=1,ipadx=5,columnspan=2,ipady=10,padx=10,pady=10,sticky="nswe")
s2=StringVar()
e2=Entry(f1,textvariable=s2,bg="#123456",fg="white",font="arial 16")
e2.grid(row=5,column=1,padx=10,columnspan=2,ipadx=5,ipady=5,sticky="nswe")
l4=Label(f1,text="PASSWORD",bg="black",fg="white",font="arial 16 bold")
l4.grid(row=6,column=1,ipadx=5,columnspan=2,ipady=10,padx=10,pady=10,sticky="nswe")
s3=StringVar()
e3=Entry(f1,textvariable=s3,bg="#123456",fg="white",font="arial 16")
e3.grid(row=7,column=1,padx=10,columnspan=2,ipadx=5,ipady=5,sticky="nswe")
l5=Label(f1,text="Branch",bg="grey",fg="black",font="arial 12 bold")
l5.grid(row=8,column=1,ipadx=5,ipady=10,padx=10,pady=10,sticky="nswe")
t=iter(["CSE","Civil","Mech.","EE","ECE"])
v=IntVar()
l=[]
for i in range(5):
    l.append(Radiobutton(f1,text=next(t),variable=v,value=i,padx=10,bg="black",fg="white",font="arial 10 bold"))
    l[-1].grid(row=9+i,column=1,sticky="nswe")

l6=Label(f1,text="Year",bg="grey",fg="black",font="arial 12 bold")
l6.grid(row=8,column=2,ipadx=5,ipady=10,padx=10,pady=10,sticky="nswe")
t=iter(["1st","2nd","3rd","4th"])
v1=IntVar()
l1=[]
for i in range(4):
    l1.append(Radiobutton(f1,text=next(t),variable=v1,value=i,bg="black",fg="white",font="arial 10 bold"))
    l1[-1].grid(row=9+i,column=2,sticky="nswe")

l5=Label(f1,text="Gender",bg="grey",fg="black",font="arial 12 bold")
l5.grid(row=14,column=1,ipadx=5,ipady=10,padx=10,pady=10,sticky="nswe")
t=iter(["Male","Female"])
v2=IntVar()
l2=[]
for i in range(2):
    l2.append(Radiobutton(f1,text=next(t),variable=v2,value=i,bg="black",fg="white",font="arial 10 bold"))
    l2[-1].grid(row=15+i,column=1,sticky="nswe")
b1 = Button(f1,text="SUBMIT",fg="black",font="arial 10 bold",relief=RAISED,bd=5)
b1.grid(row=17,column=1,columnspan=2,padx=10,pady=10,ipadx=5,ipady=10,sticky="nswe")
for i in range(18):
    f1.grid_rowconfigure(i,weight=1)
for i in range(4):
    f1.grid_columnconfigure(i,weight=1)

img1=PhotoImage(file="kapilg.png")
panel=Label(f1,image=img1,height=1000,width=180)
panel.grid(row=0,column=3,rowspan=18,pady=10)

#login
img6=PhotoImage(file="kapil3.png")
panel5=Label(f2,image=img6,height=80,width=280)
panel5.grid(row=0,column=0,columnspan=3,padx=10)

lf=Label(f2,text="Log-In",bg="brown",fg="white",font="arial 20 bold")
lf.grid(row=1,column=0,columnspan=3,ipadx=10,ipady=10,padx=10,pady=10,sticky="nswe")
lf1=Label(f2,text="Enter Your Name",bg="black",fg="white",font="arial 16 bold")
lf1.grid(row=2,column=0,ipadx=5,columnspan=3,ipady=10,padx=10,pady=10,sticky="nswe")
fs=StringVar()
fe=Entry(f2,textvariable=fs,bg="powder blue",fg="black",font="arial 16")
fe.grid(row=3,column=0,padx=10,columnspan=3,ipadx=5,ipady=5,sticky="nswe")
lf2=Label(f2,text="Password",bg="black",fg="white",font="arial 16 bold")
lf2.grid(row=4,column=0,ipadx=5,columnspan=3,ipady=10,padx=10,pady=10,sticky="nswe")
fs1=StringVar()
fe2=Entry(f2,textvariable=fs1,show="*",bg="powder blue",fg="black",font="arial 16")
fe2.grid(row=5,column=0,padx=10,columnspan=3,ipadx=5,ipady=5,sticky="nswe")
fb = Button(f2,text="SUBMIT",fg="black",font="arial 10 bold",relief=RAISED,bd=5)
fb.grid(row=6,column=0,columnspan=3,padx=10,pady=10,ipadx=5,ipady=10,sticky="nswe")

img2=PhotoImage(file="kapilg.png")
panel=Label(f2,image=img2,height=950,width=160)
panel.grid(row=0,column=3,rowspan=18,pady=10,ipady=10)

#for i in range(7):
 #   f2.grid_rowconfigure(i,weight=1)
#for i in range(4):
 #   f2.grid_columnconfigure(i,weight=1)

w.mainloop()