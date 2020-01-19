# use this script to display an original image in Python GUI
# select coordinates for a mask, to be applied to a single image (using mask.py) or to a folder of images (using mask_all.py)

# note: imshow function does not always work in Jupyter notebooks and colaboratory
# works best when run from command line

from matplotlib import pyplot as plt
import cv2
import numpy as np

# load image and get shape values (h, w, num. channels)
picture = cv2.imread("A.jpg")
print(picture.shape)

# display rgb image with plot lines
plt.imshow(cv2.cvtColor(picture, cv2.COLOR_BGR2RGB))
plt.show()
