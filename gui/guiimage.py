from tkinter import*
from PIL import Image
from PIL.ImageTk import PhotoImage

root=Tk()
root.geometry("500x400")
img=PhotoImage(Image.open("sun.jpg"))
label=Label(root,image=img).pack()
root.mainloop()
