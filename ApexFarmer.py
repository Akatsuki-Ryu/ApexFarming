import keyboard
import pyautogui
import time
import keyboard
import random

Random = ['a','w','s','d','4','q','1','2','3','4']

while True:
    if pyautogui.locateOnScreen('ManuNotReady.png', region=(0,538,447,528), grayscale=True, confidence=0.5) != None:
        pyautogui.click(230, 950)
        time.sleep(0.5)
     
    if pyautogui.locateOnScreen('ManuNotReady2.png', region=(0,538,447,528), grayscale=True, confidence=0.5) != None:
        pyautogui.click(230, 950)
        time.sleep(0.5)
        
    if pyautogui.locateOnScreen('Team.png', region=(3,520,445,304), grayscale=True, confidence=0.9) != None:
        pyautogui.click(171, 675)
        time.sleep(0.5)
        pyautogui.click(171, 675)
                
    if pyautogui.locateOnScreen('ManuReady.png', region=(0,538,447,528), grayscale=True, confidence=0.7) != None:
         print("Waiting for game")
         time.sleep(5)
    
    
    if pyautogui.locateOnScreen('InGame.png', region=(87,755,379,304), grayscale=True, confidence=0.5) != None:
         print("In game waiting")
         keyboard.press_and_release(Random)
         time.sleep(0.5)
    
    if pyautogui.locateOnScreen('dead.png', region=(441,19,1017,304), grayscale=True, confidence=0.6) != None:
                pyautogui.click(1771, 1040)
                time.sleep(0.5)
                pyautogui.click(1771, 1040)
                
    
    if pyautogui.locateOnScreen('leave.png', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
                pyautogui.click(963, 623)
                time.sleep(0.5)
     
    if pyautogui.locateOnScreen('space.png', region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
     keyboard.press_and_release('space')
     
    if pyautogui.locateOnScreen('yes.png', region=(506,550,912,304), grayscale=True, confidence=0.6) != None:
         pyautogui.click(850, 713)
         time.sleep(0.5)
         pyautogui.click(850, 713)
         
    if pyautogui.locateOnScreen('jump.PNG', region=(715,743,513,304), grayscale=True, confidence=0.9) != None:
         keyboard.press_and_release('Enter')
         time.sleep(0.5)
         keyboard.press_and_release('L')
         time.sleep(0.5)
         keyboard.press_and_release('O')
         time.sleep(0.5)
         keyboard.press_and_release('L')         
         time.sleep(0.5)
         keyboard.press_and_release('Enter')

    if pyautogui.locateOnScreen('Contunue.PNG', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
         pyautogui.click(952, 717)
         time.sleep(0.5)
         pyautogui.click(952, 717)
         
    if pyautogui.locateOnScreen('startmanu.PNG', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
         pyautogui.click(952, 717)
         time.sleep(0.5)
         pyautogui.click(952, 717)


    if pyautogui.locateOnScreen('MenuReady_hover.png', region=(0, 538, 447, 528), grayscale=True, confidence=0.5) != None:
        if gamestate == 1:
            gamestate = 0
            print("lobby, Waiting to start")
        time.sleep(5)

    if pyautogui.locateOnScreen('InGame.png', region=(87, 755, 379, 304), grayscale=True, confidence=0.8) != None:
        if gamestate == 0:
            gamestate = 1
            print("In game, landed and playing")
            tic = time.perf_counter()

        if tic != 0:
            toc = time.perf_counter()
            # print(f"InGame for {toc - tic:0.4f} seconds")

        keyboard.press_and_release('a')
        time.sleep(0.5)
        keyboard.press_and_release('d')
        time.sleep(0.5)

    if pyautogui.locateOnScreen('dead.png', region=(441, 19, 1017, 304), grayscale=True, confidence=0.6) != None:
        print("In game, dead")
        if tic != 0:
            toc = time.perf_counter()
            print(f"=======================================InGame for {toc - tic:0.4f} seconds")
        # gamestate = 0
        click(1771, 1040)
        time.sleep(0.5)
        click(1771, 1040)

    if pyautogui.locateOnScreen('leave.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.6) != None:
        print("In game, leaving match")
        click(963, 623)
        time.sleep(0.5)

    if pyautogui.locateOnScreen('space.png', region=(676, 777, 619, 304), grayscale=True, confidence=0.6) != None:
        keyboard.press_and_release('space')

    if pyautogui.locateOnScreen('yes.png', region=(506, 550, 912, 304), grayscale=True, confidence=0.6) != None:
        click(850, 713)
        time.sleep(0.5)
        click(850, 713)

    if pyautogui.locateOnScreen('jump.PNG', region=(715, 743, 513, 304), grayscale=True, confidence=0.9) != None:
        print("In game, jumping")
        # keyboard.press_and_release('Enter')
        # time.sleep(0.5)
        # keyboard.press_and_release('L')
        # time.sleep(0.5)
        # keyboard.press_and_release('O')
        # time.sleep(0.5)
        # keyboard.press_and_release('L')
        # time.sleep(0.5)
        # keyboard.press_and_release('Enter')*/

    if pyautogui.locateOnScreen('Contunue.PNG', region=(773, 581, 379, 304), grayscale=True, confidence=0.6) != None:
        click(952, 717)
        time.sleep(0.5)
        click(952, 717)

    if pyautogui.locateOnScreen('startmanu.PNG', region=(773, 581, 379, 304), grayscale=True, confidence=0.6) != None:
        print("starting game")
        click(952, 717)
        time.sleep(0.5)
        click(952, 717)
