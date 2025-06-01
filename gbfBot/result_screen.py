from ast import While
import pyautogui
import cv2
import time
import numpy as np

ok_template = cv2.imread("img/OK.png", 0)
backup_template = cv2.imread("img/Backup.png", 0)


def find_button(input_template, threshold=0.9):

    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    screen = cv2.imread("screenshot.png")

    template = input_template
    # Apply template matching
    result = cv2.matchTemplate(cv2.cvtColor(
        screen, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # If confidence is high, click the button
    time.sleep(2)
    if max_val >= threshold:
        # Click at detected location
        pyautogui.click(max_loc[0] + 10, max_loc[1] + 10)
        print("click ")
        return True


pyautogui.click(300, 400)
time.sleep(3)
print("clicking ok")
find_button(ok_template)
time.sleep(2)
while True:
    print("clicking backup")
    checking = find_button(backup_template)
    if checking == True:
        break
    pyautogui.click(163, 251)
