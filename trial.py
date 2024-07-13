import serial
import random
import time
from datetime import datetime


# set baud rate, same speed as set in your Arduino sketch.
baud_rate = 9600

# set serial port as suits your operating system
s = serial.Serial('COM5', baud_rate, timeout=5)

while True:  # infinite loop, keep running

    #  a random number between 5 and 50.
    data_send = random.randint(5, 50)

    # write to serial port, set data encoding. 
    # Raw bytes are sent through serial ports, Python bytes() needs 
    # to know the encoding to generate bytes from string.
    # We send a single integer which is read from Arduino sketch.
    d = s.write(bytes(str(data_send), 'utf-8'))
    #current time year, month, data, hour, minute, second
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(f"{timestamp} Send >>> {data_send} ({d} bytes)")
    print(f"Completing {data_send} blinks...")
    #This for loop sleeps for 1 second for each value in data_send
    #so if data send is 5 it will sleep 5 seconds
    for i in range(data_send):
        time.sleep(1)
    #Setting a new time stamp, ensuring that the correct time is printed
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(f"{timestamp} Done blinking")
    #this takes the random number generated from ardunio and strips it
    #reading the serial port until it reads the number from ardunio
    j = s.readline().decode("utf-8").strip()
    #This then converts j to an integer and then prints it with the current time stamp
    tm = int(j)
    print(f"\nReceived <<< {j}")
    #Again creating a new timestamp so the correct time is shown
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(f"{timestamp} sleeping for {j} seconds")
    time.sleep(tm)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(f"{timestamp} Done sleeping\n")

    

    
