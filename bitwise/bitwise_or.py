# bitwise OR of 2 input images 
	 
import cv2 
import numpy as np 
	
# path to input images are specified and 
# images are loaded with imread command 
image1 = cv2.imread('input1.jpg') 
image2 = cv2.imread('input2.jpg') 

# cv2.bitwise_or is applied over the 
# image inputs with applied parameters 
dest_or = cv2.bitwise_or(image2, image1, mask = None) 

# the window showing output image 
# with the Bitwise OR operation 
# on the input images 
cv2.imshow('Bitwise OR', dest_or) 
cv2.imwrite('bitwise_or.jpg', dest_or)

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
