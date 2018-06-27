import cv2
import numpy as np
from matplotlib import pyplot as plt
import pickle

brikkeInt = 56


KEYPOINTPATH = "cutwithkeypoint\\"
GRABCUTPATH = "grabcut\\"

f = open("labeles.csv")
g = open("keyptsxy.csv", "w")
tittel = f.readline()
tittel.split(";")

kpxylist = []

def toString(*args):
    
    i = 0
    for arg in args:
        if type(arg)==list:
            for a in arg:
                if i == 0:
                    string = str(a)
                else:
                    string += ";"+str(a)
                i += 1
        elif i == 0:
            string = str(arg)
            i += 1
        else:
            string += ";"+str(arg)
            i += 1
        
    return string

for j in range(brikkeInt):

    info = f.readline()
    info = info[:-1]
    info = info.split(';')
    name = info.pop(0)
    '''
    #xy =np.zeros((8,2), dtype=float)
    src = cv2.imread(GRABCUTPATH+name+".png", -1)
    src = cv2.cvtColor(src, cv2.COLOR_BGRA2BGR)

    '''
    kpxylist.append([])
    kpxylist[j].append(name)
    kp1 = []
    colors = [(0,255,255), (255,0,0), (0,0,255), (0,255,0)]

    for i in range(len(info)):
        pair = info[i].split(',')
        x = int(pair[0][1:])
        y=int(pair[1][:-1])
        kpxylist[j].append(x)
        kpxylist[j].append(y)
        
        kp = cv2.KeyPoint(x,y,1)
        kp1.append(kp)


    for i in range(len(colors)):
        pt1 = kp1[2*i].pt
        pt2 = kp1[2*i+1].pt
        pt1 = (int(pt1[0]), int(pt1[1]))
        pt2 = (int(pt2[0]), int(pt2[1]))
        '''
        if (pt1[0]+pt2[0]+pt1[1]+pt2[1]):
            cv2.line(src, pt1, pt2, colors[i], 3)

        '''
    
    g.write(toString(kpxylist[j])+"\n")

    #cv2.drawKeypoints(src, kp1, src)
    
    

    #cv2.imwrite(KEYPOINTPATH + name + "withK.png", src)

g.close()
f.close()