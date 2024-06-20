import serial
import time

ser = serial.Serial('COM8',9600)
time.sleep(2)

try:
    print("Started Logging")
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(line)
except KeyboardInterrupt:
    print("Logging Stopped")
finally:
    ser.close()
    
