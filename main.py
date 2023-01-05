# https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

# game running in 1600x900 window

import numpy
import pyautogui
import cv2
import time
from time import gmtime, strftime
import random
import win32gui
import yaml


# screen resolution
screenWidth = 1600
screenHeight = 900

# keybindings 
with open('resources/keybinding.yaml', 'r') as yamlfile:
    keybindings = yaml.safe_load(yamlfile)

# variables



# function screenshot creation and run code
def createScreenshot():
    # take screenshot and save it
    image = pyautogui.screenshot(region = (0, 0, screenWidth,screenHeight+25 ))
    image.save(r"C:\Users\MonkeyKing 2\Desktop\AutoMiningEVE\screenshots\1.png")

    #cv2 process image
    # image = cv2.cvtColor(numpy.array(image),0)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # pos returns coordinates left top width height, find match with confidence 0.5
    # pos = pyautogui.locateOnScreen("resources/undock.png", grayscale=True, confidence=.5)
    # print(pos)
    # pyautogui.moveTo(pos[0]+pos[2]/2, pos[1]+pos[3]/2)
    # pyautogui.click()

    time.sleep(5)
    
    # open location
    # pyautogui.keyDown('l')
    # time.sleep(1)
    # pos = pyautogui.locateOnScreen("resources/miningLocation.png", grayscale=True, confidence=0.5)
    # print(pos)
    # pyautogui.moveTo(pos[0]+pos[2]/2, pos[1]+pos[3]/2)
    # pyautogui.rightClick()

    # # warp to location
    # pos = pyautogui.locateOnScreen("resources/warpToLocation.png", grayscale=True, confidence=0.5)
    # print(pos)
    # pyautogui.moveTo(pos[0]+pos[2]/2, pos[1]+pos[3]/2)
    # pyautogui.click()

    # time.sleep(20)



    # start mining
    pos = pyautogui.locateOnScreen("resources/closestOre.png", grayscale=True, confidence=0.3)
    print(pos)
    pyautogui.moveTo(pos[0]+pos[2]/2, pos[1]+pos[3]/2+30)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.hotkey('ctrl')
    time.sleep(3)
    pyautogui.hotkey('f2')


    # wait until bag full
 
    while(1):
        time.sleep(0.5)
        pos = pyautogui.locateOnScreen("resources/CargoFull.png", grayscale=True, confidence=0.3)
        print(pos)
        if (pos != 'None'):
            print(strftime("%H:%M:%S", gmtime()), "Full")
        break

    







# run script
time.sleep(2)
print(strftime("%H:%M:%S", gmtime())),
createScreenshot()






# open resourceMenu alt-m / undock under air cv-image undock
# cv-image undock
# sleep
# close resourceMenu alt-m
# open locaiton menu L
# cv-image mining location
# right click warp to 0 - left click

# mouse move to 1st mining site - left click
# cv-image lockTargetIcon - left click\
# f2 start mining

# cv-image scan for CargoFull
# open location
# cv-image home or mouse location - right click dock - left click
# sleep / or cv-image dockedConfirmation

# alt-c 
# mouse drag location
# open item hangar alt-g
# mouse drag location - right click sell
# cv-image sellButton -left click
# close alt-g alt-c
