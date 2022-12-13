import cv2 as cv
import numpy as np

snew_list,sold_list=0,0
mnew_list,mold_list=0,0
lnew_list,lold_list=0,0

videoCapture = cv.VideoCapture('Videos/videoplayback.mp4')


while True:
    ret, frame = videoCapture.read()
    if not ret: break

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurFrame = cv.GaussianBlur(grayFrame ,(1,1),0)
    cv.imshow('Blur',blurFrame)

    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 20, param1=50, param2=40, minRadius=10, maxRadius=40)

    if circles is not None:
        for k in circles:
            snew_list =0
            mnew_list =0
            lnew_list =0
            for j in k:
                for l in j:

                    if l<100:
                        if l>12 and l<20:
                            snew_list+=1
                            if snew_list > sold_list:
                                sold_list = snew_list
                        if l>20 and l<30:
                            mnew_list+=1
                            if mnew_list > mold_list:
                                mold_list = mnew_list
                        if l>30 and l<40:
                            lnew_list+=1
                            if lnew_list > lold_list:
                                lold_list = lnew_list
                

        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            cv.circle(frame,(i[0],i[1]),2,(0,255,0),2)
            
    
    cv.imshow("Circle Detection", frame)

 
    if cv.waitKey(1) & 0xFF == ord('q'): break
print("The number of small pipes is", sold_list)
print("The number of medium pipes is", mold_list) 
print("The number of large pipes is", lold_list)    
videoCapture.release()
cv.destroyAllWindows()