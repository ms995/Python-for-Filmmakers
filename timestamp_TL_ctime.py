# timestamp - left justified at top
# current settings for 720x480 pixel images
# grey line @ 80 pixels thick and text in white

# month (as digit), day of month, year
# hour:minute:second based on 12-hr clock (AM/PM)
# ex: '2019-07-04 8:29:04 PM'

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
    formattedstamp = stamp.strftime("%Y-%m-%d %l:%M:%S %p")
    new = cv2.line(image, (0,0), (720,0), (105, 105, 105), 80)
    font = cv2.FONT_HERSHEY_PLAIN
    new = cv2.putText(image, formattedstamp, (30,30), font, 2, (255,255,255), 2, cv2.LINE_AA)
    cv2.imwrite(f, new)

cv2.waitKey(0)
cv2.destroyAllWindows()