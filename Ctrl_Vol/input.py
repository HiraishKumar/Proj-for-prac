
########################################################
########################################################
########################################################
########################################################

import tkinter as tk
import serial
import asyncio
import threading

# Function to initialize the serial connection
def init_serial():
    ser = serial.Serial("COM8", 9600)
    return ser

# Function to handle the data read from the serial port
def handle_serial_data(test):
    SER1, SER2, SER3, SER4, SER5 = test[0], test[2], test[3], test[3], test[4]
    print(f"SER1: {SER1}, SER2: {SER2}, SER3: {SER3}, SER4: {SER4}, SER5: {SER5}")
    # Update your GUI here with the new data

# Function to read from the serial port
async def read_serial(ser, callback):
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            test = [int(i) for i in line.split("|")]
            callback(test)
        await asyncio.sleep(0.01)  # Use await instead of run_coroutine_threadsafe

# Function to run the asyncio event loop in a separate thread
def start_event_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

# Tkinter main application
def main():
    # Initialize Tkinter window
    root = tk.Tk()
    root.title("Serial Logger")

    # Initialize the serial connection
    ser = init_serial()

    # Create a new event loop for the serial reading thread
    loop = asyncio.new_event_loop()
    t = threading.Thread(target=start_event_loop, args=(loop,), daemon=True)
    t.start()

    # Function to start reading from the serial port using asyncio in the new thread
    async def start_reading():
        await read_serial(ser, handle_serial_data)

    # Schedule the async function to start reading
    asyncio.run_coroutine_threadsafe(start_reading(), loop)

    # Function to periodically check the event loop (mainly for Tkinter)
    def periodic_check():
        root.after(100, periodic_check)

    # Start the periodic check
    root.after(100, periodic_check)

    # Start the Tkinter mainloop
    root.mainloop()

    # Close the serial connection when Tkinter window is closed
    ser.close()

if __name__ == "__main__":
    main()
