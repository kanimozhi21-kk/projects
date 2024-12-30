from tkinter import *
from tkinter import filedialog
r=Tk()
r.geometry("600x600")
stud=[]
l1=Label(r,text="Enter the Name:")
l1.place(relx=0.1,rely=0.10)
name=Entry(r)
name.place(relx=0.29,rely=0.11)

l2=Label(r,text="Enter the age:")
l2.place(relx=0.1,rely=0.15)
age=Entry(r)
age.place(relx=0.29,rely=0.16)

l3=Label(r,text="Enter a English Mark:")
l3.place(relx=0.1,rely=0.20)
m1=Entry(r)
m1.place(relx=0.29,rely=0.21)

l4=Label(r,text="Enter a Tamil Mark:")
l4.place(relx=0.1,rely=0.25)
m2=Entry(r)
m2.place(relx=0.29,rely=0.26)

l5=Label(r,text="Enter a Science Mark:")
l5.place(relx=0.1,rely=0.30)
m3=Entry(r)
m3.place(relx=0.29,rely=0.31)

l6=Label(r,text="Enter a Maths Mark:")
l6.place(relx=0.1,rely=0.35)
m4=Entry(r)
m4.place(relx=0.29,rely=0.36)

l7=Label(r,text="Enter a Social Mark:")
l7.place(relx=0.1,rely=0.40)
m5=Entry(r)
m5.place(relx=0.29,rely=0.40)

k8=Label(r,text="Total:")
k8.place(relx=0.1,rely=0.45)
k8=Entry(r)
k8.place(relx=0.29,rely=0.45)

k9=Label(r,text="Average:")
k9.place(relx=0.1,rely=0.50)
k9=Entry(r)
k9.place(relx=0.29,rely=0.50)
def add():
    def open_file():
        pass
    name1=(name.get())
    age1=int(age.get())
    a=int(m1.get())
    b=int(m2.get())
    c=int(m3.get())
    d=int(m4.get())
    e=int(m5.get())
    f=a+b+c+d+e
    g=f/5
    stud.append({"Name":name1,"Age":age1,"English":a,"Tamil":b,"Science":c,"Maths":d,"Social":e,"Total":f,"Average":g})
    print(stud)
    with open("Student_mark.txt","a")as file:
        ss=[]
        ss.append({"Name":name1,"Age":age1,"English":a,"Tamil":b,"Science":c,"Maths":d,"Social":e,"Total":f,"Average":g})
        '''file.write(f"Name:{name1}\n")
        file.write(f"Age:{age1}\n")
        file.write(f"English:{a}\n")
        file.write(f"Tamil:{b}\n")
        file.write(f"Maths:{c}\n")
        file.write(f"Science:{d}\n")
        file.write(f"Social:{e}\n")
        file.write(f"Total:{f}\n")
        file.write(f"Average:{g}\n")'''
        file.write(f"records:{ss}")
    k8.delete(0,60)
    k8.insert(0,f)
    k9.insert(0,g)

b=Button(r,text="Result",command=lambda:add())
b.place(relx=0.34,rely=0.55)

r.mainloop()

'''from tkinter import *
r=Tk()
r.geometry("600x600")

l1=Label(r,text="enter the 1st number:")
l1.place(relx=0.1,rely=0.10)
m1=Entry(r)
m1.place(relx=0.32,rely=0.11)

l2=Label(r,text="enter the 2nd number:")
l2.place(relx=0.1,rely=0.15)
m2=Entry(r)
m2.place(relx=0.32,rely=0.16)

l3=Label(r,text="Total:")
l3.place(relx=0.1,rely=0.20)
m3=Entry(r)
m3.place(relx=0.32,rely=0.21)

def add():
    a=int(m1.get())
    b=int(m2.get())
    
    f=a+b

    m3.delete(0,40)
    m3.insert(0,f)

b=Button(r,text="add",command=add)
b.place(relx=0.34,rely=0.26)

def sub():
    a=int(m1.get())
    b=int(m2.get())
    
    f=a-b
    m3.delete(0,40)
    m3.insert(0,f)

b=Button(r,text="sub",command=sub)
b.place(relx=0.28,rely=0.26)

def mul():
    a=int(m1.get())
    b=int(m2.get())
    
    f=a*b

    m3.delete(0,40)
    m3.insert(0,f)

b=Button(r,text="multi",command=mul)
b.place(relx=0.40,rely=0.26)

def div():
    a=int(m1.get())
    b=int(m2.get())
    
    f=a/b

    m3.delete(0,40)
    m3.insert(0,f)

b=Button(r,text="div",command=div)
b.place(relx=0.48,rely=0.26)
r.mainloop()'''

