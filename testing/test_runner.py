# load csv data to dictionary https://www.geeksforgeeks.org/load-csv-data-into-list-and-dictionary-using-python/
# in Visual Studio, use text boxes to show the output but set them as readonly. The TabStop property has been set to True in code.

import pyautogui, time
import pyperclip # to copy text from the revenue boxes
from csv import DictReader 
import os

executable_path = "C:\\Temp\\Testing_with_Pyautogui-main\\Testing_with_Pyautogui-main\\source\\StadiumSeating\\StadiumSeating\\bin\\Debug\\netcoreapp3.1\\StadiumSeating.exe"
os.startfile(executable_path)

#give the user a chance to kill the script
print(' 5 second pause to let user press Ctrl-C or to click on the running file to make the window active ')
time.sleep(5)

with open('tests_with_headers.csv','r') as f: 
    # ticketsA,ticketsB,ticketsC,chargesA,chargesB,chargesC,chargesTotal,message,TestName
    dict_reader = DictReader(f)
    formData = list(dict_reader)

print(formData) # just so we can see the list of test dictionaries

tests_failed = 0 # number of tests failed

for test in formData:
    #tabbing: classA, classB, ClassC, Calculate, revenueA, revenueB, revenueC, _
    #  totalRevenu, clear, automatically back to classA

    test_failed = False # assume this test will not fail

    # Fill out the Class A field.
    pyautogui.write(test['ticketsA'] + '\t', interval=0.25)

    # Fill out the Class B field.
    pyautogui.write(test['ticketsB'] + '\t', interval=0.25)

    # Fill out the Class C field.
    pyautogui.write(test['ticketsC'] + '\t', interval=0.25)

    # click the Calculate Revenue button 
    pyautogui.press('enter')
    pyautogui.write('\t')

    # go to the Class A charges and check them
    pyautogui.hotkey('ctrl','c')  # to copy to clipboard
    text = pyperclip.paste()
    expected = test['chargesA']
    if expected != text:
        print(f'Expected: {expected} , actual {text} \n')
        test_failed = True
    pyautogui.write('\t')

    # go to the Class Bb charges and check them
    pyautogui.hotkey('ctrl','c')  # to copy to clipboard
    text = pyperclip.paste()
    expected = test['chargesB']
    if expected != text:
        print(f'Expected: {expected} , actual {text} \n')
        test_failed = True
    pyautogui.write('\t')

    # go to the Class C charges and check them
    pyautogui.hotkey('ctrl','c')  # to copy to clipboard
    text = pyperclip.paste()
    expected = test['chargesC']
    if expected != text:
        print(f'Expected: {expected} , actual {text} \n')
        test_failed = True
    pyautogui.write('\t')

    # go to the total charges and check them
    pyautogui.hotkey('ctrl','c')  # to copy to clipboard
    text = pyperclip.paste()
    expected = test['chargesTotal']
    if expected != text:
        print(f'Expected: {expected} , actual {text} \n')
        test_failed = True
    pyautogui.write('\t')

    if test_failed:
        print(f'test {test} failed\n')
        tests_failed +=1

    #now we are at the clear button , automatically goes back to ClassA
    pyautogui.press('enter') # to clear the boxes with the clear button
    
print(f'{tests_failed} tests failed of {len(formData)}\n')


