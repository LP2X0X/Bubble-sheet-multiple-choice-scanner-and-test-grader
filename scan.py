# Import the necessary packages
import os
import cv2
import imutils
import argparse
import numpy as np
from transform import four_point_transform
from skimage.filters import threshold_local

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image to be scanned")
args = vars(ap.parse_args())

# Load the image and compute the ratio of the old height
# to the new height, clone it, and resize it
image = cv2.imread(args["image"])
# Use this in case the pincture is not rotated
# image = imutils.rotate_bound(image, -90)

# Convert the image to grayscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 75, 220)
cv2.imshow("Canny Edges Detection", imutils.resize(edged, height = 650))
cv2.waitKey(0)

# Apply dilation to image so that the Contour can be detected easier
kernel = np.ones((3,3), np.uint8)
edged = cv2.dilate(edged, kernel)
cv2.imshow("After Dilation", imutils.resize(edged, height = 650))
cv2.waitKey(0)

# Find the contours in the edged image, keeping only 3 
# largest ones, and initialize the screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:3]

# Loop over the contours
for c in cnts:
	# Approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	# If our approximated contour has four points, then we
	# can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break

# Apply the four point transform to obtain a top-down
# view of the original image
warped = four_point_transform(image, screenCnt.reshape(4, 2))

cv2.imshow("The Test", imutils.resize(warped, height = 650))
cv2.waitKey(0)

cv2.imwrite(r"D:\School_Documents\XLA\PROJECT\input.png", warped)
cv2.waitKey(0)

string = 'cmd /k "python test_grader.py --image input.png\"'
os.system(string)

