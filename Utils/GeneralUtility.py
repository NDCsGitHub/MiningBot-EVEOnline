import pyautogui
from time import gmtime, strftime
import time

# report the position of the target image
def locatePosition(mode, purpose, imageName, sleepTime, confidence):
    pos = pyautogui.locateOnScreen(f"resources/{imageName}.png", grayscale=True, confidence=confidence)
    print(strftime("%H:%M:%S", gmtime()), f'Location Found at {pos} to {purpose}')

    if imageName == 'closestOre':
        pyautogui.moveTo(pos[0]+pos[2]/2, pos[1]+pos[3]/2+30)
    else:
        pyautogui.moveTo(pos[0]+pos[2]/2, pos[1]+pos[3]/2)

    if mode=="rightClick":
        pyautogui.rightClick()
    else:
        pyautogui.click()
        
    print(strftime("%H:%M:%S", gmtime()), f'{purpose} in progress')
    time.sleep(sleepTime)


def checkCondition(condition, imageName, confidence):
    time.sleep(1)
    print(strftime("%H:%M:%S", gmtime()), f'{condition}')
    conditionImageLocation = pyautogui.locateOnScreen(f"resources/{imageName}.png", grayscale=True, confidence=confidence)

    if conditionImageLocation is not None:
        print(strftime("%H:%M:%S", gmtime()), f'{condition} conditon met at {conditionImageLocation}')
        return conditionImageLocation
    else:
        print(strftime("%H:%M:%S", gmtime()), f'{condition} conditon not met')
        return 'Condition not met'