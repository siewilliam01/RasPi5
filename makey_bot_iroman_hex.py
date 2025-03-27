from gpiozero import LED #import libaries
from gpiozero import PWMLED
from gpiozero import Servo
import random
from time import sleep

red_led = LED(3) #set each led to gpio pins
yellow_led = LED(15)
green_led = LED(27)
red_left_light = PWMLED(25)
green_left_light = PWMLED(8)
blue_left_light = PWMLED(7)
red_right_light = PWMLED(5)
green_right_light = PWMLED(6)
blue_right_light = PWMLED(13)

nod_servo = Servo(26, min_pulse_width=0.0015, max_pulse_width=0.0022) #set servo to gpio pin and servo min and max travel

def run_test(): #test function run through every led and color
    red_led.on()
    sleep(0.2)
    red_led.off()
    yellow_led.on()
    sleep(0.2)
    yellow_led.off()
    green_led.on()
    sleep(0.2)
    green_led.off()
    red_left_light.value = 1
    sleep(0.2)
    red_left_light.value = 0
    green_left_light.value = 1
    sleep(0.2)
    green_left_light.value = 0
    blue_left_light.value = 1
    sleep(0.2)
    blue_left_light.value = 0
    red_right_light.value = 1
    sleep(0.2)
    red_right_light.value = 0
    green_right_light.value = 1
    sleep(0.2)
    green_right_light.value = 0
    blue_right_light.value = 1
    sleep(0.2)
    blue_right_light.value = 0
    nod_servo.min()
    sleep(0.2)
    nod_servo.max()
    sleep(0.2)

def get_colors(): #set dictionaries for LEDs, all off by default
    stop_colors_dict = {'red' : 'off', 'yellow' : 'off', 'green' : 'off'}
    eye_colors_L_dict = {'red_left' : 0, 'green_left' : 0, 'blue_left' : 0}
    eye_colors_R_dict = {'red_right' : 0, 'green_right' : 0, 'blue_right' : 0}
    colors_list = [stop_colors_dict, eye_colors_L_dict, eye_colors_R_dict]
    return colors_list

def stop_light(_stop_colors_dict): #set each of the stoplight LEDs to its on or off dictionary value
    for key in _stop_colors_dict:
        led_str = key + '_led.' + _stop_colors_dict[key] + '()'
        exec(led_str)

def eyes_RGB(eyes): #for each eye for each color, set value based on its dictionary value
    for i in eyes:
        for key in i:
            eye_str = key + '_light.value = ' + str(i[key])
            exec(eye_str)            

def stop_dict_change(_stop_colors_dict, _user_color):
    if(_user_color in _stop_colors_dict): #only runs if the user input is valid 'red' 'yellow' or 'green'
        for key in _stop_colors_dict: #sets all the stop light colors off first in the dictionary
            _stop_colors_dict[key] = 'off'
        _stop_colors_dict[_user_color] = 'on' #set dictionary on for only the one the user inputted
    else:
        print("skipping")
    return _stop_colors_dict

def nod(): #nod servo back and forth 5 periods
    for waves in range(5):
        nod_servo.min()
        sleep(0.25)
        nod_servo.max()
        sleep(0.25)
    nod_servo.detach()

def main():
    ask_test = input("Input 'test' to run test, nothing to skip >>> ") #asks to run test or to skip it
    if(ask_test == "test"):
        run_test()
    colors_list = get_colors()
    while True:
        print("Input traffic light color 'red' 'yellow' or 'green'")
        user_color = input(">>> ")
        stop_colors_dict_ = stop_dict_change(colors_list[0], user_color)
        for i in colors_list[1:]: #for each eye ask for hex code
            print("Input hex code for eye")
            user_eye = input(">>> ")
            if(user_eye):
                user_eye = user_eye.upper() + "A" #just to make it easier to extract each color's hex
                count = 0
                for e in i: #for each color of the eye
                    try:
                        hex_input = user_eye[-7+count:-5+count] #reads the portion of the hex corresponding to the color
                        i[e] = int(hex_input, 16) #sets the current color's dictionary value to the numeric version of the hex
                    except:
                        print("skipping, invalid digit")
                    else:
                        i[e] = i[e] / 255 #converts to a range of 0-1
                        count += 2
                        if("red" in e): #red is much brighter than the green or blue, so it is halved
                            i[e] = i[e] / 2
        print(colors_list)
        stop_light(stop_colors_dict_)
        eyes_RGB(colors_list[1:])
        nod()

main()

# =============================================================================
# https://github.com/siewilliam01/RasPi5/blob/main/makey_bot_iroman_hex.py
# William Sie
# Name: makey_bot_iroman.py
# Description: Turns on one light only based on user console input
# Dependencies: python 3
# License: GNU General Public License v2.0
# Inputs: console
# Outputs: 3x LEDs
# Created: 03/12/25
# Updated: 03/27/25


