import pyautogui as pag
import keyboard
import time
while True:
    pag.keyDown('enter')
    time.sleep(0.1)
    pag.keyUp('enter')
    time.sleep(0.1)
    pag.keyDown('w')
    time.sleep(0.1)
    pag.keyUp('w')  
    time.sleep(0.1)
    pag.keyDown('enter')
    time.sleep(0.1)
    pag.keyUp('enter')
    time.sleep(0.1)
    pag.keyDown('w')
    time.sleep(0.1)
    pag.keyUp('w')
    time.sleep(0.1)
    pag.click()
    time.sleep(0.1)
    if keyboard.press_and_release('p'):
        exit()