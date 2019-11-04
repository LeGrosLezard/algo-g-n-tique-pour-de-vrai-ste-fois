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



def lign_contour(parcourage):
    if parcourage[-2] == parcourage[-1]:
        print("lign")
        print(parcourage)
        print("")

def escalier(parcourage):
    if parcourage[-4] == parcourage[-3] and\
       parcourage[-2] == 1 and parcourage[-1] == 1 and\
       parcourage[-3] != parcourage[-2]:
        print("escalier descendant")
        print(parcourage)
        print("")


    if parcourage[-4] == parcourage[-3] and\
       parcourage[-2] == 0 and parcourage[-1] == 0 and\
       parcourage[-3] != parcourage[-2]:
        print("escalier qui monte")
        print(parcourage)
        print("")


def coin(parcourage):
    if parcourage[-3] == parcourage[-2] and\
        parcourage[-1] == 0 and\
        parcourage[-2] != 0:
        print("coin gauche")
        print(parcourage)
        print("")

    if parcourage[-3] == parcourage[-2] and\
        parcourage[-1] == 1 and\
        parcourage[-2] != 1:
        print("coin droit")
        print(parcourage)
        print("")




def road(copy, blanck, a, b, lastx, lasty, delete, parcourage):

    try:
        lign_contour(parcourage)
        escalier(parcourage)
        coin(parcourage)
    except:
        pass


    copy1[lastx + a, lasty + b] = 0, 0, 255
    blanck[lastx + a, lasty + b] = 255

    x = lastx + a
    y = lasty + b

    eclaireurs = [blanck[x + 1, y], blanck[x - 1, y], 
                  blanck[x, y + 1], blanck[x, y - 1],
                  blanck[x + 1, y + 1], blanck[x - 1, y - 1],
                  blanck[x + 1, y - 1], blanck[x - 1, y + 1]]

    poste = []
    #Routes
    for nb, eclaireur in enumerate(eclaireurs):
        if eclaireur == 255:
            print(eclaireur, nb)

            if nb == 0:poste.append(0)
            elif nb == 1:poste.append(1)
            elif nb == 2:poste.append(2)
            elif nb == 3:poste.append(3)
            elif nb == 4:poste.append(4)
            elif nb == 5:poste.append(5)
            elif nb == 6:poste.append(6)
            elif nb == 7:poste.append(7)


    for i in poste:
        if i == delete:
            poste.remove(i)


    lastx = x
    lasty = y

    show_picture("copy1", copy1, 0, "")

    return lastx, lasty, poste





poste = []
copy1 = copy.copy()

lastx = 0
lasty = 0

i = 1


parcourage = []

while True:

    print(poste)

    if poste != []:
        for post in poste:



            if post == 0:
                print("")
                print("poste 0")
                lastx, lasty, poste = road(copy, blanck, 1, 0, lastx, lasty, 1, parcourage)
                parcourage.append(0)


            if post == 1:
                print("")
                print("poste 1")
                lastx, lasty, poste = road(copy, blanck, -1, 0, lastx, lasty, 0, parcourage)
                parcourage.append(1)


            if post == 2:
                print("")
                print("poste 2")

                lastx, lasty, poste = road(copy, blanck, 0, 1, lastx, lasty, 3, parcourage)
                parcourage.append(2)


            if post == 3:
                print("")
                print("poste 3")
                lastx, lasty, poste = road(copy, blanck, 0, -1, lastx, lasty, 2, parcourage)
                parcourage.append(3)


            if post == 6:
                print("")
                print("poste 6")

                lastx, lasty, poste = road(copy, blanck, -1, -1, lastx, lasty, "", parcourage)
                parcourage.append(6)

 



    if poste == []:
        eclaireurs = [blanck[x + i, y], blanck[x - i, y], 
                      blanck[x, y + i], blanck[x, y - i],
                      blanck[x + i, y + i], blanck[x - i, y - i],
                      blanck[x + i, y - i], blanck[x - i, y + i]]

        poste = []

        #et a leur tour d'envoyer des éclaireurs


        

        lastx = x
        lasty = y


        #Routes
        for nb, eclaireur in enumerate(eclaireurs):
            if eclaireur == 255:
                print(eclaireur, nb)

                if nb == 0:poste.append(0)
                elif nb == 1:poste.append(1)
                elif nb == 2:poste.append(2)
                elif nb == 3:poste.append(3)
                elif nb == 4:poste.append(4)
                elif nb == 5:poste.append(5)
                elif nb == 6:poste.append(6)
                elif nb == 7:poste.append(7)


        #show_picture("copy1", copy1, 0, "")
