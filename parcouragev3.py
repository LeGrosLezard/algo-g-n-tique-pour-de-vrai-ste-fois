import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from operation import open_picture
from operation import show_picture
from operation import blanck_picture


def recup_contours(img):

    edges = cv2.Canny(img, 255,200)
    contours, _ = cv2.findContours(edges, R, P)

    for cnts in contours:
        cv2.drawContours(blanck, [cnts], -1, (255,255,255), 1)
        #cv2.fillPoly(blanck, pts =[cnts], color=(255, 255, 255))
        (x, y, w, h) = cv2.boundingRect(cnts)

    return blanck



R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE


img = open_picture('images/lign_v1.jpg')
copy = img.copy()
blanck = blanck_picture(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blanck = recup_contours(img)
blanck = cv2.cvtColor(blanck, cv2.COLOR_BGR2GRAY)



pointsx = []
pointsy = []

for y in range(blanck.shape[1]):
    for x in range(blanck.shape[0]):

        if blanck[x ,y] == 255:
            pointsx.append([x, y])
            pointsy.append(y)
        
x = pointsx[0][0]
y = pointsx[0][1]


copy[x, y] = 0, 0, 255



def deja(liste, x, y):

    for i in liste:
        if i[0] == x and i[1] == y:
            return True

    return False


historique = []

t = 0
while True:


    listex = [x + 1, x - 1, x,    x]
    listey = [y,     y,     y+1,  y - 1]

    histo = []
    bas = False; droite = False;
    for i in range(len(listex)):
        if blanck[listex[i], listey[i]] == 255:

            print(i)
            if i == 0:
                x += 1
                copy[x, y] = 0, 255, 0
                histo.append(0)

            if i == 2:
                y += 1
                copy[x, y] = 255, 0, 0
                histo.append(2)

            if i == 1:
                pass
                #x-=1                


    print("")

    


    copy1 = copy.copy()
    cv2.imwrite("ici.png", copy1)
    cv2.imwrite("iciblanck.png", blanck)
    copy1 = cv2.resize(copy1, (800, 800))
    show_picture("copy1", copy1, 0, "")
























