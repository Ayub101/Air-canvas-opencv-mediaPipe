import cv2 as cv
import HandMotion as hm
htm = hm.handTraking()

cam = cv.VideoCapture(0,cv.CAP_DSHOW)

if cam.isOpened():
    while True:
        ret , frame = cam.read()
        if not ret:
            break
        if frame is not None:
            frame =cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame.flags.writeable = True
            frame = htm.trakHands(cam=cam,frame=frame)
            frame =cv.cvtColor(frame, cv.COLOR_RGB2BGR)
            cv.imshow("hand movement",frame)
        #cv22.imshow("frame",cv22.flip(frame,1))
        if cv.waitKey(5) & 0xFF == 27:
            break

cam.release()
cv.destroyAllWindows()