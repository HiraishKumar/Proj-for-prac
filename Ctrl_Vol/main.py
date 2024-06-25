
from tkinter import *
from tkinter import ttk

import serial
import time


root = Tk()
root.title("Serial Reader")
root.geometry("500x500")


mainframe = ttk.Frame(root,padding=("3 3 12 12"))
mainframe.grid(row=1,column=1,sticky="nsew")

root.columnconfigure(1,weight=1)
root.rowconfigure(1,weight=1)
for i in range(1, 6):
    mainframe.columnconfigure(i, weight=1)

# Create labels in the first row
ttk.Label(mainframe, text="SER1").grid(row=1, column=1,pady=10, sticky="")
ttk.Label(mainframe, text="SER2").grid(row=1, column=2,pady=10, sticky="")
ttk.Label(mainframe, text="SER3").grid(row=1, column=3,pady=10, sticky="")
ttk.Label(mainframe, text="SER4").grid(row=1, column=4,pady=10, sticky="")
ttk.Label(mainframe, text="SER5").grid(row=1, column=5,pady=10, sticky="")

# Create labels in the second row
serial1 = IntVar()
SER1 = ttk.Entry(mainframe,textvariable=serial1,state=DISABLED,width=5)
SER1.grid(row=2, column=1,pady=10, sticky="")
serial2 = IntVar()
SER2 = ttk.Entry(mainframe,textvariable=serial2,state=DISABLED,width=5)
SER2.grid(row=2, column=2,pady=10, sticky="")
serial3 = IntVar()
SER3 = ttk.Entry(mainframe,textvariable=serial3,state=DISABLED,width=5)
SER3.grid(row=2, column=3,pady=10, sticky="")
serial4 = IntVar()
SER4 = ttk.Entry(mainframe,textvariable=serial4,state=DISABLED,width=5)
SER4.grid(row=2, column=4,pady=10, sticky="")
serial5 = IntVar()
SER5 = ttk.Entry(mainframe,textvariable=serial5,state=DISABLED,width=5)
SER5.grid(row=2, column=5,pady=10, sticky="")

button = ttk.Button(mainframe,text= "Get Value")
button.grid(row=3,column=5,pady=20)

for child in mainframe.winfo_children():
    child.grid_configure(padx=20)

# print(serial2.get())
########################################################
########################################################
########################################################
########################################################

    
ser = serial.Serial("COM8",9600)
time.sleep(2)
try:
    print("Started Logging")
    test =[0,0,0,0,0]
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            test =[int (i) for i in line.split("|")]
            print(test)
            SER1=test[0]
            SER2=test[2]
            SER3=test[3]
            SER4=test[3]
            SER5=test[4]
            # print("\n".join([f"serial {i+1} is {j}" for i,j in enumerate(test)]))
except KeyboardInterrupt:
    print("Logging Stopped")
finally:
    ser.close()


root.mainloop()