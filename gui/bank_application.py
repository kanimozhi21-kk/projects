import tkinter as tk
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog

def home():
    root=tk.Tk()
    root.title("bank")
    root.geometry("400x400")
    root.configure(bg="darkolivegreen4")

    label_wel=tk.Label(root,text="KANI  BANK",fg="lime",font=("times new roman",40))
    frame=tk.Frame(root,bg="yellow",height=20,width=1600).pack()
    frame1=tk.Frame(root,bg="yellow",height=20,width=12).place(anchor='w',relx=0.1,rely=0.)
    label_wel.configure(bg="darkolivegreen4")
    label_wel.pack(pady=20)

    f=font.Font(weight="bold",family="times new roman",size=20)
    t="""A bank is a financial institution that accepts deposits from the public
    and creates a demand deposit while simultaneously making loans.
    Lending activities can be directly performed by the bank or indirectly through capital markets."""
    tk.Label(root,text=t,font=f).place(relx=.13,rely=.3)

    
    font_but=font.Font(weight="bold",family="Trebuchet MS",size=15)
    font_but2=font.Font(weight="bold",family="Trebuchet MS",size=15)
    font_but3=font.Font(weight="bold",family="Trebuchet MS",size=15)
       
    login_but=tk.Button(root,text="CUSTOMER LOGIN",command=login,font=font_but)
    login_but.configure(bg="darksalmon",activebackground="rosybrown2")
    login_but.place(relx=0.1,rely=0.60)
    reg_but=tk.Button(root,text="CUSTOMER REGISTER",command=register,font=font_but)
    reg_but.configure(bg="darksalmon",activebackground="rosybrown2")
    reg_but.place(relx=0.42,rely=0.60)
    admin_but=tk.Button(root,text="ADMIN LOGIN",command=admin,font=font_but)
    admin_but.configure(bg="darksalmon",activebackground="rosybrown2")                  
    admin_but.place(relx=0.75,rely=0.60)
    
    frame=tk.Frame(root,width=1500,height=50,bg="yellow").place(relx=.0,rely=.94)
    f=font.Font(root,weight="bold",family="times new roman",size=15)
    x=tk.Label(frame,text=" © CopyRight 2024 KANI",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=0.94)

    frame=tk.Frame(root,width=20,height=1500,bg='yellow').place(relx=.0,rely=.0)
    frame=tk.Frame(root,width=20,height=1500,bg='yellow').place(relx=.99,rely=.0)
    

    root.mainloop()
    
def login():
    def open_file():
        pass
    par1=tk.Tk()
    par1.title("customer Login")
    par1.geometry("600x600")
    par1.configure(bg="cyan4")

    frame1=tk.Frame(par1,bg="yellow",height=20,width=1900).place(anchor='w',relx=.0,rely=0.)
    label_wel=tk.Label(par1,text="KANI  BANK",fg="lime",font=("times new roman",20))
    label_wel.configure(bg="darkolivegreen4")
    label_wel.pack(pady=20)

    font_11=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(par1,text="USER ID:",bg="cyan4",font=font_11).place(relx=0.1,rely=0.15)
    entry_username=tk.Entry(par1,width=20,font='arial 18')
    entry_username.place(relx=0.3,rely=0.15)
    
    font_12=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(par1,text="PASSWORD:",bg="cyan4",font=font_12).place(relx=0.1,rely=0.30)
    entry_password=tk.Entry(par1,width=20,font='arial 18')
    entry_password.place(relx=0.3,rely=0.30)

    def log():
        user=entry_username.get()
        passw=entry_password.get()
        with open("Customer_login.txt","a")as file:
            file.write(f"UserId:{user}\n")
            file.write(f"Password:{passw}\n")

        if user and passw:
            messagebox.showinfo("login successfully","welcome to our bank")
        else:
            messagebox.showerror("failed","fill the all vales")
    font_but=font.Font(weight="bold",family="Trebuchet MS",size=30)       
    login_button=tk.Button(par1,text="LOGIN",bg="chocolate",activebackground="rosybrown2",command=log,font=font_but)
    login_button.place(relx=0.40,rely=0.45)

    fram=tk.Frame(par1,width=1500,height=50,bg="yellow").place(relx=.0,rely=.94)
    '''f=font.Font(par1,weight="bold",family="times new roman",size=15)
    y=tk.Label(fram,text=" © CopyRight 2024 KANI",font=f)
    #bg="yellow",fg="black")
    y.configure(bg="yellow",fg="black")
    y.place(relx=.40,rely=0.1)'''

    frame=tk.Frame(par1,width=20,height=1500,bg='yellow').place(relx=.0,rely=.0)
    frame=tk.Frame(par1,width=20,height=1500,bg='yellow').place(relx=.99,rely=.0)
    

def register():
    def open_file():
        pass
    par2=tk.Tk()
    par2.title("Admin Login")
    par2.geometry("600x600")
    par2.configure(bg="cyan4")


    font_11=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(par2,text="NAME:",bg="cyan4",font=font_11).place(relx=0.1,rely=0.15)
    entry_name=tk.Entry(par2,width=20,font='arial 18')
    entry_name.place(relx=0.3,rely=0.15)

    font_12=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(par2,text="DOB:",bg="cyan4",font=font_12).place(relx=0.1,rely=0.25)
    entry_dob=tk.Entry(par2,width=20,font='arial 18')
    entry_dob.place(relx=0.3,rely=0.25)

    font_13=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(par2,text="PLACE:",bg="cyan4",font=font_13).place(relx=0.1,rely=0.35)
    entry_place=tk.Entry(par2,width=20,font='arial 18')
    entry_place.place(relx=0.3,rely=0.35)

    font_14=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(par2,text="PHONE_NO:",bg="cyan4",font=font_14).place(relx=0.1,rely=0.45)
    entry_non=tk.Entry(par2,width=20,font='arial 18')
    entry_non.place(relx=0.3,rely=0.45)
 
    def reg():
        name=entry_name.get()
        dob=entry_dob.get()
        place=entry_place.get()
        phone_no=entry_non.get()

        with open("customer_register.txt","a")as file:
            file.write(f"NAME:{name}\n")
            file.write(f"DOB:{dob}\n")
            file.write(f"Phone no:{phone_no}\n")
            file.write(f"PLACE:{place}\n")

        if name and dob and place and phone_no:
            messagebox.showinfo("registration successfully","welcome to our bank")
        else:
            messagebox.showerror("failed","fill the all values")
    font_but2=font.Font(weight="bold",family="Trebuchet MS",size=30)
    register_button=tk.Button(par2,text="REGISTER",bg="chocolate",activebackground="rosybrown2",command=reg,font=font_but2)
    register_button.place(relx=0.40,rely=0.55)

    frame=tk.Frame(par2,width=1500,height=50,bg="yellow").place(relx=.0,rely=.94)
    '''f=font.Font(par2,weight="bold",family="times new roman",size=15)
    x=tk.Label(frame,text=" © CopyRight 2024 KANI",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=0.94)'''

    frame=tk.Frame(par2,width=20,height=1500,bg='yellow').place(relx=.0,rely=.0)
    frame=tk.Frame(par2,width=20,height=1500,bg='yellow').place(relx=.99,rely=.0)


def admin():
    def open_file():
        pass
    par3=tk.Tk()
    par3.title("Admin Login")
    par3.geometry("600x600")
    par3.configure(bg="cyan4")


    font_l1=font.Font(weight="bold",family="Trebuchet MS",size=10)
    tk.Label(par3,text="ADMINID:",bg="cyan4",font=font_l1).place(relx=0.1,rely=0.15)
    entry_user=tk.Entry(par3,width=20,font='arial 18')
    entry_user.place(relx=0.3,rely=0.15)

    font_l2=font.Font(weight="bold",family="Trebuchet MS",size=10)
    tk.Label(par3,text="PASSWORD:",bg="cyan4",font=font_l2).place(relx=0.1,rely=0.30)
    entry_pass=tk.Entry(par3,width=20,font='arial 18')
    entry_pass.place(relx=0.3,rely=0.30)
    def adm():
        adminname=entry_user.get()
        password=entry_pass.get()

        with open("admin_login.txt","a")as file:
            file.write(f"AdminId:{adminname}\n")
            file.write(f"Password:{password}\n")

        if adminname=="admin" and password=="admin":
            messagebox.showinfo("login successfully","welcome to our bank")
        else:
            messagebox.showerror("failed","fill the all values or check both values")
    font_but3=font.Font(weight="bold",family="Trebuchet MS",size=30) 
    admin_button=tk.Button(par3,text="ADMIN",bg="chocolate",activebackground="rosybrown2",command=adm,font=font_but3)
    admin_button.place(relx=0.40,rely=0.45)

    frame=tk.Frame(par3,width=1500,height=50,bg="yellow").place(relx=.0,rely=.94)
    f=font.Font(par3,weight="bold",family="times new roman",size=15)
    x=tk.Label(frame,text=" © CopyRight 2024 KANI",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.30,rely=0.94)

    frame=tk.Frame(par3,width=20,height=1500,bg='yellow').place(relx=.0,rely=.0)
    frame=tk.Frame(par3,width=20,height=1500,bg='yellow').place(relx=.99,rely=.0)

home()






    
