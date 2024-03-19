import numpy as np
import pyautogui
import cv2
import time

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "video.avi"
#fps = 10
#prev = 0
out = cv2.VideoWriter(filename, codec, 20.0, (resolution))

while True:

    #time_elapsed = time.time() - prev
    img = pyautogui.screenshot()
   # if time_elapsed > 1.0/fps:
    #    prev = time.time()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    #cv2.waitKey(100)
    
cv2.destroyAllWindows()
out.release()
