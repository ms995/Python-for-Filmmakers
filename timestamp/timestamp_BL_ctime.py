# timestamp - left justified at bottom
# current settings for 720x480 pixel images
# white line @ 80 pixels thick and text in black

# abbreviated month, day of month, year
# hour:minute:second based on 24-hr clock
# ex: 'Dec 27 2019 - 20:37:15'

import os
import numpy as np
import cv2
from datetime import time, datetime

# folder which contains all the images 
os.chdir("/Users/surgesm/Desktop/matplotlib/c") 

# print current directory
print(os.getcwd())

num_of_images = len(os.listdir())
print(num_of_images)

for f in os.listdir(os.getcwd()):
    image = cv2.imread(f, 1)
    statinfo = (os.stat(f).st_birthtime)
    stamp = (datetime.fromtimestamp(statinfo))
    formattedstamp = stamp.strftime("%b %d %Y - %H:%M:%S")
    new = cv2.line(image, (0,480), (720,480), (255, 255, 255), 80)
    font = cv2.FONT_HERSHEY_PLAIN
    new = cv2.putText(image, formattedstamp, (30,470), font, 2, (0,0,0), 2, cv2.LINE_AA)
    cv2.imwrite(f, new)

cv2.waitKey(0)
cv2.destroyAllWindows()
