import cv2
import numpy as np

filnavn = "1.jpg"



cap = cv2.VideoCapture(1) #cv2.imread(filnavn, 0) #load img as grayscale


src = cv2.imread(filnavn) #cap.read()
img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(img, 100, 200)
minLineLength = 1000
maxLineGap = 0

lines = cv2.HoughLinesP(edges,1,np.pi/180,10, minLineLength=10, maxLineGap = 10)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(src,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('houghlines3.jpg',src)


while (not(cv2.waitKey(1) & 0xFF==ord('q'))):



    continue

cv2.destroyAllWindows()
cap.release()