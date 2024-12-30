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
        register()
    else:
        messagebox.showerror("failed","fill the all values OR wrong values")
def register():
    login_frame.pack_forget()
    regis_frame.pack(fill="both",expand=True)
def pa():
    name=entry_name.get()
    dob=entry_dob.get()
    place=entry_place.get()
    phone_no=entry_non.get()

    if name and dob and place and phone_no:
        imag()
    else:
        messagebox.showerror("failed","fill the all values")
def imag():
    regis_frame.pack_forget()
    image_page.pack(fill="both",expand=True)
root=Tk()
root.title("HOME PAGE")
root.geometry("400x400")

login_frame=Frame(root)
login_frame.pack(fill="both",expand=True)

frame=Frame(login_frame,width=0,height=0)
frame.place(relx=0.01)
imge=ImageTk.PhotoImage(Image.open("bank7.jpg"))
label=Label(frame,image=imge).pack()

font_but2=font.Font(weight="bold",family="Trebuchet MS",size=30)
x=Label(frame,text="K2 BANK OF INDIA",font=font_but2)
x.config(bg="black",fg="white")
x.place(relx=0.38,rely=0.10)

font_but3=font.Font(weight="bold",family="Trebuchet MS",size=15)
frame1=Frame(root,bg="black",height=30,width=1600).place(rely=0.00)
frame2=Frame(root,bg="black",height=1600,width=45).place(rely=0.00)
mani=Label(root,text="HOME",bg="black",fg="white")
mani1=Label(root,text="CONTACT",bg="black",fg="white")
mani2=Label(root,text="ABOUT",bg="black",fg="white")
mani3=Label(root,text="MENU",bg="black",fg="white")
mani.place(relx=0.01,rely=0.01)
mani1.place(relx=0.05,rely=0.01)
mani2.place(relx=0.10,rely=0.01)
mani3.place(relx=0.15,rely=0.01)

font_11=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(login_frame,text="USER ID:",bg="black",fg="white",font=font_11).place(relx=0.36,rely=0.60)
usernam_entry=Entry(login_frame,width=20,font='arial 18')
usernam_entry.place(relx=0.46,rely=0.60)
    
font_12=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(login_frame,text="PASSWORD:",bg="black",fg="white",font=font_12).place(relx=0.36,rely=0.70)
password_entry=Entry(login_frame,width=20,font='arial 18')
password_entry.place(relx=0.46,rely=0.70)

font_but=font.Font(weight="bold",family="Trebuchet MS",size=15)       
login_button=Button(login_frame,text="LOGIN",bg='black',fg="white",activebackground="rosybrown2",command=login,font=font_but)
login_button.place(relx=0.5,rely=0.80)
    
frame=Frame(login_frame,width=20,height=1500,bg='black').place(relx=.0,rely=.0)
frame=Frame(login_frame,width=30,height=1500,bg='black').place(relx=.98,rely=.0)
    
frame3=Frame(root,bg="black",height=30,width=1600).place(relx=0.00,rely=0.96)

##
regis_frame=Frame(root)

font_but2=font.Font(weight="bold",family="Trebuchet MS",size=20)
x=Label(regis_frame,text="WELCOME",font=font_but2)
x.config(bg="black",fg="white")
x.place(relx=0.43,rely=0.10)

fram=Frame(regis_frame,bg="black",height=40,width=1600).place(rely=0.00)
fram=Frame(regis_frame,bg="black",height=1600,width=20).place(rely=0.00)
fram=Frame(regis_frame,bg="black",height=20,width=1600).place(relx=0.00,rely=0.98)
fram=Frame(regis_frame,bg="black",height=1600,width=20).place(relx=0.99,rely=0.00)

mani=Label(root,text="HOME",bg="black",fg="white")
mani1=Label(root,text="CONTACT",bg="black",fg="white")
mani2=Label(root,text="ABOUT",bg="black",fg="white")
mani3=Label(root,text="MENU",bg="black",fg="white")
mani.place(relx=0.01,rely=0.01)
mani1.place(relx=0.05,rely=0.01)
mani2.place(relx=0.10,rely=0.01)
mani3.place(relx=0.15,rely=0.01)

imga=Image.open("pic.jpg")
imga=imga.resize((200,200))
phot=ImageTk.PhotoImage(imga)
Label(regis_frame,image=phot).place(relx=0.40,rely=0.22)

frame=Frame(regis_frame,width=400,height=280,bg='indianred1')
frame.place(relx=0.32,rely=.50)
    
font_11=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(regis_frame,text="NAME:",bg="black",fg="white",font=font_11).place(relx=0.35,rely=0.55)
entry_name=Entry(regis_frame,width=20,font='arial 12')
entry_name.place(relx=0.45,rely=0.55)

font_12=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(regis_frame,text="DOB:",bg="black",fg="white",font=font_12).place(relx=0.35,rely=0.60)
entry_dob=Entry(regis_frame,width=20,font='arial 12')
entry_dob.place(relx=0.45,rely=0.60)

font_13=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(regis_frame,text='GENDER',bg="black",fg="white",font=font_13).place(relx=0.35,rely=0.65)
combo=ttk.Combobox(regis_frame,values=['MALE','FEMALE'],width=20,font='arial 11').place(relx=0.45,rely=0.65)

font_14=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(regis_frame,text="CONTACT:",bg="black",fg="white",font=font_14).place(relx=0.35,rely=0.70)
entry_non=Entry(regis_frame,width=20,font='arial 12')
entry_non.place(relx=0.45,rely=0.70)

font_e=font.Font(weight="bold",family="Trebuchet MS",size=15)
c=Label(regis_frame,text="EMAIL ID:",bg="black",fg="white",font=font_e)
c.place(relx=0.35,rely=0.75)
entry_no=Entry(regis_frame,width=20,font='arial 12')
entry_no.place(relx=0.45,rely=0.75)

font_13=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(regis_frame,text="ADDRESS:",bg="black",fg="white",font=font_13).place(relx=0.35,rely=0.80)
entry_place=Entry(regis_frame,width=20,font='arial 12')
entry_place.place(relx=0.45,rely=0.80)

font_but2=font.Font(weight="bold",family="Trebuchet MS",size=15)
register_button=Button(regis_frame,text="REGISTER",bg="black",fg="white",command=pa,activebackground="rosybrown2",font=font_but2)
register_button.place(relx=0.45,rely=0.90)

image_page=Frame(root)

fram=Frame(image_page,bg="black",height=30,width=1600).place(rely=0.00)
fram=Frame(image_page,bg="black",height=1600,width=30).place(rely=0.00)
fram=Frame(image_page,bg="black",height=30,width=1600).place(relx=0.00,rely=0.98)
fram=Frame(image_page,bg="black",height=1600,width=30).place(relx=0.99,rely=0.00)

img=Image.open("veri.jpg")
img=img.resize((200,200))
photo=ImageTk.PhotoImage(img)
Label(image_page,image=photo).place(relx=0.42,rely=0.30)
font_but2=font.Font(weight="bold",family="Trebuchet MS",size=15)

t=""" YOUR ACCOUNT IS VERIFIED
    AND YOUR ACCOUNT IS CREATED"""
Label(image_page,text=t,font=font_but2).place(relx=0.37,rely=0.60)

root.mainloop()
