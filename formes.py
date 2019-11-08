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

    
liste_points_shems = []

#on cherche le schema selon la position
for ii in range(len(ok_liste)):

    print(ok_liste[ii])
    print(ok_liste[ii + 1])

    img = open_picture(ok_liste[ii][0])
    img2 = open_picture(ok_liste[ii + 1][0])

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)



    copy = img.copy()

    copy2 = img2.copy()


    #1er pts
    pbx, pby = find_first_points(gray)
    




    historic = []
    last = []
    t = 0


    ocontinuer = True
    while ocontinuer:


        current = []
        


                  #0     #1     #2    #3      #4     #5     #6    #7
        listex = [pbx+1,   pbx-1,   pbx,    pbx,      pbx+1,   pbx-1,   pbx+1,  pbx-1]
        listey = [pby,       pby,   pby+1,  pby-1,    pby+1,   pby-1,   pby-1,  pby+1]


        for i in range(len(listex)):
            if gray[listex[i], listey[i]] >= 100:
                current.append(i)

        #print(current)

        current = no_bloc(last, current)
        current = diagonale(current)
        current = arrierre_avant(historic, current, pbx, pby, last)
        current = corner_to_lign(current, last)
        speciale_corner_after_selection(current, copy, gray, pbx, pby)
        historic.append([pbx, pby])

        #print(current)

        if t == 0 and len(current) > 1:
            current = [current[0]]
            t += 1



        for i in current:

            if i == 0:
                #print("zero")
                pbx, pby = incrementation(pbx, pby, 1, 0, copy, "color_copy")
                last = []; last.append(0);break;
            if i == 1:
                #print("un")
                pbx, pby = incrementation(pbx, pby, -1, 0, copy, "color_copy")
                last = []; last.append(1);break;
            elif i == 2:
                #print("deux")
                pbx, pby = incrementation(pbx, pby, 0, 1, copy, "color_copy")
                last = []; last.append(2);break;
            elif i == 3:
                #print("trois")
                pbx, pby = incrementation(pbx, pby, 0, -1, copy, "color_copy")
                last = []; last.append(3);break;
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


        copy1 = cv2.resize(copy, (800, 800))
        #show_picture("img", copy1, 0, "")



        if len(historic) > 10:
            if historic[0] == historic[-1]:
                ocontinuer = False










    #1er pts
    pbx, pby = find_first_points(gray2)
    

    historic2 = []
    last = []
    t = 0


    ocontinuer = True
    while ocontinuer:


        current = []
        


                  #0     #1     #2    #3      #4     #5     #6    #7
        listex = [pbx+1,   pbx-1,   pbx,    pbx,      pbx+1,   pbx-1,   pbx+1,  pbx-1]
        listey = [pby,       pby,   pby+1,  pby-1,    pby+1,   pby-1,   pby-1,  pby+1]


        for i in range(len(listex)):
            if gray2[listex[i], listey[i]] >= 100:
                current.append(i)

        #print(current)

        current = no_bloc(last, current)
        current = diagonale(current)
        current = arrierre_avant(historic2, current, pbx, pby, last)
        current = corner_to_lign(current, last)
        speciale_corner_after_selection(current, copy, gray2, pbx, pby)
        historic2.append([pbx, pby])

        #print(current)

        if t == 0 and len(current) > 1:
            current = [current[0]]
            t += 1



        for i in current:

            if i == 0:
                #print("zero")
                pbx, pby = incrementation(pbx, pby, 1, 0, copy, "color_copy")
                last = []; last.append(0);break;
            if i == 1:
                #print("un")
                pbx, pby = incrementation(pbx, pby, -1, 0, copy, "color_copy")
                last = []; last.append(1);break;
            elif i == 2:
                #print("deux")
                pbx, pby = incrementation(pbx, pby, 0, 1, copy, "color_copy")
                last = []; last.append(2);break;
            elif i == 3:
                #print("trois")
                pbx, pby = incrementation(pbx, pby, 0, -1, copy, "color_copy")
                last = []; last.append(3);break;
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


        copy1 = cv2.resize(copy, (800, 800))
        #show_picture("img", copy1, 0, "")










        if len(historic2) > 10:
            if historic2[0] == historic2[-1]:
                ocontinuer = False



                points_road = [(33, 60, 37, 69), (60, 109, 56, 95),
                              (83, 109, 89, 108), (140, 95, 134, 84),
                              (159, 107, 160, 117)]
                #pts histor
                y, x = points_road[ii][0], points_road[ii][1]
                y1, x1 = points_road[ii][2], points_road[ii][3]




                for i in historic:
                    if i[0] == x and i[1] == y:
                        index = historic.index(i)

                print(len(historic))


                avant = [i for i in historic[index-20:index]]
                apres = [i for i in historic[index:index+20]]


                for i in avant:
                    copy[i[0], i[1]] = 255, 0, 0

                for i in apres:
                    copy[i[0], i[1]] = 0, 255, 0








                for i in historic2:
                    if i[0] == x1 and i[1] == y1:
                        index2 = historic2.index(i)


                avant2 = [i for i in historic2[index2-20:index2]]
                apres2 = [i for i in historic2[index2:index2+20]]


                for i in avant2:
                    copy[i[0], i[1]] = 255, 0, 0

                for i in apres2:
                    copy[i[0], i[1]] = 0, 255, 0





                print(avant)
                print("")
                print(apres)

                print("")
                print("")
                
                print(avant2)
                print("")
                print(apres2)






                copy1 = cv2.resize(copy, (800, 800))
                show_picture("img", copy1, 0, "")


                img2[x1, y1] = 0, 255, 0
        
    



    
print(liste_points_shems)



















