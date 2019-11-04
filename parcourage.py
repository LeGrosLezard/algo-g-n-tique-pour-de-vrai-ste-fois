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
while True:
    #copy1 = copy.copy()
    

    print(poste, x, y, i)

    if poste != []:
        for post in poste:






            if post == 0:
                print("poste 0")

                
                xz = xz+1

                eclaireurs = [blanck[xz + 1, yz], blanck[xz - 1, yz], 
                              blanck[xz, yz + 1], blanck[xz, yz - 1],
                              blanck[xz + 1, yz + 1], blanck[xz - 1, yz - 1],
                              blanck[xz + 1, yz - 1], blanck[xz - 1, yz + 1]]

                poste = []

                #et a leur tour d'envoyer des éclaireurs
                copy_zero[xz + 1, yz] = 0, 0, 255
                copy_zero[xz - 1, yz] = 0, 0, 255
                copy_zero[xz, yz + 1] = 0, 0, 255
                copy_zero[xz, yz - 1] = 0, 0, 255
                copy_zero[xz + 1, yz + 1] = 0, 0, 255
                copy_zero[xz - 1, yz - 1] = 0, 0, 255
                copy_zero[xz + 1, yz - 1] = 0, 0, 255
                copy_zero[xz - 1, yz + 1] = 0, 0, 255





                #Routes
                for nb, eclaireur in enumerate(eclaireurs):
                    if eclaireur == 255:
                        print(eclaireur, nb)

                        if nb == 0:poste.append(0)
                        elif nb == 1:poste.append(1)
                        elif nb == 2:poste.append(2)
                        elif nb == 3:poste.append(3)
                        elif nb == 4:
                            blanck[xz+1,yz] = 255
                            poste.append(4)
                        elif nb == 5:
                            blanck[xz-1,yz] = 255
                            poste.append(5)
                        elif nb == 6:
                            blanck[xz+1,yz] = 255
                            poste.append(6)
                        elif nb == 7:
                            blanck[xz-1, yz] = 255
                            poste.append(7)





                show_picture("copy_zero", copy_zero, 0, "")








            if post == 1:
                print("poste 1")


                xu = xu-1
                yu = yu
                
                eclaireurs = [blanck[xu + 1, yu], blanck[xu - 1, yu], 
                              blanck[xu, yu + 1], blanck[xu, yu - 1],
                              blanck[xu + 1, yu + 1], blanck[xu - 1, yu - 1],
                              blanck[xu + 1, yu - 1], blanck[xu - 1, yu + 1]]

                poste = []

                #et a leur tour d'envoyer des éclaireurs
                copy_un[xu + 1, yu] = 0, 0, 255
                copy_un[xu - 1, yu] = 0, 0, 255
                copy_un[xu, yu + 1] = 0, 0, 255
                copy_un[xu, yu - 1] = 0, 0, 255
                copy_un[xu + 1, yu + 1] = 0, 0, 255
                copy_un[xu - 1, yu - 1] = 0, 0, 255
                copy_un[xu + 1, yu - 1] = 0, 0, 255
                copy_un[xu - 1, yu + 1] = 0, 0, 255



                #Routes
                for nb, eclaireur in enumerate(eclaireurs):
                    if eclaireur == 255:
                        print(eclaireur, nb)

                        if nb == 0:poste.append(0)
                        elif nb == 1:poste.append(1)
                        elif nb == 2:poste.append(2)
                        elif nb == 3:poste.append(3)
                        elif nb == 4:
                            blanck[xu+1,yu] = 255
                            poste.append(4)
                        elif nb == 5:
                            blanck[xu-1,yu] = 255
                            poste.append(5)
                        elif nb == 6:
                            blanck[xu+1,yu] = 255
                            poste.append(6)
                        elif nb == 7:
                            blanck[xu-1, yu] = 255
                            poste.append(7)





                show_picture("copy_un", copy_un, 0, "")











            if post == 2:
                print("poste 2")

                xd = xd
                yd = yd+1
                
                eclaireurs = [blanck[xd + 1, yd], blanck[xd - 1, yd], 
                              blanck[xd, yd + 1], blanck[xd, yd - 1],
                              blanck[xd + 1, yd + 1], blanck[xd - 1, yd - 1],
                              blanck[xd + 1, yd - 1], blanck[xd - 1, yd + 1]]

                poste = []

                #et a leur tour d'envoyer des éclaireurs
                copy_deux[xd + 1, yd] = 0, 0, 255
                copy_deux[xd - 1, yd] = 0, 0, 255
                copy_deux[xd, yd + 1] = 0, 0, 255
                copy_deux[xd, yd - 1] = 0, 0, 255
                copy_deux[xd + 1, yd + 1] = 0, 0, 255
                copy_deux[xd - 1, yd - 1] = 0, 0, 255
                copy_deux[xd + 1, yd - 1] = 0, 0, 255
                copy_deux[xd - 1, yd + 1] = 0, 0, 255



                #Routes
                for nb, eclaireur in enumerate(eclaireurs):
                    if eclaireur == 255:
                        print(eclaireur, nb)

                        if nb == 0:poste.append(0)
                        elif nb == 1:poste.append(1)
                        elif nb == 2:poste.append(2)
                        elif nb == 3:poste.append(3)
                        elif nb == 4:
                            blanck[xd+1,yd] = 255
                            poste.append(4)
                        elif nb == 5:
                            blanck[xd-1,yd] = 255
                            poste.append(5)
                        elif nb == 6:
                            blanck[xd+1,yd] = 255
                            poste.append(6)
                        elif nb == 7:
                            blanck[xd-1, yd] = 255
                            poste.append(7)





                show_picture("copy_deux", copy_deux, 0, "")







            if post == 3:
                print("poste 3")

                xt = xt
                yt = yt-1
                
                eclaireurs = [blanck[xt + 1, yt], blanck[xt - 1, yt], 
                              blanck[xt, yt + 1], blanck[xt, yt - 1],
                              blanck[xt + 1, yt + 1], blanck[xt - 1, yt - 1],
                              blanck[xt + 1, yt - 1], blanck[xt - 1, yt + 1]]

                poste = []

                #et a leur tour d'envoyer des éclaireurs
                copy_trois[xt + 1, yt] = 0, 0, 255
                copy_trois[xt - 1, yt] = 0, 0, 255
                copy_trois[xt, yt + 1] = 0, 0, 255
                copy_trois[xt, yt - 1] = 0, 0, 255
                copy_trois[xt + 1, yt + 1] = 0, 0, 255
                copy_trois[xt - 1, yt - 1] = 0, 0, 255
                copy_trois[xt + 1, yt - 1] = 0, 0, 255
                copy_trois[xt - 1, yt + 1] = 0, 0, 255



                #Routes
                for nb, eclaireur in enumerate(eclaireurs):
                    if eclaireur == 255:
                        print(eclaireur, nb)

                        if nb == 0:poste.append(0)
                        elif nb == 1:poste.append(1)
                        elif nb == 2:poste.append(2)
                        elif nb == 3:poste.append(3)
                        elif nb == 4:
                            blanck[xt+1,yt] = 255
                            poste.append(4)
                        elif nb == 5:
                            blanck[xt-1,yt] = 255
                            poste.append(5)
                        elif nb == 6:
                            blanck[xt+1,yt] = 255
                            poste.append(6)
                        elif nb == 7:
                            blanck[xt-1, yt] = 255
                            poste.append(7)





                show_picture("copy_trois", copy_trois, 0, "")






            if post == 4:
                print("poste 4")


                xq = xq + 1
                yq = yq + 1
  
                eclaireurs = [blanck[xq + 1, yq], blanck[xq - 1, yq], 
                              blanck[xq, yq + 1], blanck[xq, yq - 1],
                              blanck[xq + 1, yq + 1], blanck[xq - 1, yq - 1],
                              blanck[xq + 1, yq - 1], blanck[xq - 1, yq + 1]]

                poste = []

                #et a leur tour d'envoyer des éclaireurs
                copy_quattre[xq + 1, yq] = 0, 0, 255
                copy_quattre[xq - 1, yq] = 0, 0, 255
                copy_quattre[xq, yq + 1] = 0, 0, 255
                copy_quattre[xq, yq - 1] = 0, 0, 255
                copy_quattre[xq + 1, yq + 1] = 0, 0, 255
                copy_quattre[xq - 1, yq - 1] = 0, 0, 255
                copy_quattre[xq + 1, yq - 1] = 0, 0, 255
                copy_quattre[xq - 1, yq + 1] = 0, 0, 255



                #Routes
                for nb, eclaireur in enumerate(eclaireurs):
                    if eclaireur == 255:
                        print(eclaireur, nb)

                        if nb == 0:poste.append(0)
                        elif nb == 1:poste.append(1)
                        elif nb == 2:poste.append(2)
                        elif nb == 3:poste.append(3)
                        elif nb == 4:
                            blanck[xq+1,yq] = 255
                            poste.append(4)
                        elif nb == 5:
                            blanck[xq-1,yq] = 255
                            poste.append(5)
                        elif nb == 6:
                            blanck[xq+1,yq] = 255
                            poste.append(6)
                        elif nb == 7:
                            blanck[xq-1, yq] = 255
                            poste.append(7)





                show_picture("copy_quattre", copy_quattre, 0, "")







            if post == 5:
                print("poste 5")

                xc = xc + 1
                yc = yc + 1
                
                eclaireurs = [blanck[xc + 1, yc], blanck[xc - 1, yc], 
                              blanck[xc, yc + 1], blanck[xc, yc - 1],
                              blanck[xc + 1, yc + 1], blanck[xc - 1, yc - 1],
                              blanck[xc + 1, yc - 1], blanck[xc - 1, yc + 1]]

                poste = []

                #et a leur tour d'envoyer des éclaireurs
                copy_cinq[xc + 1, yc] = 0, 0, 255
                copy_cinq[xc - 1, yc] = 0, 0, 255
                copy_cinq[xc, yc + 1] = 0, 0, 255
                copy_cinq[xc, yc - 1] = 0, 0, 255
                copy_cinq[xc + 1, yc + 1] = 0, 0, 255
                copy_cinq[xc - 1, yc - 1] = 0, 0, 255
                copy_cinq[xc + 1, yc - 1] = 0, 0, 255
                copy_cinq[xc - 1, yc + 1] = 0, 0, 255



                #Routes
                for nb, eclaireur in enumerate(eclaireurs):
                    if eclaireur == 255:
                        print(eclaireur, nb)

                        if nb == 0:poste.append(0)
                        elif nb == 1:poste.append(1)
                        elif nb == 2:poste.append(2)
                        elif nb == 3:poste.append(3)
                        elif nb == 4:
                            blanck[xc+1,yc] = 255
                            poste.append(4)
                        elif nb == 5:
                            blanck[xc-1,yc] = 255
                            poste.append(5)
                        elif nb == 6:
                            blanck[xc+1,yc] = 255
                            poste.append(6)
                        elif nb == 7:
                            blanck[xc-1, yc] = 255
                            poste.append(7)





                show_picture("copy_cinq", copy_cinq, 0, "")












            if post == 6:
                print("poste 6")


                xs = xs - 1
                ys = ys - 1
                
                eclaireurs = [blanck[xs + 1, ys], blanck[xs - 1, y], 
                              blanck[xs, ys + 1], blanck[xs, y - 1],
                              blanck[xs + 1, ys + 1], blanck[xs - 1, ys - 1],
                              blanck[xs + 1, ys - 1], blanck[xs - 1, ys + 1]]

                poste = []

                #et a leur tour d'envoyer des éclaireurs
                copy_six[xs + 1, ys] = 0, 0, 255
                copy_six[xs - 1, ys] = 0, 0, 255
                copy_six[xs, ys + 1] = 0, 0, 255
                copy_six[xs, ys - 1] = 0, 0, 255
                copy_six[xs + 1, ys + 1] = 0, 0, 255
                copy_six[xs - 1, ys - 1] = 0, 0, 255
                copy_six[xs + 1, ys - 1] = 0, 0, 255
                copy_six[xs - 1, ys + 1] = 0, 0, 255



                #Routes
                for nb, eclaireur in enumerate(eclaireurs):
                    if eclaireur == 255:
                        print(eclaireur, nb)

                        if nb == 0:poste.append(0)
                        elif nb == 1:poste.append(1)
                        elif nb == 2:poste.append(2)
                        elif nb == 3:poste.append(3)
                        elif nb == 4:
                            blanck[xs+1,ys] = 255
                            poste.append(4)
                        elif nb == 5:
                            blanck[xs-1,ys] = 255
                            poste.append(5)
                        elif nb == 6:
                            blanck[xs+1,ys] = 255
                            poste.append(6)
                        elif nb == 7:
                            blanck[xs-1, ys] = 255
                            poste.append(7)





                show_picture("copy_six", copy_six, 0, "")













#copy[x, y] = 0, 0, 255
#copy[x+1, y] = 0, 255, 0
#copy[x, y+1] = 255, 0, 0




            if post == 7:
                print("poste 7")


                xse = xse - 1
                yse = yse + 1
                
                eclaireurs = [blanck[xse + 1, yse], blanck[xse - 1, yse], 
                              blanck[xse, yse + 1], blanck[xse, yse - 1],
                              blanck[xse + 1, yse + 1], blanck[xse - 1, yse - 1],
                              blanck[xse + 1, yse - 1], blanck[xse - 1, yse + 1]]

                poste = []

                #et a leur tour d'envoyer des éclaireurs
                copy_sept[xse + 1, yse] = 0, 0, 255
                copy_sept[xse - 1, yse] = 0, 0, 255
                copy_sept[xse, yse + 1] = 0, 0, 255
                copy_sept[xse, yse - 1] = 0, 0, 255
                copy_sept[xse + 1, yse + 1] = 0, 0, 255
                copy_sept[xse - 1, yse - 1] = 0, 0, 255
                copy_sept[xse + 1, yse - 1] = 0, 0, 255
                copy_sept[xse - 1, yse + 1] = 0, 0, 255


                #Routes
                for nb, eclaireur in enumerate(eclaireurs):
                    if eclaireur == 255:
                        print(eclaireur, nb)

                        if nb == 0:poste.append(0)
                        elif nb == 1:poste.append(1)
                        elif nb == 2:poste.append(2)
                        elif nb == 3:poste.append(3)
                        elif nb == 4:
                            blanck[xse+1,yse] = 255
                            poste.append(4)
                        elif nb == 5:
                            blanck[xse-1,yse] = 255
                            poste.append(5)
                        elif nb == 6:
                            blanck[xse+1,yse] = 255
                            poste.append(6)
                        elif nb == 7:
                            blanck[xse-1, yse] = 255
                            poste.append(7)


                show_picture("copy_sept", copy_sept, 0, "")
















    if poste == []:
        eclaireurs = [blanck[x + i, y], blanck[x - i, y], 
                      blanck[x, y + i], blanck[x, y - i],
                      blanck[x + i, y + i], blanck[x - i, y - i],
                      blanck[x + i, y - i], blanck[x - i, y + i]]

        poste = []

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
                elif nb == 4:
                    blanck[x+1,y] = 255
                    poste.append(4)
                elif nb == 5:
                    blanck[x-1,y] = 255
                    poste.append(5)
                elif nb == 6:
                    blanck[x+1,y] = 255
                    poste.append(6)
                elif nb == 7:
                    blanck[x-1, y] = 255
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



























