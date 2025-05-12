import time
import serial

data_dict = {}

count = 0

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)  # Open Serial port
while True:
    raw_line = ser.readline().decode("utf-8")
    if "GPGGA" in raw_line:
        count += 1
        line = raw_line
        lines = line.split(",")
        data_dict["time"] = lines[1]
        data_dict["latitude"] = lines[2]
        data_dict["N/S"] = lines[3]
        data_dict["longitude"] = lines[4]
        data_dict["E/W"] = lines[5]
        data_dict["quality"] = lines[6]
        data_dict["satellites"] = lines[7]
        print(count)
        for i in data_dict:
            print(i, ":", data_dict[i])
