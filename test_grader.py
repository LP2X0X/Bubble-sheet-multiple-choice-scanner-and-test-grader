# Import the necessary packages
import cv2
import imutils
import argparse
import numpy as np
from imutils import contours
from collect_data import Collect_Data
from skimage.filters import threshold_local

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")
args = vars(ap.parse_args())

# Load the image, cut out the edges, convert it to gray scale,
# blur it slightly, then threshold it using Otsu
image = cv2.imread(args["image"])
(a, b, c) = image.shape
image = image[10:a-10, 10:b-10]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(ret, thresh) = cv2.threshold(gray,  0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

cv2.imshow('Otsu Threshold', imutils.resize(thresh, height = 650))
cv2.waitKey(0)

# Find contours in the thresholded image, then initialize
# the list of contours that correspond to questions
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
questionCnts = []

# Loop over the contours
for c in cnts:
	# Compute the bounding box of the contour, then use the
	# bounding box to derive the aspect ratio
	(x, y, w, h) = cv2.boundingRect(c)
	ar = w / float(h)

	# In order to label the contour as a question, region
	# should be sufficiently wide, sufficiently tall, and
	# have an aspect ratio approximately equal to 1
	if 70 >= w >= 30 and 70 >= h >= 30 and ar >= 0.8 and ar <= 1.2:
		questionCnts.append(c)

def x_cord_contour(contours):
    # Returns the X cordinate for the contour centroid
    if cv2.contourArea(contours) > 10:
        M = cv2.moments(contours)
        return (int(M['m10']/M['m00']))
    else:
        pass

# Sort the question contours top-to-bottom, then initialize
# the total number of correct answers
questionCnts = contours.sort_contours(questionCnts, method="top-to-bottom")[0]
correct = 0
correct_answer_list = Collect_Data()

# Create a counter for right answers
a = 0

# Each question has 4 possible answers, to loop over the
# question in batches of 16
for (q, i) in enumerate(np.arange(0, len(questionCnts), 16)):
	# Sort the contours for the current question from
	# left to right, then initialize the index of the bubbled answers
    cnts = questionCnts[i:(i + 16)]
    contours_left_to_right = sorted(cnts, key = x_cord_contour, reverse = False)
    j = 0
    # Loop over the contours
    for n in range(4):
        cnts_4 = contours_left_to_right[j:j+4]
        j += 4
        bubbled = None
        for (k, l) in enumerate(cnts_4):
            mask = np.zeros(thresh.shape, dtype="uint8")
            cv2.drawContours(mask, [l], -1, 255, -1)
            mask = cv2.bitwise_and(thresh, thresh, mask=mask)
            total = cv2.countNonZero(mask)
            if ((bubbled is None) or (total > bubbled[0])):
                bubbled = [total, k]
            if bubbled[0] < 1000:
                bubbled[1] = 'x'
        if bubbled[1] == correct_answer_list[a]:
            if correct_answer_list[a] == 'x':
                pass
            else:
                correct += 1
                cv2.drawContours(image, [cnts_4[correct_answer_list[a]]], -1, (0, 255 , 0), 4)
                cv2.imshow("Test", imutils.resize(image, height=650))
                cv2.waitKey(0)
        else:
            if correct_answer_list[a] == 'x':
                pass
            else:
                cv2.drawContours(image, [cnts_4[correct_answer_list[a]]], -1, (0, 0 , 255), 4)
                cv2.imshow("Test", imutils.resize(image, height=650))
                cv2.waitKey(0)
        a += 1
        if a == len(correct_answer_list):
            no = list(correct_answer_list).count("x")
            num = len(correct_answer_list) - no
            correct = (correct / num)*100
            text = (f'{correct:.2f}') + "%"
            coordinates = (700, 120)
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 2
            color = (0, 0, 255)
            thickness = 2
            image = cv2.putText(image, text, coordinates, font, fontScale, color, thickness, cv2.LINE_AA)
            cv2.imshow("Output", imutils.resize(image, height = 650))
            cv2.imwrite(r"D:\School_Documents\XLA\PROJECT\output.png", imutils.resize(image, height = 650))
            cv2.waitKey(0)
            exit()
        #cv2.drawContours(image, cnts_4, -1, (0, 0 ,255), 4)
        #cv2.imshow("Test", imutils.resize(image, height=650))
        #cv2.waitKey(0)

