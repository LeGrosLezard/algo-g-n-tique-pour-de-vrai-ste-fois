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



original = open_picture("images/" + "lign_v1.jpg")
show_picture("original", original, 0, "")
blanck = blanck_picture(original)

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



all_recurent_points = []
ancrage = []

last = []


#on cherche le schema selon la position
for number in range(len(ok_liste)):

    try:
        print(ok_liste[number], ok_liste[number + 1])
        print("")

        a = ok_liste[number][1][0] + ok_liste[number][1][2]
        b = ok_liste[number + 1][1][0] + ok_liste[number + 1][1][2]
        posx = 0
        pos_y = 0

        if b > a:
            print("prochaine a droite")
            posx = "d", abs(a-b)
        else:
            print("prochaine a gauche")
            posx = "g", abs(a-b)

        c = ok_liste[number][1][1]
        d = ok_liste[number + 1][1][1]

        if c > d:
            print("la prochaine en haut de : ", abs(c - d))
            posy = "h", abs(c - d)
        else:
            print("la prochaine en bas de: ", abs(c - d))
            posy = "b", abs(c - d)

        print("last last," , last)
        last = []
        last.append([posx, posy])

        img = open_picture(ok_liste[number][0])
        copy = img.copy()

        print(posx, posy)
        liste = []
        listex = []
        listey = []

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for x in range(gray.shape[1]):
            for y in range(gray.shape[0]):
                if gray[x, y] >= 200:
                    blanck[x, y] = 255, 255, 255
                    liste.append([x, y])
                    listex.append(x)
                    listey.append(y)


        print("")
    ##    print(liste)
    ##    print(listex)
    ##    print(listey)

        print("")

        coord = 0
        if posx[0] == "d":
            b = max(listey)
            for i in liste:
                if i[1] == b:
                    coord = i

        elif posx[0] == "g":
            b = min(listey)
            for i in liste:
                if i[1] == b:
                    coord = i


        print(coord)
        print("")

        print(last)


        other_coord = 0
        if last != [] and last[0][0][0] == "d" and last[0][1][0] == "b":

            
            b = min(listex)
            liste_w = []
            for i in liste:
                if i[0] == b:
                    liste_w.append(i)
            print(liste_w)
            liste_w1 = []
            for i in liste_w:
                liste_w1.append(i[1])

            for i in liste_w:
                if i[1]== min(liste_w1):
                    other_coord = i



        if last != [] and last[0][0][0] == "d"  and last[0][1][0] == "h":
            b = max(listex)
            liste_w = []
            for i in liste:
                if i[0] == b:
                    liste_w.append(i)

            liste_w1 = []
            for i in liste_w:
                liste_w1.append(i[1])

            for i in liste_w:
                if i[1]== max(liste_w1):
                    other_coord = i



        print("iciiiiiiiii", other_coord)
        print("")

        



        blanck[coord[0], coord[1]] = 0, 0, 255

        blanck[other_coord[0], other_coord[1]] = 255, 0, 0

        cv2.imwrite("ici.png", blanck)
        blanck_copy = cv2.resize(blanck, (800, 800))
        show_picture("blanckblanck", blanck_copy, 0, "")

    except:
        pass



##for i in points_road:
##     blanck[i[1], i[0]] = 255, 0, 0
##     
##
##
##
##
##
##
##
##
blanck_copy = cv2.resize(blanck, (800, 800))
show_picture("blanckblanck", blanck_copy, 0, "")
##cv2.imwrite("ici.png", blanck)
##print(ancrage)
##print("")
##print(all_recurent_points)
##


        
























