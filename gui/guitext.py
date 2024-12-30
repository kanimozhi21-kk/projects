from tkinter import*
from tkinter import Tk
name=Tk()
text=Text(name,height=3,width=40)
text.insert(INSERT,"Hellooo....")
text.insert(END,"Bye Bye....")
text.pack()

b=Button(name,text="submit")
b.pack()
text.tag_add("here","1.0","1.7")
text.tag_add("start","1.8","1.15")
text.tag_config("here",background="blue",foreground="white")
text.tag_config("start",background="red",foreground="black")
name.mainloop()

                
