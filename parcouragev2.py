import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from operation import open_picture
from operation import show_picture
from operation import blanck_picture


#Variables
R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE

#Image
img = open_picture('images/lign_v1.jpg')

#New Images
copy = img.copy()
blanck = blanck_picture(img)

def recup_contours(img):

    edges = cv2.Canny(img, 255,200)
    contours, _ = cv2.findContours(edges, R, P)

    for cnts in contours:
        cv2.drawContours(blanck, [cnts], -1, (255,255,255), 1)
        #cv2.fillPoly(blanck, pts =[cnts], color=(255, 255, 255))
        (x, y, w, h) = cv2.boundingRect(cnts)

    return blanck





#Filter
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blanck = recup_contours(img)
blanck = cv2.cvtColor(blanck, cv2.COLOR_BGR2GRAY)
#show_picture("blanck", blanck, 0, "")


pts1 = 0; pts2 = 0;
pointsx = []; pointsy = [];


for y in range(blanck.shape[1]):
    for x in range(blanck.shape[0]):

        if blanck[x ,y] == 255:
            pointsx.append([x, y])
            pointsy.append(y)
        
x = pointsx[0][0]
y = pointsx[0][1]







eclaireurs = [blanck[x + 1, y], blanck[x - 1, y], 
              blanck[x, y + 1], blanck[x, y - 1],
              blanck[x + 1, y + 1], blanck[x - 1, y - 1],
              blanck[x + 1, y - 1], blanck[x - 1, y + 1]]


poste = []

lastx = x
lasty = y


for nb, eclaireur in enumerate(eclaireurs):
    if eclaireur == 255:
        if nb == 0:poste.append(0)
        elif nb == 1:poste.append(1)
        elif nb == 2:poste.append(2)
        elif nb == 3:poste.append(3)
        elif nb == 4:poste.append(4)
        elif nb == 5:poste.append(5)
        elif nb == 6:poste.append(6)
        elif nb == 7:poste.append(7)


show_picture("blanck", blanck, 0, "")


print(poste, x, y)
for post in poste:

    if post == 0:

        avant_poste = []

        
        print(" \nPOSTE  0")

        x = x + 1
        y = y


        copy[x, y] = 255, 0, 0
        cv2.imwrite("oki.png", copy)


        while True:
            print(x, y, "\n")

            listex = [x + 1, x-1, x, x, x+1, x-1, x+1, x-1]
            listey = [y, y, y+1, y-1, y+1, y-1, y-1, y+1]

            for i in range(len(listex)):
                if blanck[listex[i], listey[i]] == 255:
                    if i == 0:avant_poste.append(0)
                    elif i == 1:avant_poste.append(1)
                    elif i == 2:avant_poste.append(2)
                    elif i == 3:avant_poste.append(3)
                    elif i == 4:avant_poste.append(4)
                    elif i == 5:avant_poste.append(5)
                    elif i == 6:avant_poste.append(6)
                    elif i == 7:avant_poste.append(7)

            print(avant_poste, x, y)
            show_picture("blanck", blanck, 0, "")




##eclaireurs = [blanck[x + 1, y], blanck[x - 1, y], 
##              blanck[x, y + 1], blanck[x, y - 1],
##              blanck[x + 1, y + 1], blanck[x - 1, y - 1],
##              blanck[x + 1, y - 1], blanck[x - 1, y + 1]]












    if post == 1:
        x = x - 1
        y = y
        while True:
            pass

    if post == 2:
        x = x
        y = y + 1
        while True:
            pass

    if post == 3:
        x = x
        y = y - 1
        while True:
            pass

    if post == 4:
        x = x + 1
        y = y + 1

    if post == 5:
        x = x - 1
        y = y - 1
        while True:
            pass

    if post == 6:
        x = x + 1
        y = y - 1
        while True:
            pass

    if post == 7:
        x = x - 1
        y = y + 1
        while True:
            pass












