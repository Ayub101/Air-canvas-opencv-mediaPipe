
import cv2 as cv
import numpy as np
import HandMotion as hm
import detect as dt
pen = dt.Pen()
htm = hm.handTraking()
cam = cv.VideoCapture(1,cv.CAP_DSHOW)
if cam.isOpened():
    while True:
        ret , frame = cam.read()
        if not ret:
            break
        if frame is not None:
            
            canvas = pen.write(frame,(0,255,0),3)
            result = htm.trakHands(cam=cam,frame=frame)
            frame = result.get('frame')
            [x,y] = result.get('erase')
            pen.erase(canvas,x,y)
            # if result.get('Coordinates')!=None:
            #     x2,y2 = result.get('Coordinates')[1][0][0],result.get('Coordinates')[1][0][1]
            #     if x1 == 0 and y1 == 0:
            #         canvas = np.zeros_like(frame)
            #         x1,y1 = x2,y2
            #     else:
            #         canvas = cv.line(canvas, (x1,y1),(x2,y2), [255,0,0], 4)
            #         #cv.imshow("canvas",canvas)
            #         x1,y1= x2,y2
            
            frame = cv.add(canvas,frame)
            #frame = np.hstack((frame,canvas))
            #cv.imshow("hand movement",cv.resize(frame,None,fx=0.6,fy=0.6))
            cv.imshow("air canvas",frame)
            #cv.imshow("a",can)
        #cv22.imshow("frame",cv22.flip(frame,1))
        if cv.waitKey(5) & 0xFF == 27:
            break

cam.release()
cv.destroyAllWindows()
#range 3 181 141 to  13 200 190