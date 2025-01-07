import cv2 as cv
import numpy as np 

# creating a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('blank', blank)

## 1. paint the img a color
# blank[:] = 0, 255, 0
# cv.imshow('green', blank)

## paint a portion by passing ranges
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('portion', blank)

## can use the rectangle method!
##             img    start    end        color   thickness
# cv.rectangle(blank, (0,0), (250, 250), (0,255,0), 2)
# cv.imshow('rectangle', blank)

## draw a circle
##          img     center  radius   color   thickness
# cv.circle(blank, (250, 250), 40, (0, 0, 255), 2)
# cv.imshow('circle', blank)

## writing text on an img
## MUST specify a font type, font scale, color, and thickness
cv.putText(blank, 'Hello!', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 1)
cv.imshow('text', blank)

# img = cv.imread('images/cat.jpg')
# cv.imshow('cat', img)
cv.waitKey(0)

# cv.waitKey(5000)  # Closes the window after 5000ms (5 seconds)
# cv.destroyAllWindows()
