import pyautogui

#get resolution
screenW, screenH= pyautogui.size()
#set box of vision
width, height = (300,300)

#get coord part of screen (center screen)
def get_coord():
    x,y,w,h = (screenW//2 - width//2, screenH//2 - height//2, width, height)
    return (x,y,w,h)

def get_monitor():
    x,y,w,h = (screenW//2 - width//2, screenH//2 - height//2, width, height)
    monitor = {"top": y, "left": x, "width": w, "height": h}

    return monitor

#record screen
def get_frame():
    img = pyautogui.screenshot(region=(get_coord()))
    return img