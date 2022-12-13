import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston',img)

b,g,r, = cv.split(img)
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape)
#.shape gives three values --> height , width , no. of color channels
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)