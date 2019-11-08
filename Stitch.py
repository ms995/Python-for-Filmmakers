# importing libraries 
import os 
import cv2 
from PIL import Image 

# Checking the current directory path 
print(os.getcwd()) 

# Folder which contains all the images 
# from which video is to be generated 
#surgesm on macbook
os.chdir("/Users/surgesm/Desktop/flow/imagesets/532c") 
path = "/Users/surgesm/Desktop/flow/imagesets/532c"

num_of_images = len(os.listdir('.')) 
print(num_of_images) 

for file in os.listdir('.'): 
	im = Image.open(os.path.join(path, file)) 
	# im.show() # uncomment this for displaying the image 

# Video Generating function 
def generate_video(): 
	image_folder = '/Users/surgesm/Desktop/flow/imagesets/532c' # make sure to use your folder 
	video_name = '532c_2_24_5fps.avi'
	os.chdir("/Users/surgesm/Desktop/flow/imagesets/532c") 
	
	images = [img for img in os.listdir(image_folder) 
			if img.endswith(".jpg") or
				img.endswith(".jpeg") or
				img.endswith("png")] 
	
	# Array images should only consider 
	# the image files ignoring others if any 
	print(images) 

	frame = cv2.imread(os.path.join(image_folder, images[0])) 

	# setting the frame width, height width 
	# the width, height of first image 
	height, width, layers = frame.shape 

	# 5fps
	video = cv2.VideoWriter(video_name, 0, 5, (width, height)) 

	# Appending the images to the video one by one 
	for image in images: 
		video.write(cv2.imread(os.path.join(image_folder, image))) 
	
	# Deallocating memories taken for window creation 
	cv2.destroyAllWindows() 
	video.release() # releasing the video generated 


# Calling the generate_video function 
generate_video() 

