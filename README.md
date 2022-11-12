# Bubble sheet multiple choice scanner and test grader
This is an image processing project.  
The purpose of this project is to create a program which can detect the student answer in a bubble sheet and grade it.

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Algorithm Implementation](#algorithm-implementation)
* [Result](#result)
* [References](#references)

## General Info
The algorithm behind is implemented using Python.
</br>
This project contains 5 files:
* An excel file containing answers. Each worksheet is equivalent to the answers of a problem code. A, B, C, D are referred to as 0, 1, 2, 3 in the file respectively.
* <i>collect_data.py</i> is used to read the excel file and return a list of answers depending on the problem code.
* <i>scan.py</i> is used to scan a photo from which it obtains the sheet in the image and then converts the image to gray scale.
* <i>transform.py</i> contains functions used to transform the sheet to obtain the top-down views.
* <i>test_grader.py</i> is the file used to determine the answer selected by the student and whether that answer is correct or incorrect. From there, we calculate the score of the test.

## Technologies
* Python 3.x
* OpenCV Library 4.x
* Numpy Library 1.x
* Imutils Module 0.x
* Matplotlib Library 3.x
* Pandas Library 1.x

## Algorithm Implementation
For a more exhaustive explanation, please read my report (written in Vietnamese) or the references.

## Result
## Original Test Sheet
<img src="https://github.com/LP2X0X/Multiple-choice-scanner-and-test-grader/blob/main/form.png" alt="Original" width="700"/>

## Input Image

## Output Image

## References
1. https://pyimagesearch.com/2016/10/03/bubble-sheet-multiple-choice-scanner-and-test-grader-using-omr-python-and-opencv/
2. https://pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
3. https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/
