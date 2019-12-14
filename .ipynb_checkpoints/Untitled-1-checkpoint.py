import cv2
import numpy as np

img = cv2.imread('p2withK.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
img2,contours,hierarchy = cv2.findContours(thresh,2,1)
print(len(contours))
cnt = contours[0]
print(cnt)
cnt = [[[186.28660182, 294.04927006]],[[186.28660182, 294.04927006]],[[235.53769202,278.71449107]],[[195.80981729,241.21424498]],[[175.87870216,344.04292536]], [[149.33770675, 258.80066193]],[[227.9712003,  327.82339611]],[[139.22468928,309.7414215 ]]]
print(cnt)
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)



cv2.imshow('img',img)

cv2.waitKey(1000)
cv2.destroyAllWindows()
