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

xz = pointsx[0][0]
yz = pointsx[0][1]

xu = pointsx[0][0]
yu = pointsx[0][1]


xd = pointsx[0][0]
yd = pointsx[0][1]

xt = pointsx[0][0]
yt = pointsx[0][1]


xq = pointsx[0][0]
yq = pointsx[0][1]

xc = pointsx[0][0]
yc = pointsx[0][1]

xs = pointsx[0][0]
ys = pointsx[0][1]

xse = pointsx[0][0]
yse = pointsx[0][1]
#cv2.circle(copy, (x, y), 3, (255, 0, 0), 3)

#copy[x, y] = 0, 0, 255
#copy[x+1, y] = 0, 255, 0
#copy[x, y+1] = 255, 0, 0


#on increment le points
i = 1


#--------------------

"""
éclaireur -> avant poste - > 'constructeur de route' -> eclaireur

"""

#--------------------



poste = []
copy1 = copy.copy()
copy_zero = copy.copy()
copy_un = copy.copy()
copy_deux = copy.copy()
copy_trois = copy.copy()
copy_quattre = copy.copy()
copy_cinq = copy.copy()
copy_six = copy.copy()
copy_sept = copy.copy()


lastx = 0
lasty = 0

while True:
    #copy1 = copy.copy()
    

    print(poste)

    if poste != []:
        for post in poste:






            if post == 0:
                print("")
                print("poste 0")


                copy1[lastx + 1, lasty] = 0, 0, 255
                blanck[lastx + 1, lasty] = 255


                xz = lastx + 1
                yz = lasty
                eclaireurs = [blanck[xz + 1, yz], blanck[xz - 1, yz], 
                              blanck[xz, yz + 1], blanck[xz, yz - 1],
                              blanck[xz + 1, yz + 1], blanck[xz - 1, yz - 1],
                              blanck[xz + 1, yz - 1], blanck[xz - 1, yz + 1]]

                poste = []


                #Routes
                for nb, eclaireur in enumerate(eclaireurs):
                    if eclaireur == 255:
                        print(eclaireur, nb)

                        if nb == 0:
                            poste.append(0)
                        elif nb == 1:pass
                        elif nb == 2:
                            poste.append(2)
                        elif nb == 3:poste.append(3)
                        elif nb == 4:
                            poste.append(4)
                        elif nb == 5:
                            poste.append(5)
                        elif nb == 6:
                            poste.append(6)
                        elif nb == 7:
                            poste.append(7)


                        lastx = xz
                        lasty = yz

                #et a leur tour d'envoyer des éclaireurs
##                copy1[xz + 1, yz] = 0, 0, 255
##                copy1[xz - 1, yz] = 0, 0, 255
##                copy1[xz, yz + 1] = 0, 0, 255
##                copy1[xz, yz - 1] = 0, 0, 255
##                copy1[xz + 1, yz + 1] = 0, 0, 255
##                copy1[xz - 1, yz - 1] = 0, 0, 255
##                copy1[xz + 1, yz - 1] = 0, 0, 255
##                copy1[xz - 1, yz + 1] = 0, 0, 255


                show_picture("copy1", copy1, 0, "")
                cv2.imwrite("coco.png",copy1)
                cv2.imwrite("dza444dzadza.png",blanck)






            if post == 2:
                print("")
                print("poste 2")

                copy1[lastx, lasty+1] = 0, 0, 255
                blanck[lastx, lasty+1] = 255

                xd = lastx
                yd = lasty + 1


                eclaireurs = [blanck[xd + 1, yd], blanck[xd - 1, yd], 
                              blanck[xd, yd + 1], blanck[xd, yd - 1],
                              blanck[xd + 1, yd + 1], blanck[xd - 1, yd - 1],
                              blanck[xd + 1, yd - 1], blanck[xd - 1, yd + 1]]

                poste = []



                #Routes
                for nb, eclaireur in enumerate(eclaireurs):
                    if eclaireur == 255:
                        print(eclaireur, nb)

                        if nb == 0:poste.append(0)
                        elif nb == 1:poste.append(1)
                        elif nb == 2:
                            poste.append(2)
                        elif nb == 3:pass
                        elif nb == 4:
                            poste.append(4)
                        elif nb == 5:
                            poste.append(5)
                        elif nb == 6:
                            poste.append(6)
                        elif nb == 7:
                            poste.append(7)


                        lastx = xd
                        lasty = yd

                cv2.imwrite("coco.png",copy1)
                cv2.imwrite("dzadzadza.png",blanck)
                show_picture("copy1", copy1, 0, "")














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

                if nb == 0:
                    poste.append(0)

                elif nb == 1:
                    poste.append(1)

                elif nb == 2:
                    poste.append(2)

                elif nb == 3:
                    poste.append(3)
                    
                elif nb == 4:
                    poste.append(4)

                elif nb == 5:
                    poste.append(5)

                elif nb == 6:
                    poste.append(6)
 
                elif nb == 7:
                    poste.append(7)



        




        

        #show_picture("copy1", copy1, 0, "")

        







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



























