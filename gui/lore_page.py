import tkinter
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import font
from tkinter import filedialog

# username="admin"
# password="admin"
def home():
    par1=Tk()
    par1.title("customer Login")
    par1.geometry("600x600")
    
    frame=Frame(par1,width=100,height=100)
    frame.place(anchor="n",relx=0.5)
    img=ImageTk.PhotoImage(Image.open("pic3.jpg"))
    label=Label(frame,image=img)
    label.pack()

    label_wel=Label(par1,text="Login Page",fg="lime",font=("times new roman",30))
    label_wel.configure(bg="darkolivegreen4")
    label_wel.pack(pady=20)

    font_11=font.Font(weight="bold",family="Trebuchet MS",size=20)
    Label(par1,text="USER ID:",bg="cyan4",font=font_11).place(relx=0.30,rely=0.25)
    entry_username=Entry(par1,width=20,font='arial 18')
    entry_username.place(relx=0.45,rely=0.25)
    
    font_12=font.Font(weight="bold",family="Trebuchet MS",size=20)
    Label(par1,text="PASSWORD:",bg="cyan4",font=font_12).place(relx=0.30,rely=0.40)
    entry_password=Entry(par1,width=20,font='arial 18')
    entry_password.place(relx=0.45,rely=0.40)
    
    font_but=font.Font(weight="bold",family="Trebuchet MS",size=30)       
    login_button=Button(par1,text="LOGIN",bg="chocolate",activebackground="rosybrown2",command=register,font=font_but)
    login_button.place(relx=0.40,rely=0.45)
    
    user=entry_username.get()
    passw=entry_password.get()
    if user=="admin" and passw=="admin":
        register()
        
def register():
    root=Tk()
    root.geometry("600x600")
    root.configure(bg="cyan4")

    frame=Frame(root,width=100,height=100)
    frame.place(anchor="n",relx=0.5)
    #img=ImageTk.PhotoImage(Image.open("pic3.jpg"))
    #label=Label(frame,image=img)
    #label.pack()

    label_wel=Label(root,text="Register",fg="lime",font=("times new roman",40))
    label_wel.configure(bg="darkolivegreen4")
    label_wel.place(anchor="n",relx=0.47,rely=0.13)

    c1=Entry(root,width=20,font='arial 18')
    c1.place(relx=0.2,rely=0.6)
    font_n=font.Font(weight="bold",family="Trebuchet MS",size=20)
    a=Label(root,text="First Name:",font=font_n)
    a.place(relx=0.05,rely=0.5)
    font_d=font.Font(weight="bold",family="Trebuchet MS",size=20)
    b=Label(root,text="DOB:",font=font_d)
    b.place(relx=0.05,rely=0.6)
    font_e=font.Font(weight="bold",family="Trebuchet MS",size=20)
    c=Label(root,text="EMAIL-ID:",font=font_d)
    c.place(relx=0.05,rely=0.7)
    font_e=font.Font(weight="bold",family="Trebuchet MS",size=20)
    d=Label(root,text="Contact:",font=font_e)
    d.place(relx=0.5,rely=0.7)

    a1=Entry(root,width=20,font='arial 18')
    a1.place(relx=0.2,rely=0.5)
    b1=Entry(root,width=20,font='arial 18')
    b1.place(relx=0.2,rely=0.7)
    d1=Entry(root,width=20,font='arial 18')
    d1.place(relx=0.6,rely=0.7)

    font_g=font.Font(weight="bold",family="Trebuchet MS",size=20)
    R=Label(root,text="Gender:",font=font_g)
    R.place(relx=0.5,rely=0.5)
    var=IntVar()
    R1=Radiobutton(root,text="male",variable=var,value=1,font='arial 18')
    R1.place(relx=0.7,rely=0.5)
    R1=Radiobutton(root,text="female",variable=var,value=2,font='arial 18')
    R1.place(relx=0.6,rely=0.5)

    font_p=font.Font(weight="bold",family="Trebuchet MS",size=20)
    combo1=Label(root,text="Place:",font=font_p)
    combo1.place(relx=0.5,rely=0.6)
    p1=Entry(root,width=20,font='arial 18')
    p1.place(relx=0.6,rely=0.6)
    def kani():
        aa1=a1.get()
        bb1=b1.get()
        cc1=c1.get()
        dd1=d1.get()
        pp1=p1.get()
        if aa1 and bb1 and cc1 and dd1 and pp1:
            messagebox.showinfo("registration successfully","welcome")
        else:
            messagebox.showerror("failed","fill the all values")
    font_b=font.Font(weight="bold",family="Trebuchet MS",size=20)
    B1=Button(root,text="Register",command=kani,font=font_b)
    B1.place(relx=0.7,rely=0.8)

home()
 
""" import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Advanced Login Form")
root.geometry("400x250")
root.resizable(False, False)

# Add a logo (optional)
'''logo = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(root, image=logo)
logo_label.grid(row=0, column=1, pady=20)'''

# Username label and entry field
username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=5)

username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=5)

# Password label and entry field
password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Remember Me checkbox
remember_me_var = tk.IntVar()
remember_me_check = tk.Checkbutton(root, text="Remember Me", variable=remember_me_var)
remember_me_check.grid(row=3, column=1)

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Replace with your own validation logic
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", "Welcome Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=4, column=1, pady=20)

# Run the application
root.mainloop() """










   
    
