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



def lign_contour():
    pass








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


#cv2.circle(copy, (x, y), 3, (255, 0, 0), 3)

#copy[x, y] = 0, 0, 255
#copy[x+1, y] = 0, 255, 0
#copy[x, y+1] = 255, 0, 0


i = 1

poste = []
while True:
    copy1 = copy.copy()


    print(poste)
    poste = []

    eclaireurs = [blanck[x + i, y], blanck[x - i, y], 
                  blanck[x, y + i], blanck[x, y - i],
                  blanck[x + i, y + i], blanck[x - i, y - i],
                  blanck[x + i, y - i], blanck[x - i, y + i]]


    #et a leur tour d'envoyer des éclaireurs
    copy1[x + i, y] = 0, 0, 255
    copy1[x - i, y] = 0, 0, 255
    copy1[x, y + i] = 0, 0, 255
    copy1[x, y - i] = 0, 0, 255
    copy1[x + i, y + i] = 0, 0, 255
    copy1[x - i, y - i] = 0, 0, 255
    copy1[x + i, y - i] = 0, 0, 255
    copy1[x - i, y + i] = 0, 0, 255


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
            elif nb == 7:
                blanck[x+1,y] = 255
                poste.append(7)

        else:
            print(eclaireur)

    i += 1






    copy[x, y] = 0, 0, 255
##
##    
##
##    #Lign
##    lign = 0
##    while True:
##        if blanck[x + lign, y] == 0:
##            break
##        else:
##            print(blanck[x + lign, y])
##            copy[x + lign, y] = 0, 0, 255
##            lign += 1
##            show_picture("copy", copy, 0, "")



    show_picture("copy", copy, 0, "")
    show_picture("copy1", copy1, 0, "")




































