import pyautogui

while True:
    x, y = pyautogui.position()
    print(f"Mouse position: ({x}, {y})", end="\r")
