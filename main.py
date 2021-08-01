from win32con import CCHDEVICENAME
import recording
import vision 
import cv2 as cv
import mss
import time
import numpy as np
import win32gui, win32con
import keyboard
import sys
from time import sleep

print("Started!")

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = recording.get_monitor()

    while "Screen capturing":
        #sleep(0.1)
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        vision.draw_circle(img)
        
        cv.imshow("Recording", vision.draw_circle(img))

        hWnd = win32gui.FindWindow(None, "Recording")
        win32gui.SetWindowPos(hWnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('Closing...')
            sys.exit()

        # Press "q" to quitqqq
        if cv.waitKey(25) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break

