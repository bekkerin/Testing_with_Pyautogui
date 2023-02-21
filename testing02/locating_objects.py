import pyautogui
import time

# disconnect  = pyautogui.locateOnScreen('disconnect.png')
# print(disconnect)
# time.sleep(1)
# disconnect_center = pyautogui.center(disconnect)
# print(disconnect_center)
# time.sleep(1)
# pyautogui.click(disconnect_center)
# time.sleep(1)

# time.sleep(1)
# open the calculator, enter a number. run the script to get the square
square = pyautogui.locateOnScreen('square.png')
square_center = pyautogui.center(square)
pyautogui.click(square_center)
