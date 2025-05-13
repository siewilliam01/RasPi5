import time
import serial

data_dict = {}

count = 0

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Open Serial port
while False:
    raw_line = ser.readline().decode("utf-8")
    print(raw_line)
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
        data_dict["altitude"] = lines[9]
        data_dict["alt unit"] = lines[10]
        data_dict["quality"] = lines[6]
        data_dict["satellites"] = lines[7]
        data_dict["HDOP"] = lines[8]
        print("\n", count)
        for i in data_dict:
            print(i, ":", data_dict[i])
