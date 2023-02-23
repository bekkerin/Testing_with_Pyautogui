import pyautogui
import time

# first open Chrome and go to the NSU home page
pyautogui.press('winleft')
pyautogui.PAUSE
pyautogui.write('Chrome')
pyautogui.press('enter')
# hotkeys for Chrome can be found at https://www.howtogeek.com/114518/47-keyboard-shortcuts-that-work-in-all-web-browsers/ 
time.sleep(2)
pyautogui.hotkey('ctrl','l') # shift focus to the address bar (load)
pyautogui.write('nsuok.edu')
pyautogui.press('enter')
time.sleep(2)
pyautogui.scroll(-400)

# click successively on the buttons in the left column, then go back for the next button
buttons = ['degrees_and_majors.png', 'colleges.png','academic_advising.png','bookstore.png','extended_learning.png','student_support_services.png']
for button in buttons:
    print(f'click on {button}')
    while pyautogui.locateOnScreen(button) is None:
        pyautogui.PAUSE 
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(button)))
    print('click back')
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('back.png')))
    time.sleep(2)
pyautogui.hotkey('alt','f4') # close the browser
print("done")


