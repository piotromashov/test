import pyautogui
import time

while True:
    print(pyautogui.position())  # Prints (x, y) coordinates
    time.sleep(0.1)  # Updates every 0.1 seconds