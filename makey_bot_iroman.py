from gpiozero import LED
from gpiozero import PWMLED
import random
import time

red_led = LED(3)
yellow_led = LED(15)
green_led = LED(27)
red_left_light = PWMLED(25)
green_left_light = PWMLED(8)
blue_left_light = PWMLED(7)
red_right_light = PWMLED(5)
green_right_light = PWMLED(6)
blue_right_light = PWMLED(13)

def get_colors():
    stop_colors_dict = {'red' : 'off', 'yellow' : 'off', 'green' : 'off'}
    eye_colors_L_dict = {'red_left' : 0, 'green_left' : 0, 'blue_left' : 0}
    eye_colors_R_dict = {'red_right' : 0, 'green_right' : 0, 'blue_right' : 0}
    colors_list = [stop_colors_dict, eye_colors_L_dict, eye_colors_R_dict]
    return colors_list

def stop_light(_stop_colors_dict):
    for key in _stop_colors_dict:
        led_str = key + '_led.' + _stop_colors_dict[key] + '()'
        exec(led_str)

def eyes_RGB(eyes):
    for i in eyes:
        for key in i:
            eye_str = key + '_light.value = ' + str(i[key])
            exec(eye_str)            

def stop_dict_change(_stop_colors_dict, _user_color):
    if(_user_color in _stop_colors_dict):
        for key in _stop_colors_dict:
            _stop_colors_dict[key] = 'off'
        _stop_colors_dict[_user_color] = 'on'
    else:
        print("skipping")
    return _stop_colors_dict

#def eyes_dict_change():
    

def main():
    colors_list = get_colors()
    while True:
        print("Input traffic light color 'red' 'yellow' or 'green'")
        user_color = input(">>> ")
        stop_colors_dict_ = stop_dict_change(colors_list[0], user_color)
        for i in colors_list[1:]:
            print("Input hex code for eye")
            user_eye = input(">>> ")
            if(user_eye):
                user_eye = user_eye.upper() + "A"
                count = 0
                for e in i:
                    try:
                        i[e] = user_eye[-7+count:-5+count]
                        i[e] = int(i[e], 16)
                    except:
                        print("skipping, invalid digit")
                    else:
                        i[e] = i[e] / 255
                        count += 2
                        if("red" in e):
                            i[e] = i[e] / 2
        print(colors_list)
        stop_light(stop_colors_dict_)
        eyes_RGB(colors_list[1:])
        
        

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
# Updated: 03/21/25
