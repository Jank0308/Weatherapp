from tkinter import *
from tkinter import ttk
from retrieve_data import ret_data
root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()
entry = ttk.Entry(width= 20)
entry.grid(column=1,row=0)
def b():
    g = ret_data(entry.get())
    ttk.Label(frm, text=g).grid(column=0, row=1)
ttk.Button(frm, text="Get Data", command=b).grid(column=0, row=0)
root.mainloop()

