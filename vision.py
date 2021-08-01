import pyautogui
import cv2 as cv
import numpy as np
import math

"""Computing Vision"""

#finding pink pixel on part of screen
def find_pink(image):
    image = cv.cvtColor(image, cv.COLOR_RGBA2RGB)
    #lower_white = np.array([174, 170, 238])
    lower_white = np.array([174, 170, 238])  # BGR-code of your lowest white
    upper_white = np.array([215,211,250])   # BGR-code of your highest white 

    mask = cv.inRange(image, lower_white, upper_white)  
    #get all non zero values
    coord=cv.findNonZero(mask)

    #if not found
    if(coord == "None"):
        return False
    else:    
        return coord

def draw_circle(image):
    try: 
        (x_pink,y_pink) = find_pink(image)[0][0]
        
        if(math.pow(x_pink-150,2)+math.pow(y_pink-150,2) >= 60**2):
            pyautogui.press('space')  # press the Space key
            color = (0, 255, 255)
            thickness = 2
            radius = 10
            image = cv.circle(image,(x_pink,y_pink), radius, color, thickness)
            return image
        else:
            return image
    except:
        #print("Not Found")
        image = cv.circle(image,(150,150), 64, (0,255,0), 2)
        return image



