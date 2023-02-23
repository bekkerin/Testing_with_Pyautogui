import pyautogui
import time


# time.sleep(1)
# open the calculator, enter a number. run the script to get the square
square = pyautogui.locateOnScreen('square.png')
square_center = pyautogui.center(square)
pyautogui.click(square_center)
