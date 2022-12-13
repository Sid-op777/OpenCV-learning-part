import cv2 as cv


img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat', img)




cv.waitKey(0)