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

mainframe = ttk.Frame(root,padding="10 10 10 10")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))

root.columnconfigure(0,weight=2)
root.rowconfigure(0,weight=2)

feet=StringVar()
feet_entry = ttk.Entry(mainframe,width=7,textvariable=feet)
feet_entry.grid(column=2,row=1,sticky=(W,E))
ttk.Label(mainframe,text="Feet").grid(column=3,row=1,sticky=W)


meter = StringVar()
ttk.Label(mainframe,text="is Equivalent to ").grid(column=1,row=2,sticky=E)
meter_entry = ttk.Entry(mainframe,textvariable=meter)
meter_entry.grid(column=2,row=2,sticky=(W,E))
ttk.Label(mainframe,text="Meter").grid(column=3,row=2,sticky=W)


ttk.Button(mainframe,text="calculate",command=Calculate).grid(row=3,column=3,sticky=(W,E))

feet_entry.focus()
root.bind("<Return>",Calculate)

root.mainloop()