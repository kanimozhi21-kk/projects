import tkinter
var=tkinter.Tk()
var.mainloop()

from tkinter import*
root=Tk()
root.geometry("300x300")
frame=Frame(root,bg="green",height=70,width=300)
frame.pack()
root.mainloop()

from tkinter import*
root=Tk()
frame=Frame(root,bg="blue",height=700,width=700)
frame.pack()
root.mainloop()

import tkinter
from tkinter import messagebox
def content():
    messagebox.showwaring("helo python","hello pyton")
value=tkinter.Tk()
b=tkinter.Button(value,text="new",command=content)
b.pack()
value.mainloop()

import tkinter
t=tkinter.Tk()
frame=tkinter.Frame(t,bg="blue",width=450,height=450)
b=tkinter.Button(t,text="hello",activebackground="green")
frame.pack()
b.pack()
t.mainloop()

from tkinter import*
root=Tk()
for fm in['orange','green','grey','black','white','yellow','pink','brown','violet','purple']:
    Frame(height=20,width=640,bg=fm).pack()
root.mainloop()
          
