from tkinter import *
from tkinter import ttk
import serial
import serial.tools.list_ports
import threading
from input import AudioController

process_name = "firefox.exe" 
audio_controller = AudioController(process_name)

current_volume = audio_controller.process_volume()
print(f"Current volume for {process_name}: {current_volume}")

def find_port():
    # Get a list of all available serial ports.
    ports = serial.tools.list_ports.comports()

    # print("The following serial ports were found:")
    for port in ports:
        if port.description.find("CH340") != -1 or port.description.find("Arduino") != -1:
            # print(f"Device: {port.device}, Description: {port.description}")
            print(f"the port connected to {port.device}")
            return port.device

def readSerial():
    print("Started Logging")
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            test = [int(i)//10 if 0 <= int(i) < 1000 else 100 for i in line.split("|")]
            # print(test)
            new_volume = float(test[0]/100 )
            audio_controller.set_volume(new_volume)
            print(f"New volume for {process_name} set to {new_volume}")
            for num,item in enumerate(serials):
                item.set(test[num])
            
            for num,item in enumerate(sliders):
                item.set(value=test[num])

def startReading():
    thread =threading.Thread(target=readSerial)
    thread.daemon=True
    thread.start()
               
root = Tk()
root.title("Serial Reader")
root.geometry("500x500")

mainframe = ttk.Frame(root,padding=("3 3 12 12"))
mainframe.grid(row=1,column=1,sticky="nsew")

root.columnconfigure(1,weight=1)
root.rowconfigure(1,weight=1)

serials =[]
sliders = []
for i in range(5):
    serial_val = IntVar()
    serials.append(serial_val) 

for i in range(1,6):
    serial_ = ttk.Entry(mainframe,textvariable=serials[i-1],state=DISABLED,width=5)
    serial_.grid(row=2, column=i,pady=10, sticky="")
    
    slider = Scale(mainframe, from_=0, to=100, orient=VERTICAL, length=300)
    slider.grid(row=3, column=i)
    sliders.append(slider)
    
    mainframe.columnconfigure(i, weight=1)
    
    ttk.Label(mainframe, text=(f"SER{i}")).grid(row=1, column=i,pady=10, sticky="")
    
for child in mainframe.winfo_children():
    child.grid_configure(padx=20)

ser = serial.Serial(find_port(),9600)

startReading()

root.mainloop()


