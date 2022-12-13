import cv2 as cv

# img = cv.imread("Photos/cat_large.jpg")
# cv.imshow("Cat", img)  # shows the image the parameters are name of the window and the matrix of pixels

#reading videos
capture = cv.VideoCapture('Videos/dog.mp4')
#takes default path parameters as well as int 0,1,2 etc for camera distinction like 0 can be for webcam

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)