from tkinter import *
from tkinter import ttk

def Calculate(*args) -> None:
    try:
        value = float(feet.get())
        meter.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except:
        pass


root = Tk()
root.title('Feet to meters')
root.geometry('330x110')
root.resizable(False, False)

mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0,row=0)

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

feet=StringVar()
feet_entry = ttk.Entry(mainframe,textvariable=feet)
feet_entry.grid(column=2,row=1)
ttk.Label(mainframe,text="Feet",).grid(column=3,row=1,sticky=W)


meter = StringVar()
ttk.Label(mainframe,text="is Equivalent to ").grid(column=1,row=2)
meter_entry = ttk.Entry(mainframe,textvariable=meter,state=DISABLED)
meter_entry.grid(column=2,row=2)
ttk.Label(mainframe,text="Meter").grid(column=3,row=2,sticky=W)


ttk.Button(mainframe,text="calculate",command=Calculate).grid(row=3,column=3,sticky=(N,W,E,S))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>",Calculate)

root.mainloop()

