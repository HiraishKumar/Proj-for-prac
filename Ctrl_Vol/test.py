import tkinter as tk
from tkinter import ttk
import serial
import threading

class SerialReader:
    def __init__(self, port, baudrate, callback):
        self.port = port
        self.baudrate = baudrate
        self.callback = callback
        self.serial_connection = serial.Serial(self.port, self.baudrate)
        self.running = False

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.read_serial)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def read_serial(self):
        while self.running:
            if self.serial_connection.in_waiting > 0:
                line = self.serial_connection.readline().decode('utf-8').strip()
                if "Analog reading changed: " in line:
                    value = line.split(": ")[1]
                    self.callback(value)

class App:
    def __init__(self, root, serial_reader):
        self.root = root
        self.serial_reader = serial_reader

        self.root.title("Analog Reading Display")

        self.label = ttk.Label(root, text="Waiting for data...", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.start_button = ttk.Button(root, text="Start", command=self.start_serial)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_serial)
        self.stop_button.pack(pady=10)

    def start_serial(self):
        self.serial_reader.start()

    def stop_serial(self):
        self.serial_reader.stop()

    def update_label(self, value):
        self.label.config(text=f"Analog reading: {value}")

if __name__ == "__main__":
    serial_port = "COM8" 
    baud_rate = 9600

    root = tk.Tk()
    app = App(root, SerialReader(serial_port, baud_rate, lambda value: root.after(0, app.update_label, value)))
    root.mainloop()
