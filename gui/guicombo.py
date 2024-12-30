from tkinter import*
from tkinter import ttk
root=Tk()
root.title("combobox example")
root.geometry('300x300')
combo=ttk.Combobox(root,values=["optiona1","optiona2","optiona3","optiona4","optiona5"])
combo.pack()
'''def option_selected(event):
    selected_option=combo.get()
    print("you selected:",selected_option)
combo.bind("<<combobox selected>>",option_selected)'''
root.mainloop()
