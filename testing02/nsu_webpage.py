import pyautogui
import time



""" home =pyautogui.locateOnScreen('home.png')
home_center = pyautogui.center(home)
pyautogui.click(home_center)
time.sleep(2)

pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('apply.png')))
time.sleep(2)
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('admission_application.png')))
time.sleep(2) """



""" clicks = ['apply.png', 'future_students.png','current_students.png', 'athletics.png','workforce.png']
for click in clicks:
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(click)))
    time.sleep(2)
 """


# need to teach how to delay snip and sketch
# screen captures work better if you use larger rectangles like whole buttons
# use png files rather than jpg files
# it looks like some time is needed to recognize the images
pyautogui.press('winleft')
pyautogui.write('Chrome')
pyautogui.press('enter')
# https://www.howtogeek.com/114518/47-keyboard-shortcuts-that-work-in-all-web-browsers/  Ctrl-L (load)
time.sleep(2)
pyautogui.hotkey('ctrl','l') #shift focus to the address bar (load)
pyautogui.write('nsuok.edu\n')
time.sleep(2)
buttons = ['degrees_and_majors.png', 'colleges.png','academic_advising.png','bookstore.png','extended_learning.png','student_support_services.png']
for button in buttons:
    print(f'click on {button}')
    while pyautogui.locateOnScreen(button) is None:
        pyautogui.PAUSE = 2.5
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(button)))
    print('click back')
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('back.png')))
    time.sleep(2)
pyautogui.hotkey('alt','f4') #close the browser
print("done")


 
 
'''
while pyautogui.locateOnScreen('home.png') is None:
    time.sleep(.5)
'''