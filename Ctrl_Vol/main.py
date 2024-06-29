from tkinter import *
from tkinter import ttk
import serial
import threading

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
serial2 = IntVar()
serial3 = IntVar()
serial4 = IntVar()
serial5 = IntVar()

SER1 = ttk.Entry(mainframe,textvariable=serial1,state=DISABLED,width=5)
SER1.grid(row=2, column=1,pady=10, sticky="")

SER2 = ttk.Entry(mainframe,textvariable=serial2,state=DISABLED,width=5)
SER2.grid(row=2, column=2,pady=10, sticky="")

SER3 = ttk.Entry(mainframe,textvariable=serial3,state=DISABLED,width=5)
SER3.grid(row=2, column=3,pady=10, sticky="")

SER4 = ttk.Entry(mainframe,textvariable=serial4,state=DISABLED,width=5)
SER4.grid(row=2, column=4,pady=10, sticky="")

SER5 = ttk.Entry(mainframe,textvariable=serial5,state=DISABLED,width=5)
SER5.grid(row=2, column=5,pady=10, sticky="")

button = ttk.Button(mainframe,text= "Get Value")
button.grid(row=3,column=5,pady=20)

slider1 = Scale(mainframe, from_=0, to=100, orient=VERTICAL, length=300)
slider1.grid(row=4,column=1)

slider2 = Scale(mainframe, from_=0, to=100, orient=VERTICAL, length=300)
slider2.grid(row=4,column=2)

slider3 = Scale(mainframe, from_=0, to=100, orient=VERTICAL, length=300)
slider3.grid(row=4,column=3)

slider4 = Scale(mainframe, from_=0, to=100, orient=VERTICAL, length=300)
slider4.grid(row=4,column=4)

slider5 = Scale(mainframe, from_=0, to=100, orient=VERTICAL, length=300)
slider5.grid(row=4,column=5)

for child in mainframe.winfo_children():
    child.grid_configure(padx=20)

            
def readSerial():
    print("Started Logging")
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            test = [int(i)//10 if 0 <= int(i) < 1000 else 100 for i in line.split("|")]
            print(test)
            serial1.set((test[0]))
            slider1.set(value=test[0])
            
            serial2.set((test[1]))
            slider2.set(value=test[1])
            
            serial3.set((test[2]))
            slider3.set(value=test[2])
            
            serial4.set((test[3]))
            slider4.set(value=test[3])
            
            serial5.set((test[4]))
            slider5.set(value=test[4])
            # print("\n".join([f"serial {i+1} is {j}" for i,j in enumerate(test)]))


def startReading():
    thread =threading.Thread(target=readSerial)
    thread.daemon=True
    thread.start()

ser = serial.Serial("COM8",9600)

startReading()

root.mainloop()


