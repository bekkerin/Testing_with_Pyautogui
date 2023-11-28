import pyautogui
import pyperclip
import time

pyautogui.press('win') # windows key
time.sleep(.5)
pyautogui.write('ipcalc')
time.sleep(.5)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('tab')  
time.sleep(.5)
pyautogui.write('192.168.5.15/23')
time.sleep(.5)
pyautogui.press('enter')