
# ########################################################
# ########################################################
# ########################################################
# ########################################################

# import tkinter as tk
# import serial
# import asyncio
# import threading

# # Function to initialize the serial connection
# def init_serial():
#     ser = serial.Serial("COM8", 9600)
#     return ser

# # Function to handle the data read from the serial port
# def handle_serial_data(test):
#     SER1, SER2, SER3, SER4, SER5 = test[0], test[2], test[3], test[3], test[4]
#     print(f"SER1: {SER1}, SER2: {SER2}, SER3: {SER3}, SER4: {SER4}, SER5: {SER5}")
#     # Update your GUI here with the new data

# # Function to read from the serial port
# async def read_serial(ser, callback):
#     while True:
#         if ser.in_waiting > 0:
#             line = ser.readline().decode('utf-8').strip()
#             test = [int(i) for i in line.split("|")]
#             callback(test)
#         await asyncio.sleep(0.01)  # Use await instead of run_coroutine_threadsafe

# # Function to run the asyncio event loop in a separate thread
# def start_event_loop(loop):
#     asyncio.set_event_loop(loop)
#     loop.run_forever()

# # Tkinter main application
# def main():
#     # Initialize Tkinter window
#     root = tk.Tk()
#     root.title("Serial Logger")

#     # Initialize the serial connection
#     ser = init_serial()

#     # Create a new event loop for the serial reading thread
#     loop = asyncio.new_event_loop()
#     t = threading.Thread(target=start_event_loop, args=(loop,), daemon=True)
#     t.start()

#     # Function to start reading from the serial port using asyncio in the new thread
#     async def start_reading():
#         await read_serial(ser, handle_serial_data)

#     # Schedule the async function to start reading
#     asyncio.run_coroutine_threadsafe(start_reading(), loop)

#     # Function to periodically check the event loop (mainly for Tkinter)
#     def periodic_check():
#         root.after(100, periodic_check)

#     # Start the periodic check
#     root.after(100, periodic_check)

#     # Start the Tkinter mainloop
#     root.mainloop()

#     # Close the serial connection when Tkinter window is closed
#     ser.close()

# if __name__ == "__main__":
#     main()


# from comtypes import CLSCTX_ALL

# from pycaw.pycaw import AudioUtilities

# class AudioController:
#     def __init__(self, process_name):
#         self.process_name = process_name
#         self.volume = self.process_volume()
#         self.interface = None
    
#     def process_volume(self):
#         sessions = AudioUtilities.GetAllSessions()
#         for session in sessions:
#             interface = session.SimpleAudioVolume
#             if session.Process and session.Process.name() == self.process_name:
#                 print("Volume:", interface.GetMasterVolume())  # debug
#                 return interface.GetMasterVolume()

#     def set_volume(self, decibels):
#         sessions = AudioUtilities.GetAllSessions()
#         if self.interface == None:
#             for session in sessions:
#                 interface = session.SimpleAudioVolume
#                 if session.Process and session.Process.name() == self.process_name:
#                     self.interface = session
#                     # only set volume in the range 0.0 to 1.0
#                     self.volume = min(1.0, max(0.0, decibels))
#                     interface.SetMasterVolume(self.volume, None)
#                     print("Volume set to", self.volume)
#         else:
#             interface = self.interface.SimpleAudioVolume
#             self.volume = min(1.0, max(0.0, decibels))
#             interface.SetMasterVolume(self.volume, None)
#             print("Volume set to", self.volume)
            
            
from pycaw.pycaw import AudioUtilities
import math

class AudioController:
    def __init__(self, process_name):
        self.process_name = process_name
        self.volume = self.process_volume()
        self.interface = None
    
    def process_volume(self):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            interface = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.process_name:
                print("Volume:", interface.GetMasterVolume())  # debug
                return interface.GetMasterVolume()
    
    def set_volume(self, volume_linear):
        sessions = AudioUtilities.GetAllSessions()
        volume_log = self.linear_to_logarithmic(volume_linear)
        
        if self.interface is None:
            for session in sessions:
                interface = session.SimpleAudioVolume
                if session.Process and session.Process.name() == self.process_name:
                    self.interface = session
                    interface.SetMasterVolume(volume_log, None)
                    print("Volume set to", volume_log)
        else:
            interface = self.interface.SimpleAudioVolume
            interface.SetMasterVolume(volume_log, None)
            print("Volume set to", volume_log)

    def linear_to_logarithmic(self, volume_linear):
        # Convert linear volume to logarithmic scale
        # Ensure volume is between 0.0 and 1.0
        volume_linear = min(1.0, max(0.0, volume_linear))
        # Convert linear scale (0.0 to 1.0) to logarithmic scale
        # We use a log base 10 here, but other bases could be used
        return math.log10(volume_linear * 9 + 1) / 1  # maps 0.0-1.0 to 0.0-1.0 logarithmically

if __name__ == "__main__":
    process_name = "firefox.exe"  # Replace with the name of the process you want to control
    audio_controller = AudioController(process_name)
    
    # Get current volume
    current_volume = audio_controller.process_volume()
    print(f"Current volume for {process_name}: {current_volume}")
    
    # Set new volume
    new_volume = float(input("enter new volume:"))  # Set desired volume level (0.0 to 1.0) in linear scale
    audio_controller.set_volume(new_volume)
    print(f"New volume for {process_name} set to {new_volume}")
