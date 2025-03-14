from gpiozero import LED
import time

red_led = LED(3)
yellow_led = LED(15)
green_led = LED(27)

def stop_light(_colors_dict):
    for key in _colors_dict:
        led_str = key + '_led.' + _colors_dict[key] + '()'
        print(led_str)
        eval(led_str)

def dict_change(_colors_dict):
    for key in _colors_dict:
        _colors_dict[key] = 'off'
        print(_colors_dict)
    return _colors_dict

def main():
    colors_dict = {'red' : 'off', 'yellow' : 'off', 'green' : 'off'}
    while True:
        print("Input 'red' 'yellow' or 'green'")
        user_color = input(">>> ")
        if(user_color in colors_dict):
            colors_dict = dict_change(colors_dict)
            colors_dict[user_color] = 'on'
            stop_light(colors_dict)
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
# Updated: 03/14/25
