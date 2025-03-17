from gpiozero import LED
from gpiozero import PWMLED
import random
import time

red_led = LED(3)
yellow_led = LED(15)
green_led = LED(27)
r_light_L = PWMLED(25)
g_light_L = PWMLED(8)
b_light_L = PWMLED(7)
r_light_R = PWMLED(5)
g_light_R = PWMLED(6)
b_light_R = PWMLED(13)

def stop_light(_stop_colors_dict):
    for key in _stop_colors_dict:
        led_str = key + '_led.' + _stop_colors_dict[key] + '()'
        eval(led_str)

def stop_dict_change(_stop_colors_dict):
    for key in _stop_colors_dict:
        _stop_colors_dict[key] = 'off'
    return _stop_colors_dict

def main():
    stop_colors_dict = {'red' : 'off', 'yellow' : 'off', 'green' : 'off'}
    while True:
        print("Input 'red' 'yellow' or 'green'")
        user_stop_color = input(">>> ")
        if(user_stop_color in stop_colors_dict):
            stop_colors_dict = stop_dict_change(stop_colors_dict)
            stop_colors_dict[user_stop_color] = 'on'
            stop_light(stop_colors_dict)
        else:
            print("not a valid color")

main()

# =============================================================================
# https://github.com/siewilliam01/RasPi5/blob/main/makey_bot_iroman.py
# William Sie
# Name: makey_bot_iroman.py
# Description: Turns on one light only based on user console input
# Dependencies: python 3
# License: GNU General Public License v2.0
# Inputs: console
# Outputs: 3x LEDs
# Created: 03/12/25
# Updated: 03/17/25
