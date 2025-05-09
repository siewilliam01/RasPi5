#!/usr/bin/env python3
# Original Code: https://gist.github.com/Lauszus/5785023#file-gps-py
# Created by: Kristian Sloth Lauszus

import time
import serial

count = 0

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Open Serial port
while True:
    line = ser.readline().decode("utf-8")
    lines = line.split(",")
    count += 1
    print(count, lines)