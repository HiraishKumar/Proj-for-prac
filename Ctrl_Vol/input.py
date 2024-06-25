# import serial
# import time

# ser = serial.Serial("COM8",9600)
# time.sleep(2)


# try:
#     print("Started Logging")
#     while True:
#         if ser.in_waiting > 0:
#             line = ser.readline().decode('utf-8').strip()
#             test =[int (i) for i in line.split("|")]
#             print(test)
#             # print("\n".join([f"serial {i+1} is {j}" for i,j in enumerate(test)]))
# except KeyboardInterrupt:
#     print("Logging Stopped")
# finally:
#     ser.close()

from tkinter import *

root = Tk()

def task():
    print("hello")
    root.after(2000, task)  # reschedule event in 2 seconds

root.after(2000, task)
root.mainloop()