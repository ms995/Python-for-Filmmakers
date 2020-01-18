# Python program to explain cv2.ellipse() method 

import cv2 
	
inpath = r'/Users/surgesm/Desktop/P4F/Figure_1a.png' # set path to original image file
outpath = '/Users/surgesm/Desktop/P4F/Figure_1a_ellipse.png' # rename and state where to save new file
	
# Reading an image in default mode 
image = cv2.imread(inpath) 
print(image.shape) # will print in format: height, width, channels
print(image.shape[0]) # print width only
print(image.shape[1]) # print height only

# Place ellipse at center of image
height = int((image.shape[0])/2)
width = int((image.shape[1])/2)
# Python has a built-in function to convert floats to integers: int()
# In this case, 390.8 will be converted to 390. 
# When converting floats to integers with the int() function, 
# Python cuts off the decimal and remaining numbers of a float 
# to create an integer.

# print dimensions of ellipse
print(height)
print(width)

# Window name in which image is displayed 
window_name = 'Image'

# enter coordinates of ellipse.
# The coordinates are represented as tuples of two values 
# i.e. (X coordinate value, Y coordinate value).
center_coordinates = (width, height) 

axesLength = (100, 50) 
angle = 0
startAngle = 0
endAngle = 360

# Blue color in BGR 
color = (255, 0, 0) 

# Line thickness of -1 px means ellipse will be filled in
thickness = -1

# Using cv2.ellipse() method 
# Draw a ellipse with blue line borders
image = cv2.ellipse(image, center_coordinates, axesLength, angle, 
						startAngle, endAngle, color, thickness) 

# Displaying the image 
cv2.imshow(window_name, image) 

# Save image (if first argument is set to inpath, it will overwrite the original)
cv2.imwrite(outpath, image)

cv2.waitKey(0)
cv2.destroyAllWindows