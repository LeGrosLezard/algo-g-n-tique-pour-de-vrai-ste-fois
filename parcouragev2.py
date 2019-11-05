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


eclaireurs = [blanck[x + 1, y], blanck[x - 1, y], 
              blanck[x, y + 1], blanck[x, y - 1],
              blanck[x + 1, y + 1], blanck[x - 1, y - 1],
              blanck[x + 1, y - 1], blanck[x - 1, y + 1]]


poste = []

lastx = x
lasty = y

copy[x, y]= 0, 0, 255


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


print(poste)
show_picture("blanck", blanck, 0, "")




#POUR LES POINTS APRES LA DETECTION DU PTS NOIR [0, 7]
for i in poste:


    #ON A DES PTS [0 et 7]
    if i == 0:

        a = x + 1; b = y;
        copy[a, b] = 255, 0, 0

        #ON DEFINIT NOS PTS
        listex = [a + 1, a-1, a, a, a+1, a-1, a+1, a-1]
        listey = [b, b, b+1, b-1, b+1, b-1, b-1, b+1]
        avant_poste = []


        t = 0
        while True:

            #ON DOIS RAFRAICHIR LA LISTE
            if t > 0:
                listex = [a + 1, a-1, a, a, a+1, a-1, a+1, a-1]
                listey = [b, b, b+1, b-1, b+1, b-1, b-1, b+1]

            #ON ESSAIS DE VOIR DES DETECTIONS
            for nb in range(len(listex)):
                if blanck[listex[nb], listey[nb]] == 255:
                    if nb == 0:avant_poste.append(0)
                    if nb == 1:pass
                    if nb == 2:pass
                    if nb == 3:pass             
                    if nb == 4:pass
                    if nb == 5:pass
                    if nb == 6:pass
                    if nb == 7:pass

            #POUR LES PTS DANS LES DETECTIONS
            print(avant_poste)
            for avnt in avant_poste:

                if avnt == 0:
                    a+=1

                    copy[a, b] = 255, 0, 0

                    copy1 = copy.copy()
                    copy1 = cv2.resize(copy1, (800, 800))
                    show_picture("copy1", copy1, 0, "")

                    t += 1

            avant_poste = []



