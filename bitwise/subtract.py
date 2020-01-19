# arithmetic operation of 
# subtraction of pixels of two images 
   
import cv2  
import numpy as np  
    
# path to input images are specified and   
# images are loaded with imread command  
image1 = cv2.imread('input1.jpg')  
image2 = cv2.imread('input2.jpg') 
  
# cv2.subtract is applied over the 
# image inputs with applied parameters 
sub = cv2.subtract(image1, image2) 
  
# the window showing output image 
# with the subtracted image  
cv2.imshow('Subtracted Image', sub)
cv2.imwrite('subtracted.jpg', sub) 
  
# De-allocate any associated memory usage   
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()  