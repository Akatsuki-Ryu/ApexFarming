import time

import keyboard
import pyautogui
from pyautogui import *

Random = [ '1', '2', '3', '4','x','c']
randommove =['a',  'd' ]
overridemove=['w','s','a',  'd' ]

gamestate = 0  # 0 is lobby , 1 is in game
tic = 0
paused = 0

pause_duration = 10  # Inactivity duration in seconds to resume automation
last_input_time = time.time()

log_filename = "game_log.txt"  # Specify the filename for the log file

def log_game_information(game_length):
    with open(log_filename, "a") as log_file:
        log_file.write(f"Game Length: {game_length} seconds\n")
        log_file.write(f"Current Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.write("===============================\n")
        

while True:
    time.sleep(0.1) #to prevent overload

    # Check if a key has been pressed
    if any(keyboard.is_pressed(key) for key in overridemove):
        last_input_time = time.time()
        # Pause the automation
        if paused == 0:
            print("override")
        paused = 1
        time.sleep(pause_duration/2.1)
        continue

    # Check for inactivity duration
    if time.time() - last_input_time > pause_duration:
        # Resume the automation
        if paused == 1:
            print("Resume")
        paused = 0
        last_input_time = time.time()
        
        if pyautogui.locateOnScreen('ManuNotReady.png', region=(0, 538, 447, 528), grayscale=True, confidence=0.7) != None:
            print("in lobby")
            if pyautogui.locateOnScreen('Team.png', region=(3, 520, 445, 304), grayscale=True, confidence=0.7) != None:
                pyautogui.click(171, 675)
                time.sleep(0.5)
                pyautogui.click(171, 675)
                print("lobby, setup team")
            pyautogui.click(230, 950)
            time.sleep(0.5)
            pyautogui.click(230, 950)     
            time.sleep(0.5)
            pyautogui.click(230, 950)  


        if pyautogui.locateOnScreen('ManuNotReady2.png', region=(0, 538, 447, 528), grayscale=True, confidence=0.7) != None:
            print("in lobby2")
            if pyautogui.locateOnScreen('Team.png', region=(3, 520, 445, 304), grayscale=True, confidence=0.7) != None:
                pyautogui.click(171, 675)
                time.sleep(0.5)
                pyautogui.click(171, 675)
                print("lobby, setup team")
            pyautogui.click(230, 950)
            time.sleep(0.5)

        if pyautogui.locateOnScreen('Team.png', region=(3, 520, 445, 304), grayscale=True, confidence=0.9) != None:
            pyautogui.click(171, 675)
            time.sleep(0.5)
            #pyautogui.click(171, 675)
            print("lobby, setup team")

        if pyautogui.locateOnScreen('ManuReady.png', region=(0, 538, 447, 528), grayscale=True, confidence=0.7) != None:
            if gamestate == 1:
                print("Waiting for game to start")
                gamestate = 0
            time.sleep(5)

        if pyautogui.locateOnScreen('InGame.png', region=(87, 755, 379, 304), grayscale=True, confidence=0.5) != None:
            #print("In game waiting")
            keyboard.press_and_release(Random)
            time.sleep(1)
            timer = 0
            time.sleep(6)

            if gamestate == 0:
                gamestate = 1
                print("In game, landed and playing")
                tic = time.perf_counter()
                #set a offset movement 
                keytimer = 0
                keyboard.press('w')
                time.sleep(5)
                keyboard.release('w')
                pyautogui.move(20, 0)  # Move the mouse 10 pixels to the right

            if tic != 0:
                toc = time.perf_counter()
                # print(f"InGame for {toc - tic:0.4f} seconds")

        if pyautogui.locateOnScreen('dead.png', region=(441, 19, 1017, 304), grayscale=True, confidence=0.6) != None:
            print("In game, dead")
            if tic != 0:
                toc = time.perf_counter()

                print(f"==============================================InGame for {toc - tic:0.4f} seconds")
                # Output log message here
                log_game_information(toc - tic)
            #gamestate = 0
            #pyautogui.click(1771, 1040)
            #time.sleep(0.5)
            #pyautogui.click(1771, 1040)
            time.sleep(0.5)
            keyboard.press_and_release('space')
            time.sleep(0.5)

            

        if pyautogui.locateOnScreen('leave.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.6) != None:
            print("In game, leaving match")
            pyautogui.click(963, 623)
            time.sleep(0.5)
            pyautogui.press('esc')

        if pyautogui.locateOnScreen('space.png', region=(676, 777, 619, 304), grayscale=True, confidence=0.6) != None:
            keyboard.press_and_release('space')

        if pyautogui.locateOnScreen('yes.png', region=(506, 550, 912, 304), grayscale=True, confidence=0.6) != None:
            pyautogui.click(850, 713)
            time.sleep(0.5)
            pyautogui.click(850, 713)

        if pyautogui.locateOnScreen('jump.PNG', region=(715, 743, 513, 304), grayscale=True, confidence=0.9) != None:
            print("In game, jumping")

        if pyautogui.locateOnScreen('Contunue.PNG', region=(773, 581, 379, 304), grayscale=True, confidence=0.6) != None:
            pyautogui.click(952, 717)
            time.sleep(0.5)
            pyautogui.click(952, 717)

        if pyautogui.locateOnScreen('startmanu.PNG', region=(773, 581, 379, 304), grayscale=True, confidence=0.6) != None:
            print("starting game")
            pyautogui.click(952, 717)
            time.sleep(0.5)
            pyautogui.click(952, 717)
