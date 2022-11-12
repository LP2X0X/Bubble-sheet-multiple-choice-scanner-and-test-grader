# Bubble sheet multiple choice scanner and test grader
This is an image processing project.  
The purpose of this application is to create a program which can detect the student answer in a bubble sheet and grade it.

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Algorithm Implementation](#algorithm-implementation)
* [References](#references)

## General Info
The algorithm behind it is implemented using Python.

## Technologies
* Python 3.x
* OpenCV Library 4.x
* Numpy Library 1.x
* Imutils Module 0.x
* Matplotlib Library 3.x

## Algorithm Implementation
For keypoints and features detection, the **Scale-Invariant Feature Transform (SIFT)** [1] algorithm is used from the **opencv** package.
</br>

<p align="justify">
Once the <b>keypoints</b> and <b>features descriptors</b> are obtained from a pair of images, <i>brute-force-matching</i> is performed using <b>Euclidean distance</b> as the metric. For each point in one image, two points with <i>lowest</i> Euclidean distance in the other image is obtained using <b>KNN algorithm</b> (indicating the top two matches). The reason we want the top two matches rather than just the top one match is because we need to apply David Lowe’s ratio test for false-positive match pruning.
</br>
</br>
With a list of matched points between two images, the <b>Affine Transformation Matrix</b> can be computed. However, since the images are taken by a camera that move accurately horizontally and vertically, we only need to extract the <b>Translation Matrix</b> from the transformation matrix.
</br>
</br>
Once a translation matrix is obtained, opencv's warp Affine function is used to transform the second image into the perspective of the first. The algorithm therefore is faster and more accurate compare to when we use homography matrix to warp image.
</br>
</br>
</p>

## References
1. https://pyimagesearch.com/2016/10/03/bubble-sheet-multiple-choice-scanner-and-test-grader-using-omr-python-and-opencv/
2. https://pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
3. https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/
