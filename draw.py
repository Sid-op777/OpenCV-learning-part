import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

##paint the imagea certain color
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green',blank)

#Draw a rectangle
cv.rectangle(blank, (0,0),(250,250),(0,250,0),thickness=2)
#thickness = cv.FILLED or = -1
#(250,250) can also be written as blank.shape[1]//2, blank.shape[0]//2
cv.imshow('Recatngle',blank)

#Draw a circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
cv.imshow('Circle',blank)

#Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(255,255,255),thickness=3)
cv.imshow('Line',blank)

#Write text
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Text',blank)


cv.waitKey(0)