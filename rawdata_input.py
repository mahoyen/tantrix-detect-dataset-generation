import cv2
import numpy as np
from matplotlib import pyplot as plt

BRIKKEPATH = "brikker_raw\\"
GRABCUTPATH = "grabcut\\"

brikkeInt = 56

x = 815
w = 150
y = 400
h = 150

black_roi = cv2.imread(GRABCUTPATH+"p3.png")[45:45+15,45:45+25]

# We build the alpha channel so that we have transparency on the
# external border of the card
# First, initialize alpha channel fully transparent
# Then fill in the contour to make opaque this zone of the card 

alphamask = cv2.cvtColor(cv2.imread("alphamask.png"), cv2.COLOR_BGR2GRAY)

marg_alphamask = 2 

h_alphamask = 120
w_alphamask = 130

def create_blank(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image

blancimg = create_blank(w,h,(255,255,255))
for i in range(brikkeInt):
    nr = i+1
    filnavn = BRIKKEPATH+"("+str(nr)+").jpg"
    src = cv2.imread(filnavn)
    try:
        if src == None:
            print("Could not find image "+filnavn)
            continue
    except:
        src = src[y:y+h, x:x+w]

        
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        ret, threshmask = cv2.threshold(gray,100,255,0)
        inv_threshmask = cv2.bitwise_not(threshmask)

        img2, contours, hiercy =cv2.findContours(inv_threshmask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(gray, contours, -1, (255,255,255), -1)
        xb,yb,wb,hb = cv2.boundingRect(contours[0])

        gray = gray[yb:yb+h_alphamask,xb:xb+w_alphamask]
        src = src[yb:yb+h_alphamask,xb:xb+w_alphamask]

        alphachannel=np.zeros(src.shape[:2],dtype=np.uint8)

        _,contmask = cv2.threshold(gray,250,255,0)
        inv_contmask = cv2.bitwise_not(contmask)
        


        #np.subtract(contours[0], [xb,yb])
        j = 2
        for pts in contours[0]:
            if j < 23:
                pts[0][0] -= (xb-marg_alphamask) 
                pts[0][1] -= (yb-marg_alphamask)
            else:
                pts[0][0] -= (xb+marg_alphamask-1) 
                pts[0][1] -= (yb+marg_alphamask-1)

            j +=1

        cv2.drawContours(alphachannel, contours, -1, 255, -1)


        alphachannel = cv2.bitwise_and(alphachannel, alphamask)

        src[0:15,22:47] = black_roi
        src=cv2.cvtColor(src,cv2.COLOR_BGR2BGRA)


        src[:,:,3]= alphachannel

        cv2.imwrite(GRABCUTPATH+"p"+str(nr)+".png",src)



cv2.destroyAllWindows()