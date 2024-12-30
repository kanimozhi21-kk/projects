from tkinter import*
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import ttk
username="admin"
password="admin"
def login():
    user=usernam_entry.get()
    passw=password_entry.get()
    
    if user==username and passw==password:
       staff()
    else:
        messagebox.showerror("failed","fill the all values OR wrong values")
def staff():
    login_frame.pack_forget()
    staff_frame.pack(fill="both",expand=True)
root=Tk()
root.title("STUDENT MANAGEMENT SYSTEM")
root.geometry("400x400")
login_frame=Frame(root)
login_frame.pack(fill="both",expand=True)

imga=Image.open("school1.jpg")
imga=imga.resize((1500,350))
phot=ImageTk.PhotoImage(imga)
Label(login_frame,image=phot).place(relx=0.00,rely=0.00)

font_but2=font.Font(weight="bold",family="Trebuchet MS",size=15)
x=Label(text="K2 Matriculation Higher Secondary School",font=font_but2)
x.config(bg="black",fg="white")
x.place(relx=0.36,rely=0.43)

font_11=font.Font(weight="bold",family="Trebuchet MS",size=10)
Label(login_frame,text="USER ID:",bg="black",fg="white",font=font_11).place(relx=0.36,rely=0.60)
usernam_entry=Entry(login_frame,width=20,font='arial 15')
usernam_entry.place(relx=0.46,rely=0.60)
    
font_12=font.Font(weight="bold",family="Trebuchet MS",size=10)
Label(login_frame,text="PASSWORD:",bg="black",fg="white",font=font_12).place(relx=0.36,rely=0.70)
password_entry=Entry(login_frame,width=20,font='arial 15')
password_entry.place(relx=0.46,rely=0.70)

font_but=font.Font(weight="bold",family="Trebuchet MS",size=10)       
login_button=Button(login_frame,text="LOGIN",bg='black',fg="white",activebackground="rosybrown2",command=login,font=font_but)
login_button.place(relx=0.5,rely=0.80)
frame=Frame(login_frame,width=1500,height=25,bg='orange').place(relx=.00,rely=.48)
frame=Frame(login_frame,width=20,height=1500,bg='black').place(relx=.0,rely=.0)
frame=Frame(login_frame,width=20,height=1500,bg='black').place(relx=.99,rely=.0)
frame=Frame(login_frame,width=1500,height=20,bg='black').place(relx=.00,rely=.0)
frame=Frame(login_frame,width=1500,height=20,bg='black').place(relx=.98,rely=.0)



staff_frame=Frame(root)


root.mainloop()
