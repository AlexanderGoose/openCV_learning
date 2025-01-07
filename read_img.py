import cv2 as cv

# reads in the img
img = cv.imread('images/cat.jpg')

# displays the img in a new window
cv.imshow('Cat', img)

# waits for a key to be pressed
cv.waitKey(0)
