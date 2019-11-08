#for paths
import os

#Librairy for treating pictures
import cv2
from PIL import Image

import matplotlib.pyplot as plt

#Here numpy generate matrix
import numpy as np

#Show, Open, Create black picture
from operation import open_picture
from operation import show_picture
from operation import blanck_picture
from operation import find_first_points
from operation import incrementation

from drawing import *

from display import displaying
from drawing import *



def display(dico):
    for cle, valeur in dico.items():
        print(cle, valeur)
        print("")
        
#======================================================================================
picture = ['images/blanck/contour0blanck.jpg', 'images/blanck/contour1blanck.jpg',
           'images/blanck/contour2blanck.jpg', 'images/blanck/contour3blanck.jpg',
           'images/blanck/contour4blanck.jpg', 'images/blanck/contour5blanck.jpg',
           'images/blanck/contour6blanck.jpg', 'images/blanck/contour7blanck.jpg',
           'images/blanck/contour8blanck.jpg', 'images/blanck/contour9blanck.jpg',
           'images/blanck/contour10blanck.jpg', 'images/blanck/contour11blanck.jpg']

liste = [[160, 117, 22, 14], [160, 117, 22, 14],
         [35, 69, 26, 53], [35, 69, 26, 53],
         [56, 60, 28, 57], [56, 60, 28, 57],
         [14, 60, 20, 19], [14, 60, 20, 19],
         [89, 58, 52, 67], [89, 58, 52, 67],
         [134, 57, 32, 51], [134, 57, 32, 51]]

area = [137.5, 125.0, 424.5, 411.5, 603.0, 585.0, 154.0,
        140.0, 997.0, 957.5, 531.5, 509.5]

original = open_picture("images/" + "lign_v1.jpg")
show_picture("original", original, 0, "")

#displaying(picture, liste)

#======================================================================================

#positionement des contours

dico = {}

liste_placement = sorted([i[0] + i[2] for i in liste])

for nb, name in enumerate(picture):
    for i in liste_placement:
        if liste[nb][0] + liste[nb][2] == i:
            dico[name] = [liste_placement.index(i), liste[nb]]
                #name            #position          #coordinates



#triage, position l'un par apport a l'autre
liste_positionnage = []
for i in range(len(liste)):
    for key, value in dico.items():
        if value[0] == i:
            liste_positionnage.append([key, value[1]])

ok_liste = [liste_positionnage[i] for i in range(0, len(liste_positionnage), 2)]


points_road = [(33, 60, 37, 69), (60, 109, 56, 95),
              (83, 109, 89, 108), (140, 95, 134, 84),
              (159, 107, 160, 117)]

    


#on cherche le schema selon la position
for i in range(len(ok_liste)):

    print(ok_liste[i])
    print(ok_liste[i + 1])

    img = open_picture(ok_liste[i][0])
    copy = img.copy()
    img2 = open_picture(ok_liste[i + 1][0])

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    (x, y, w, h) = (ok_liste[i][1][0], ok_liste[i][1][1],\
                    ok_liste[i][1][2], ok_liste[i][1][3])

    (x1, y1, w1, h1) = (ok_liste[i + 1][1][0], ok_liste[i + 1][1][1],\
                        ok_liste[i + 1][1][2], ok_liste[i + 1][1][3])


    if y + h < y1 + h1:
        print("celle d'apres est plus basse et a droite")
    else:
        print("plus haut et a droite")




    y, x = points_road[i][0], points_road[i][1]

    print(x, y)
    
    y1, x1 = points_road[i][2], points_road[i][3]

    img[x, y] = 0, 0, 255
    img[x1, y1] = 255, 0, 0


    pbx, pby = find_first_points(gray)

    historic = []
    last = []
    t = 0

    ocontinuer = True
    while ocontinuer:

        #List for decide next move.
        current = []
        


                  #0     #1     #2    #3      #4     #5     #6    #7
        listex = [pbx+1,   pbx-1,   pbx,    pbx,      pbx+1,   pbx-1,   pbx+1,  pbx-1]
        listey = [pby,       pby,   pby+1,  pby-1,    pby+1,   pby-1,   pby-1,  pby+1]

        #We ask white neighboors points.
        for i in range(len(listex)):
            if gray[listex[i], listey[i]] >= 250:
                current.append(i)



        current = no_bloc(last, current)

        #Delete x - 1 if we have moved to (x + 1; y + 1)
        current = diagonale(current)

        #Delete from historic
        current = arrierre_avant(historic, current, pbx, pby, last)

        #Delete a corner by a lign
        current = corner_to_lign(current, last)

        #Add pixel if we moving by diagonal
        speciale_corner_after_selection(current, copy, gray, pbx, pby)



        
        historic.append([pbx, pby])





        #We decide to begening to move to the bot.
        if t == 0 and len(current) > 1:
            current = [current[0]]
            t += 1



        for i in current:

            if i == 0:
                #print("zero")
                pbx, pby = incrementation(pbx, pby, 1, 0, copy, "color_copy")
                last = []; last.append(0);
                copy[pbx, pby]  = 0, 0, 255; break;
        
            if i == 1:
                #print("un")
                pbx, pby = incrementation(pbx, pby, -1, 0, copy, "color_copy")
                last = []; last.append(1);
                copy[pbx, pby]  = 0, 0, 255; break;

            elif i == 2:
                #print("deux")
                pbx, pby = incrementation(pbx, pby, 0, 1, copy, "color_copy")
                last = []; last.append(2);
                copy[pbx, pby]  = 0, 0, 255; break;

            elif i == 3:
                #print("trois")
                pbx, pby = incrementation(pbx, pby, 0, -1, copy, "color_copy")
                last = []; last.append(3);
                copy[pbx, pby]  = 0, 0, 255; break;


            elif i == 4:
                #print("quattre")
                pbx, pby = incrementation(pbx, pby, 1, 1, copy, "color_copy")
                last = []; last.append(4); break;

            elif i == 5:
                #print("cinq")
                pbx, pby = incrementation(pbx, pby, -1, -1, copy, "color_copy")
                last = []; last.append(5); break;

            elif i == 6:
                #print("six")
                pbx, pby = incrementation(pbx, pby, 1, -1, copy, "color_copy")
                last = []; last.append(6); break;


            elif i == 7:
                #print("sept")
                pbx, pby = incrementation(pbx, pby, -1, 1, copy, "color_copy")
                last = []; last.append(7); break;






        #copy1 = cv2.resize(copy, (200, 200))
        #show_picture("img", copy1, 0, "")


        if len(historic) > 10:
            if historic[0] == historic[-1]:
                ocontinuer = False

                for i in historic:
                    if i[0] == x and i[1] == y:
                        index = historic.index(i)

                print(len(historic))
                print("ici", index-10, index+10)

                schema = historic[index-20:index]
                for i in schema:
                    copy[i[0], i[1]] = 255, 0, 0

                schema = historic[index:index + 20]
                for i in schema:
                    copy[i[0], i[1]] = 0, 255, 0



                copy1 = cv2.resize(copy, (800, 800))
                show_picture("img", copy1, 0, "")


                img2[x1, y1] = 0, 255, 0
        
    



    
    copy = cv2.resize(img, (800, 800))
    copy2 = cv2.resize(img2, (800, 800))
    cv2.imwrite("ici.png", img)
    cv2.imwrite("ici2.png", img2)
    #show_picture("img", copy, 0, "")
    #show_picture("img2", img2, 0, "")



    print("")















