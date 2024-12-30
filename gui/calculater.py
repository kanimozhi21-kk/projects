from tkinter import tk
r=Tk()
r.geometry("400x400")
var="tiger"
A=0
operator="*"
def click(cul):
    global expression
    expression=expression+str(cul)
    input_text.set(expression)

def eq():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""

expression=""
input_text=StringVar()
def res():  
    global A  
    global operator  
    global var  
    var2 = var  
    if operator == "+":  
        a = float((var2.split("+")[1]))  
        x = A + a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "-":  
        a = float((var2.split("-")[1]))  
        x = A - a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "*":  
        a = float((var2.split("*")[1]))  
        x = A * a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "/":  
        a = float((var2.split("/")[1]))  
    else:  
        x = float(A/a)
        the_data.set(x)  
        var = str(x)  
  
inpu=Entry(r,text=the_data,width=35 )
inpu.place(relx=0.35,rely=0.25)

b1=Button(r,text="1",command=lambda:click(1))
b1.place(relx=0.35,rely=0.30)
b2=Button(r,text="2",command=lambda:click(2))
b2.place(relx=0.40,rely=0.30)
b3=Button(r,text="3",command=lambda:click(3))
b3.place(relx=0.45,rely=0.30)
b4=Button(r,text="4",command=lambda:click(4))
b4.place(relx=0.35,rely=0.35)
b5=Button(r,text="5",command=lambda:click(5))
b5.place(relx=0.40,rely=0.35)
b6=Button(r,text="6",command=lambda:click(6))
b6.place(relx=0.45,rely=0.35)
b7=Button(r,text="7",command=lambda:click(7))
b7.place(relx=0.35,rely=0.40)
b8=Button(r,text="8",command=lambda:click(8))
b8.place(relx=0.40,rely=0.40)
b9=Button(r,text="9",command=lambda:click(9))
b9.place(relx=0.45,rely=0.40)
b0=Button(r,text="0",command=lambda:click(0))
b0.place(relx=0.40,rely=0.45)
bp=Button(r,text="+",command=lambda:click("+"))
bp.place(relx=0.50,rely=0.30)
bs=Button(r,text="-",command=lambda:click("-"))
bs.place(relx=0.50,rely=0.35)
bm=Button(r,text="*",command=lambda:click("*"))
bm.place(relx=0.50,rely=0.40)
bd=Button(r,text="/",command=lambda:click("/"))
bd.place(relx=0.45,rely=0.45)
be=Button(r,text="=",command=lambda:eq())
be.place(relx=0.50,rely=0.45)

r.mainloop()

'''import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.entry = tk.Entry(master, width=30, justify='right', font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("0", 4, 1)
        self.create_button(".", 4, 2)

        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)

        self.create_button("=", 4, 0)
        self.create_button("C", 5, 0)
        self.create_button("CE", 5, 1)
        self.create_button("(", 5, 2)
        self.create_button(")", 5, 3)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16), command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif text == "C":
            self.entry.delete(0, tk.End)
        elif text == "CE":
            self.entry.delete(len(self.entry.get())-1, tk.END)
        else:
            self.entry.insert(tk.END, text)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()'''



