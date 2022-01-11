import threading, random
import pyautogui as pg


random.seed();
while 1 == 1:
    x = random.uniform(0, 1500)
    y = random.uniform(0, 900)
    s = random.uniform(0, 100)
    pg.moveTo(x, y, 0.0000001)
    pg.click(x, y)
    pg.typewrite("1-0-0-6")
    pg.hotkey("shifTleft", "altleft")
    pg.hotkey("winleft", "capslock")
    pg.typewrite(["volumeup"])
    pg.typewrite(["pagedown"])
    
    
