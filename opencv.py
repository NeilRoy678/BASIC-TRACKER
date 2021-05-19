
import cv2
from matplotlib import pyplot as plt

from matplotlib.animation import FuncAnimation
def video():
    cap = cv2.VideoCapture(0)
    ret,frame1 = cap.read()
    ret,frame2 = cap.read()
    i=0 
    count = 0
    while True:
        diff  = cv2.absdiff(frame1,frame2)
        gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        _,thres = cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
        dialted = cv2.dilate(thres,None,iterations=3)
        c,h = cv2.findContours(dialted,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for contours in c:
            (x,y,w,h) = cv2.boundingRect(contours)  
            if cv2.contourArea(contours) <=700:
                continue
            if cv2.contourArea(contours) >700:

                cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('frame',frame1)
        frame1 = frame2
        ret,frame2 = cap.read()
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
   
    cap.release()
    cv2.destroyAllWindows()

video()