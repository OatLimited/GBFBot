import pyautogui
import cv2
import time
import numpy as np

boss_template = cv2.imread("img/Boss.png", 0)  # Grayscale
ok_template = cv2.imread("img/OK.png", 0)
attack_template = cv2.imread("img/Foottage/Element/Attack button.png", 0)
auto_template = cv2.imread("img/auto.png", 0)
backup_template = cv2.imread("img/Backup.png", 0)
PlayAgian_template = cv2.imread(
    "img/Foottage/Element/Play_again button.png", 0)


def find_button(input_template, sec,  threshold=0.7, status=0):

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
        if status == 1:
            return True
        # Click at detected location
        pyautogui.click(max_loc[0] + 10, max_loc[1] + 10)
        print("click ")
        time.sleep(sec)
        return True
    else :
        print(f"Cannt find button at threshold {threshold}")

#Click screen for proceed
pyautogui.click(812, 396)
while True:
    #Before battle
    print("clicking ok")
    find_button(ok_template, 8)

    print("clicking attack")
    find_button(attack_template, 2)

    print("clicking auto")
    find_button(auto_template)

    #During battle
    print("Waiting for result")
    while True:
        battle_status = find_button(ok_template, sec=2, status=1)
        if battle_status == True:
            break

    # After battle
    time.sleep(3)
    print("clicking ok")
    find_button(ok_template, sec=2)

    #Retrying function
    while True:
        print("clicking Play again")
        checking = find_button(PlayAgian_template, sec=2)
        
        #Exist EM screen
        if checking == True:
            break
        pyautogui.click(163, 251)
    time.sleep(10)
