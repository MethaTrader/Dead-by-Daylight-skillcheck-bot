# Dead by Daylight Skillcheck detection bot

### Hello everyone, this is one of my first bots written in python using the OpenCV computer vision library


### The code is pretty straightforward. This bot allows you to solve reaction checks in the **Dead by daylight** game.  

***
# How the bot works?

The bot looks for a pink pixel color in the center of the 300x300 px screen. And if it finds a pink pixel, space is pressed.

### The pink pixel is obtained by superimposing a red arrow on the white area of the skill check
 
#
**Important!**

Sometimes the red arrow hits the wrong area. Therefore, I made a check that pink pixels were searched only outside the circle or on it.

*(x-centerX)^2+(y-centerY)^2 >= R^2*

        if(math.pow(x_pink-150,2)+math.pow(y_pink-150,2) >= 60**2):
            #image found


Good luck and enjoy the game!