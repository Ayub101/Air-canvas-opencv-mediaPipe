import cv2 as cv
import numpy as np

class Pen:
    def __init__(self):
        self.lower = np.array([90,100,100])
        self.upper = np.array([102,255,255])
        self.kernel = np.ones((5,5),np.uint8)

    def detect_pen(self,frame):  
        self.frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        mask = cv.inRange(self.frame,self.lower,self.upper)
        mask = cv.bitwise_and(self.frame,self.frame,mask=mask)
        # Erosion Eats away the white part while dilation expands it.
        mask = cv.erode(mask,self.kernel,iterations = 1)
        mask = cv.dilate(mask,self.kernel,iterations = 2)
        mask = cv.cvtColor(mask,cv.COLOR_HSV2BGR)
        gray = cv.cvtColor(mask,cv.COLOR_BGR2GRAY)
        contours, hierarchy = cv.findContours(gray,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
        if contours and cv.contourArea(max(contours,key = cv.contourArea)) > 300:
            max_area = max(contours,key = cv.contourArea)
            x,y,w,h = cv.boundingRect(max_area)
            print(x,y,h,w)
            cv.rectangle(self.frame,(x,y),(x+w,y+h),(0,255,255),2)         
        self.frame = cv.cvtColor(self.frame,cv.COLOR_HSV2BGR)
        return (cv.flip(mask,1),cv.flip(self.frame,1))

cam = cv.VideoCapture(1)
# Creating A 5x5 kernel for morphological operations

if cam.isOpened():
    while True:
        _ ,frame = cam.read()
        pen = Pen()
        frame = pen.detect_pen(frame)
        sta = np.hstack(frame)
        cv.imshow('d',cv.resize(sta,None,fx=0.6,fy=0.6))
        if cv.waitKey(5) & 0xFF == 27:
            break


