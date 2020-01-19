# arithmetic operation of 
# addition of pixels of two images

import cv2 
import numpy as np 

image1 = cv2.imread('input1.jpg') 
image2 = cv2.imread('input2.jpg') 

# cv2.addWeighted is applied over the 
# image inputs with applied parameters 
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0) 

# the window showing output image 
# with the weighted sum 
cv2.imshow('Weighted Image', weightedSum) 
cv2.imwrite('/Users/surgesm/Desktop/addition_output.jpg', weightedSum)

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 