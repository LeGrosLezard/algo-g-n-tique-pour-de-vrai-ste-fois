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


#cv2.circle(copy, (x, y), 3, (255, 0, 0), 3)

#copy[x, y] = 0, 0, 255
#copy[x+1, y] = 0, 255, 0
#copy[x, y+1] = 255, 0, 0


#on increment le points
i = 1


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



poste = []
copy1 = copy.copy()

lastx = 0
lasty = 0


parcourage = []

while True:

    
    print(poste)

    if poste != []:
        for post in poste:






            if post == 0:
                print("")
                print("poste 0")
                parcourage.append(0)

                try:
                    lign_contour(parcourage)
                    escalier(parcourage)
                    coin(parcourage)
                except:
                    pass
            

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


                show_picture("copy1", copy1, 0, "")









            if post == 1:
                print("")
                print("poste 1")
                parcourage.append(1)

                try:
                    lign_contour(parcourage)
                    escalier(parcourage)
                    coin(parcourage)
                except:
                    pass






                copy1[lastx, lasty] = 255, 0, 0
                print("iciiiiiiiiiiiiiiiiiiiii")
                copy1[lastx - 1, lasty] = 0, 0, 255
                blanck[lastx - 1, lasty] = 255

                cv2.imwrite("ICI.png", copy1)

                
                xu = lastx - 1
                yu = lasty

                eclaireurs = [blanck[xu + 1, yu], blanck[xu - 1, yu], 
                              blanck[xu, yu + 1], blanck[xu, yu - 1],
                              blanck[xu + 1, yu + 1], blanck[xu - 1, yu - 1],
                              blanck[xu + 1, yu - 1], blanck[xu - 1, yu + 1]]

                poste = []



                #Routes
                for nb, eclaireur in enumerate(eclaireurs):
                    if eclaireur == 255:
                        print(eclaireur, nb)

                        if nb == 0:pass
                        elif nb == 1:poste.append(1)
                        elif nb == 2:poste.append(2)
                        elif nb == 3:poste.append(3)
                        elif nb == 4:poste.append(4)
                        elif nb == 5:poste.append(5)
                        elif nb == 6:poste.append(6)
                        elif nb == 7:poste.append(7)


                        lastx = xu
                        lasty = yu


                show_picture("copy1", copy1, 0, "")










            if post == 2:
                print("")
                print("poste 2")
                parcourage.append(2)

                try:
                    lign_contour(parcourage)
                    escalier(parcourage)
                    coin(parcourage)
                except:
                    pass

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
                        elif nb == 2:poste.append(2)
                        elif nb == 3:pass
                        elif nb == 4:poste.append(4)
                        elif nb == 5:poste.append(5)
                        elif nb == 6:poste.append(6)
                        elif nb == 7:poste.append(7)


                        lastx = xd
                        lasty = yd

                #cv2.imwrite("ici.png", copy1)
                show_picture("copy1", copy1, 0, "")









            if post == 3:
                print("")
                print("poste 3")
                parcourage.append(3)


                try:
                    lign_contour(parcourage)
                    escalier(parcourage)
                    coin(parcourage)
                except:
                    pass

                copy1[lastx, lasty - 1] = 0, 0, 255
                blanck[lastx, lasty - 1] = 255

                xt = lastx
                yt = lasty - 1


                eclaireurs = [blanck[xt + 1, yt], blanck[xt - 1, yt], 
                              blanck[xt, yt + 1], blanck[xt, yt - 1],
                              blanck[xt + 1, yt + 1], blanck[xt - 1, yt - 1],
                              blanck[xt + 1, yt - 1], blanck[xt - 1, yt + 1]]

                poste = []


                #Routes
                for nb, eclaireur in enumerate(eclaireurs):
                    if eclaireur == 255:
                        print(eclaireur, nb)

                        if nb == 0:poste.append(0)
                        elif nb == 1:poste.append(1)
                        elif nb == 2:pass
                        elif nb == 3:poste.append(3)
                        elif nb == 4:poste.append(4)
                        elif nb == 5:poste.append(5)
                        elif nb == 6:poste.append(6)
                        elif nb == 7:poste.append(7)


                        lastx = xt
                        lasty = yt


                show_picture("copy1", copy1, 0, "")










            if post == 6:
                print("")
                print("poste 6")
                parcourage.append(6)

                try:
                    lign_contour(parcourage)
                    escalier(parcourage)
                    coin(parcourage)
                except:
                    pass


                copy1[lastx - 1, lasty - 1] = 0, 0, 255
                blanck[lastx - 1, lasty - 1] = 255


                xs = lastx - 1
                ys = lasty - 1
                
                eclaireurs = [blanck[xs + 1, ys], blanck[xs - 1, y], 
                              blanck[xs, ys + 1], blanck[xs, y - 1],
                              blanck[xs + 1, ys + 1], blanck[xs - 1, ys - 1],
                              blanck[xs + 1, ys - 1], blanck[xs - 1, ys + 1]]

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


                        lastx = xs
                        lasty = ys

                cv2.imwrite("ici.png", copy1)
                show_picture("copy1", copy1, 0, "")












##            if post == 7:
##                print("poste 7")
##
##                copy1[lastx - 1, lasty + 1] = 0, 0, 255
##                blanck[lastx - 1, lasty + 1] = 255
##
##                xs = lastx - 1
##                ys = lasty + 1
##
##
##                eclaireurs = [blanck[xse + 1, yse], blanck[xse - 1, yse], 
##                              blanck[xse, yse + 1], blanck[xse, yse - 1],
##                              blanck[xse + 1, yse + 1], blanck[xse - 1, yse - 1],
##                              blanck[xse + 1, yse - 1], blanck[xse - 1, yse + 1]]
##
##                poste = []
##
##
##                #Routes
##                for nb, eclaireur in enumerate(eclaireurs):
##                    if eclaireur == 255:
##                        print(eclaireur, nb)
##
##                        if nb == 0:poste.append(0)
##                        elif nb == 1:poste.append(1)
##                        elif nb == 2:poste.append(2)
##                        elif nb == 3:poste.append(3)
##                        elif nb == 4:poste.append(4)
##                        elif nb == 5:poste.append(5)
##                        elif nb == 6:poste.append(6)
##                        elif nb == 7:poste.append(7)
##
##                        lastx = xse
##                        lasty = yse
##
##
##                show_picture("copy1", copy1, 0, "")












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

        


