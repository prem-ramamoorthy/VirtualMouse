import cv2 as cv
import numpy as np 
import handDetection as hd
import time
import autopy

wcam , hcam = 640 , 480 
wscrn , hscrn = autopy.screen.size()
framereducer = 100
smoothening = 2

vid = cv.VideoCapture(0)
vid.set(3,wcam)
vid.set(4,hcam)

detector = hd.handDetection(detectionCon=0.7)
xp , yp = 0, 0
ptime = 0
plocx , plocy = 0, 0
clocx , clocy = 0, 0

while(True) :
    isTrue , frame = vid.read()
    if not isTrue :
        break
    
    frame = detector.findHands(frame )
    lmlist = detector.findposition(frame, draw= False)
    
    cv.rectangle(frame , (framereducer, framereducer) , (wcam - framereducer , hcam - framereducer) , (255,0,255) , 1)
    
    if lmlist :
        x1,y1 = lmlist[8][1:]
        x2,y2 = lmlist[12][1:]
        fingersopen = detector.fingersup()
        
        if fingersopen[1] and fingersopen[2] : 
            x , y = lmlist[8][1] , lmlist[8][2]
            x0 , y0 = lmlist[12][1] , lmlist[12][2]
            distance = int(((x0 - x ) ** 2 + (y0 - y ) ** 2) ** 0.5)
            c1,c2 = (x +x0)//2 , (y +y0)//2
            cv.circle(frame ,(c1,c2) , 10, (255,0,0) , -1)
            cv.line(frame , (x,y) ,(x0,y0) , (255,255,255) , 2)
            cv.circle(frame , (x,y) , (30) , (0,255,0) , -1)
            cv.circle(frame , (x0,y0) , (30) , (0,255,0) , -1)
            if(distance < 40):
                autopy.mouse.click()

        if fingersopen[1] and fingersopen[2] == 0 :
            x3 = np.interp(x1 , (framereducer , wcam - framereducer) , (0, wscrn))
            y3 = np.interp(y1 , (framereducer , hcam - framereducer) , (0, hscrn))
            
            clocx = plocx + (x3 - plocx ) / smoothening
            clocy = plocy + (y3 - plocy ) / smoothening
            
            autopy.mouse.move(wscrn - clocx , plocy)
            cv.circle(frame , (x1,y1) , 10 , (0,0,255) , -1)
            
            plocx , plocy = clocx , clocy
            
            pass
            
    ctime = time.time()
    fps = 1/ (ctime - ptime)
    ptime = ctime
    
    cv.putText(frame , str(int(fps)) , (20 , 20) , cv.FONT_HERSHEY_PLAIN  , 2, (255,0,255) , 1)
    cv.imshow('Video' , frame)
    
    if cv.waitKey(1) & 0xFF == ord('d'):
            break