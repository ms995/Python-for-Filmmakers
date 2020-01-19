# bitwise NOT of 2 input images
      
import cv2  
import numpy as np  
     
# path to input images are specified and   
# images are loaded with imread command  
image1 = cv2.imread('input1.jpg')  
image2 = cv2.imread('input2.jpg') 
  
# cv2.bitwise_not is applied over the 
# image input with applied parameters  
dest_not1 = cv2.bitwise_not(image1, mask = None) 
dest_not2 = cv2.bitwise_not(image2, mask = None) 
  
# the windows showing output image 
# with the Bitwise NOT operation 
# on the 1st and 2nd input image 
cv2.imshow('Bitwise NOT on image 1', dest_not1) 
cv2.imwrite('bitwise_not1.jpg', dest_not1)
cv2.imshow('Bitwise NOT on image 2', dest_not2) 
cv2.imwrite('bitwise_not2.jpg', dest_not2)
   
# De-allocate any associated memory usage   
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()  