import cv2 as cv
import numpy as np


snew_list,sold_list=0,0
mnew_list,mold_list=0,0
lnew_list,lold_list=0,0

videoCapture = cv.VideoCapture('Videos/videoplayback.mp4')                         #takes the video


while True:
    ret, frame = videoCapture.read()                                               #frames from the video
    if not ret: break

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)                              #converting to single channel for houghcircles
    blurFrame = cv.GaussianBlur(grayFrame ,(1,1),0)                                #blur a bit to ease out the edges
    cv.imshow('Blur',blurFrame)

    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 20, param1=50, param2=40, minRadius=10, maxRadius=40)  #finds the circles in each frame

    if circles is not None:                                                        # part to count the number of pipes
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
                        if l>22 and l<28:
                            mnew_list+=1
                            if mnew_list > mold_list:
                                mold_list = mnew_list
                        if l>30 and l<40:
                            lnew_list+=1
                            if lnew_list > lold_list:
                                lold_list = lnew_list
                

        circles = np.uint16(np.around(circles)) 
        for i in circles[0,:]:
            cv.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)                          # displays the outer part(ring) of the detected circle
            cv.circle(frame,(i[0],i[1]),2,(0,255,0),2)                             # displays the center of the detected circle
            
    cv.putText(frame, "Small Pipes %d"%sold_list,(10,30), cv.FONT_HERSHEY_TRIPLEX, 1.0, (105,105,105),1)           #prints the updated value of number of pipes
    cv.putText(frame, "Mediam Pipes %d"%mold_list,(300,30), cv.FONT_HERSHEY_TRIPLEX, 1.0, (105,105,105),1)
    cv.putText(frame, "Large Pipes %d"%lold_list,(10,100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (105,105,105),1)
    cv.imshow("Circle Detection", frame)                                                                           #shows the final window with the detected circles

 
    if cv.waitKey(1) & 0xFF == ord('q'): break
print("The number of small pipes is", sold_list)                              # prints finally to the cmd line just as an extra precaution
print("The number of medium pipes is", mold_list) 
print("The number of large pipes is", lold_list)    
videoCapture.release()
cv.destroyAllWindows()

