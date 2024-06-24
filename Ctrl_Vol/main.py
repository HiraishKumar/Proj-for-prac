import serial
import time
from tkinter import *
from tkinter import ttk

# ser = serial.Serial('COM8',9600)
# time.sleep(2)

# try:
#     print("Started Logging")
#     while True:
#         if ser.in_waiting > 0:
#             line = ser.readline().decode('utf-8').strip()
#             print(line)
# except KeyboardInterrupt:
#     print("Logging Stopped")
# finally:
#     ser.close()

root = Tk()
root.title("Serial Reader")
root.geometry("500x500")


mainframe = ttk.Frame(root,padding=("3 3 12 12"))
mainframe.grid(row=0,column=0)

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)


ttk.Label(mainframe,text="Ser1",background="Grey").grid(row=1,column=1,sticky=(W,E))
ttk.Label(mainframe,text="Ser2",background="Grey").grid(row=1,column=2,sticky=(W,E))
ttk.Label(mainframe,text="Ser3",background="Grey").grid(row=1,column=3,sticky=(W,E))
ttk.Label(mainframe,text="Ser4",background="Grey").grid(row=1,column=4,sticky=(W,E))
ttk.Label(mainframe,text="Ser5",background="Grey").grid(row=1,column=5,sticky=(W,E))


ttk.Label(mainframe,text="ser1").grid(row=2,column=1)
ttk.Label(mainframe,text="ser2").grid(row=2,column=2)
ttk.Label(mainframe,text="ser3").grid(row=2,column=3)                                                           
ttk.Label(mainframe,text="ser4").grid(row=2,column=4)
ttk.Label(mainframe,text="ser5").grid(row=2,column=5)



root.mainloop()