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



#PREMIERE DETECTION DU PREMIER POINTS NOIR
pts1 = 0; pts2 = 0;
pointsx = []; pointsy = [];

for y in range(blanck.shape[1]):
    for x in range(blanck.shape[0]):

        if blanck[x ,y] == 255:
            pointsx.append([x, y])
            pointsy.append(y)
        
x = pointsx[0][0]
y = pointsx[0][1]


copy[x, y]= 0, 0, 255


def follow(liste):

    if len(liste) >= 1:
        if liste[-1] == 0:
            print("bas")

        elif liste[-1] == 1:
            print("droite")

        elif liste[-1] == 2:
            print("haut")

        print("")


def opposition(liste):

    if len(liste) >= 6:
        liste = liste[-6:]

        nb1=liste[0]; nb2=liste[1];
        c1=0; c2=0;

        for i in liste:
            if i == nb1:c1+=1
            elif i == nb2:c2+=1


        if c1 == c2:
            print("opposition")

def choice(liste):
    pass


deplacement = []
while True:
    listex = [x + 1, x,   x - 1]
    listey = [y,     y+1, y]

    for i in range(len(listex)):
        if blanck[listex[i], listey[i]] == 255:
            if i == 0:
                print("zero", deplacement)
                follow(deplacement)
                opposition(deplacement)
                deplacement.append(0)
                copy[x, y] = 0, 255, 0
                x += 1
                break
 
            elif i == 1:
                print("un", deplacement)
                follow(deplacement)
                opposition(deplacement)
                deplacement.append(1)
                copy[x, y] = 0, 0, 255
                y += 1
                break

            elif i == 2:
                print("deux", deplacement)
                follow(deplacement)
                opposition(deplacement)
                deplacement.append(2)
                copy[x, y] = 255, 0, 0
                x -= 1
                break



    copy1 = copy.copy()
    cv2.imwrite("ici.png", copy1)
    copy1 = cv2.resize(copy1, (800, 800))
    show_picture("copy1", copy1, 0, "")

































