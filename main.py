from tkinter import *
from tkinter import ttk
from retrieve_data import ret_data
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text=ret_data("Wetter (Ruhr)").grid(column=0, row=0))
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

