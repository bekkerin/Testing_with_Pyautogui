# load csv data to dictionary https://www.geeksforgeeks.org/load-csv-data-into-list-and-dictionary-using-python/
# the csv file needs to have a first column with a blank header and then numbers for the first field of each row
# in Visual Studio, use text boxes to show the output but set them as readonly. That way they can still  be tabbed through.

import pyautogui, time
import pyperclip # to copy text from the revenue buttons
from csv import DictReader 

#give the user a chance to kill the script
print(' 5 second pause to let user press Ctrl-C or to click on the running file to make the window active ')
time.sleep(5)

with open('tests_with_headers.csv','r') as f: 
    # number, ticketsA,ticketsB,ticketsC,chargesA,chargesB,chargesC,chargesTotal,message,TestName
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






""" 
    # Fill out the Greatest Fear(s) field.
    pyautogui.write(test['fear'] + '\t', interval=0.25)

    # Fill out the Source of Wizard Powers field.
    if test['source'] == 'wand':
        pyautogui.write(['down', 'enter','\t'] , interval=0.25) # needs enter before the tab
    elif test['source'] == 'amulet':
        pyautogui.write(['down', 'down', 'enter', '\t'] , interval=0.25) # extra enter
    elif test['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', 'enter', '\t'] , interval=0.25)# extra enter
    elif test['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', 'enter', '\t'] , interval=0.25)# extra enter             Alice   

    # Fill out the RoboCop field.
    if test['robocop'] == 1:
        pyautogui.write([' ', '\t', '\t'] , interval=0.25) # 0.5 seconds not enough, increased to 1.5
    elif test['robocop'] == 2:
        pyautogui.write(['right', '\t', '\t'] , interval=0.25)
    elif test['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t', '\t'] , interval=0.25)
    elif test['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t', '\t'] , interval=0.25)
    elif test['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t', '\t'] , interval=0.25)

    time.sleep(1)

    # Fill out the Additional Comments field.
    pyautogui.write(test['comments'] + '\t', interval=0.25)


    # "Click" Submit button by pressing Enter.
    time.sleep(0.5) # Wait for the button to activate.
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Submitted form.')
    time.sleep(5)

    # Click the Submit another response link.
    #pyautogui.click(submitAnotherLink[0], submitAnotherLink[1]) # no need to save coordinates, just use one tab to get to link and then press enter
    pyautogui.write(['\t','enter'])

     """