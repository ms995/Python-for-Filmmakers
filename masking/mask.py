# mask.py uses cv2 bitwise_and with two images:
# 1. the original, 2. the mask, with your choice of coordinates
# to create a new image with a rectangular mask

# Note that mask.py displays but doesn't save the result.
# I typically use this script to check before applying a mask to entire folders of images. 

from matplotlib import pyplot as plt
import cv2
import numpy as np

# Load the original image
picture = cv2.imread("A.jpg")
print(picture.shape)

# Create the basic black image: same shape 
mask = np.zeros(shape = picture.shape, dtype = "uint8")

# Draw a white, filled rectangle on the mask image
# pt1: upper left corner (x,y)
# pt2: lower right corner (x,y)
cv2.rectangle(img = mask, pt1 = (160,50), pt2 = (325,300), 
	color = (255, 255, 255), thickness = -1)

# Apply the mask and display the result
maskedImg = cv2.bitwise_and(src1 = picture, src2 = mask)

# Display masked image
cv2.imshow("maskedImg", mat=maskedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
