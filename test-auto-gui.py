import pyautogui
import time

def move(x, y):
    pyautogui.moveTo(x, y, 1)

while True:
     move(333, 90)
     time.sleep(0.5)
     move(350, 180)
     time.sleep(0.5)
     move(433, 90)
     time.sleep(10)
     print("...")



