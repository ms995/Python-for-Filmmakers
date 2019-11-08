# show original image and get coordinates for a mask

from matplotlib import pyplot as plt
import cv2
import numpy as np

# load image and get shape values (h, w, num. channels)
picture = cv2.imread("532.jpg")
print(picture.shape)

# display rgb image with plot lines
plt.imshow(cv2.cvtColor(picture, cv2.COLOR_BGR2RGB))
plt.show()