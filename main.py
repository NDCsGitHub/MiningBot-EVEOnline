import pyautogui
import time
from time import gmtime, strftime
import win32gui
import Utils
from Utils import GeneralUtility as gu


# function screenshot creation and run code
def MiningBot():

    # locate undock, click, and wait for 8 seconds
    gu.locatePosition('click', 'Undock', 'undock', 8, 0.7)

    # pyautogui.keyDown('l')
    time.sleep(5)

    # locate mining position
    gu.locatePosition('rightClick', 'Locate Mine', 'miningLocation', 5, 0.5 )

    # warp to minging location
    gu.locatePosition('click', 'Warp To Mining Location', 'warpToLocation', 50, 0.5 )

    # start mining
    gu.locatePosition('doubleClick', 'Start Mining', 'closestOre', 5, 0.3)
    time.sleep(10)
    pyautogui.hotkey('ctrl')
    time.sleep(3)
    pyautogui.hotkey('f2')

    # check for condition for full inventory
    while(1):
        while(1):
            if gu.checkCondition('Wait for Full Inventory', 'CargoFull', 0.4) != 'Condition not met':
                time.sleep(2)
                gu.locatePosition('rightClick', 'Locate Home', 'home', 2, 0.8 )
                gu.locatePosition('click', 'Dock to Home', 'dockToHome', 2 ,0.5)
                break
            
        #check for condition if arrive at base
        while(1):
            time.sleep(1)
            if gu.checkCondition('Wait for Arrive at Base', 'undock', 0.5) != 'Condition not met':
                print(strftime("%H:%M:%S", gmtime()), 'Returned to base')
                pyautogui.keyDown('alt')
                pyautogui.press('c')
                pyautogui.keyUp('alt')
                time.sleep(2)

                ore = pyautogui.locateOnScreen("resources/ore.png", grayscale=True, confidence=.6)
                print(ore)
                time.sleep(2)
                pyautogui.moveTo(ore[0]+ore[2]/2, ore[1]+ore[3]/2)
                pyautogui.mouseDown(button='left')
                time.sleep(1)
                pyautogui.moveTo(ore[0]+50, ore[1]+50)
                time.sleep(0.5)
                pyautogui.keyDown('alt')
                pyautogui.press('g')
                pyautogui.keyUp('alt')
                time.sleep(1)
                pyautogui.mouseUp(button='left')
                # close hangar and inventory
                pyautogui.keyDown('alt')
                pyautogui.press('g')
                pyautogui.keyUp('alt')

                pyautogui.keyDown('alt')
                pyautogui.press('c')
                pyautogui.keyUp('alt')
                time.sleep(1)
    
                break
        break


























# run script
count = 0
while(1):
    count+=count
    time.sleep(5)
    print(strftime("%H:%M:%S", gmtime()), f'Running Count:{count}')
    MiningBot()



