from tkinter import*
r=Tk()
r.geometry("250x400")
l0=Label(r,text="GROCERY BILL").grid(row=0,column=5)
l1=Label(r,text="PRODUCT 1").grid(row=2,column=1)
l2=Label(r,text="PRODUCT 2").grid(row=3,column=1)
l3=Label(r,text="PRODUCT 3").grid(row=4,column=1)
l4=Label(r,text="PRICE").grid(row=5,column=1)

e1=Entry(r)
e1.grid(row=2,column=2)
e2=Entry(r)
e2.grid(row=3,column=2)
e3=Entry(r)
e3.grid(row=4,column=2)
e4=Entry(r)
e4.grid(row=5,column=2)




def add():
    a=int(e1.get())
    b=int(e2.get())
    c=int(e3.get())
    d=a+b+c
    e4.insert(0,d)
b=Button(r,text="total amount",command=lambda:add())
b.grid(row=5,column=4)
r.mainloop()
'''

from tkinter import*
r=Tk()
r.geometry("400x400")
l0=Label(r,text="GROCERY BILL")
l0.grid(row=0,column=5)
l1=Label(r,text="PRODUCT 1")
l1.grid(row=2,column=1)
l2=Label(r,text="PRODUCT 2")
l2.grid(row=3,column=1)
l3=Label(r,text="PRODUCT 3")
l3.grid(row=4,column=1)
l4=Label(r,text="PRICE")
l4.grid(row=5,column=1)


e1=Entry(r)
e1.grid(row=2,column=2)
e2=Entry(r)
e2.grid(row=3,column=2)
e3=Entry(r)
e3.grid(row=4,column=2)
e4=Entry(r)
e4.grid(row=5,column=2)

def add():
    a=int(e1.get())
    b=int(e2.get())
    c=int(e3.get())
    d=a+b+c
    e4.insert(0,d)

b=Button(r,text="total Amount",command=lambda:add())
b.grid(row=5,column=3)    
    
r.mainloop()
'''      
    
