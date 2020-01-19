# note: filenames must first be formatted to contain 'created time' (see rename_files.py for help)
# timestamp.py adds a timestamp banner to the top 80px of each image

import os
import numpy as np
import cv2

# folder which contains all the images 
os.chdir("/Users/msurges/Desktop/timestamping/b2") 

# print current directory
print(os.getcwd())

num_of_images = len(os.listdir())
print(num_of_images)

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    # print(os.path.splitext(f)) # uncomment to test
    f_cam, f_time = file_name.split('x')
    # print(f_time) # isolates time from camera number # uncomment to test
    image = cv2.imread(f, 1)
    new = cv2.line(image, (0,0), (720,0), (105,105,105), 80)
    font = cv2.FONT_HERSHEY_PLAIN
    new = cv2.putText(image, f_time, (30,30), font, 2, (255,255,255), 2, cv2.LINE_AA)
    cv2.imwrite(f,new)

cv2.waitKey(0)
cv2.destroyAllWindows()
