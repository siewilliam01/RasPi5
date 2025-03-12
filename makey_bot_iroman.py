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

def main():
    colors_dict = {'red' : 'off', 'yellow' : 'off', 'green' : 'off'}
    while True:
        print("Input 'red' 'yellow' or 'green'")
        user_color = input(">>> ")
        if(user_color in colors_dict):
            for key in colors_dict:
                colors_dict[key] = 'off'
            colors_dict[user_color] = 'on'
            stop_light(colors_dict)
        else:
            print("not a valid color")

main()