import time
import serial

data_dict = {}

count = 0
check = 0
GPGGA_list = []
GPGSV_list = []
connection_status = False

while True:
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        connection_status = True # Open Serial port
    except:
        try:
            ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
            connection_status = True
        except:
            print("GPS Disconnected")
    finally:
        while connection_status == True:
            try:
                raw_data = ser.readline().decode("utf-8")
            except:
                print("GPS Failed")
                connection_status = False
            else:
                if "GPGGA" in raw_data:
                    GPGGA_line = raw_data
                    GPGGA_list = GPGGA_line.split(",")
                    check += 1
                if "GPGSV" in raw_data:
                    GPGSV_line = raw_data
                    GPGSV_list_temp = GPGSV_line.split(",")
                    if "1" in GPGSV_list_temp[2]:
                        GPGSV_list = GPGSV_list_temp
                        check +=1
                if check >= 2:
                    data_dict["time"] = GPGGA_list[1]
                    data_dict["latitude"] = GPGGA_list[2]
                    data_dict["N/S"] = GPGGA_list[3]
                    data_dict["longitude"] = GPGGA_list[4]
                    data_dict["E/W"] = GPGGA_list[5]
                    data_dict["altitude"] = GPGGA_list[9]
                    data_dict["alt unit"] = GPGGA_list[10]
                    data_dict["quality"] = GPGGA_list[6]
                    data_dict["sats view"] = GPGSV_list[3]
                    data_dict["sats used"] = GPGGA_list[7]
                    data_dict["HDOP"] = GPGGA_list[8]
                    check = 0
                    count += 1
                    print("\n", count)
                    for i in data_dict:
                        print(i, ":", data_dict[i])

