import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Boston', img)

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
blur =  cv.GaussianBlur(img , (3,3), cv.BORDER_DEFAULT)
#increase the kernal size to increase the blur
cv.imshow('Blur' ,blur)

#Edge Cascade
canny = cv.Canny(img, 125,175)#use blur in the source img for less edges
cv.imshow('Canny',canny)

#Dillating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated',dilated)

#Eroding 
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)

#Resized
resized = cv.resize(img ,(500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized1', resized)
resized = cv.resize(img ,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized2', resized)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)


cv.waitKey(0)