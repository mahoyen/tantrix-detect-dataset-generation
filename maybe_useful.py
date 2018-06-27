
''' Grabcut
img = src
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (5,5,140,140)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.savefig(GRABCUTPATH+str(nr)+".png")
plt.show()
'''


''' Polydp and convex hull
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, threshmask = cv2.threshold(gray,100,255,0)
inv_threshmask = cv2.bitwise_not(threshmask)
img2, contours, hiercy =cv2.findContours(inv_threshmask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(gray, contours, -1, (255,255,255), -1)
cnt = contours[0]
polyDPepsilon  = 0.0001*cv2.arcLength(cnt,True)



hull = cv2.convexHull(cnt)
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(src,(x,y),(x+w,y+h),(0,255,0),2)
'''