# import library 

import time 
import pyautogui 
import os 
import pyfiglet

# cli setup 

os.system("title automate message by python")
os.system("cls")
os.system("color 06")

# asci art sign 

asci_art_sign  = pyfiglet.figlet_format(" automate message by python",font='bulbhead' )

print(asci_art_sign)

# couter about for loop 

i = 1

# the system is reading input about message and limit of the for loop 


print("could you insert the message \n\n")

message = input()

print("how many time do you wanna repete the message in chat ? \n\n")

limit_of_for_loop = int(input())


# search telegram on your operative system 

print("whatsapp is starting ")

pyautogui.press("win")

time.sleep(0.5)

pyautogui.write("whatsapp")

time.sleep(0.5)

pyautogui.press("enter")

time.sleep(7)

# loop until your limit have you choice 

for i in range(limit_of_for_loop):

    pyautogui.write(message)
    time.sleep(1)
    pyautogui.press("enter")




