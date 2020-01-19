# Similar to mask.py, but applies the mask to an entire folder of images and saves the resulting images in that location
# Note that this script will overwrite existing files in the given folder

from matplotlib import pyplot as plt
import os
import numpy as np
import cv2

# folder which contains all the images 
image_folder = '/path/to/images'
os.chdir("/path/to/images") 

images = [img for img in os.listdir(image_folder) 
			if img.endswith(".jpg") or
				img.endswith(".jpeg") or
				img.endswith("png")] 

num_of_images = len(os.listdir())
print(num_of_images)
print(images) 

for f in images:
    if f.endswith(".jpg"):
        img = cv2.imread(f, 1)
        # print(img.shape)
        # print(img.dtype)
        mask = np.zeros(shape = img.shape, dtype = "uint8")
        cv2.rectangle(img = mask, pt1 = (160,50), pt2 = (300,250), color = (255, 255, 255), thickness = -1)
        maskedImg = cv2.bitwise_and(src1 = img, src2 = mask)
        new = maskedImg
        cv2.imwrite(f,new)

cv2.waitKey(0)
cv2.destroyAllWindows()
