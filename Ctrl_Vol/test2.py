import tkinter as tk
import serial
import threading

def read_serial():
    """Reads data from the serial port."""
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            label.config(text=data)

def start_reading():
    """Starts the thread for reading serial data."""
    thread = threading.Thread(target=read_serial)
    thread.daemon = True
    thread.start()

# Create the main window
root = tk.Tk()
root.title("Serial Port Data")

# Create a label to display the serial port data
label = tk.Label(root, text="Waiting for data...", font=("Helvetica", 48))
label.pack(pady=20)

# Set up the serial port
ser = serial.Serial('COM8', 9600)

# Start reading from the serial port
start_reading()

# Start the main event loop
root.mainloop()


