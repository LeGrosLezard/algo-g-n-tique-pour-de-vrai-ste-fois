#========================================================================
"""Importation of module"""

#for paths
import os

#Librairy for treating pictures
import cv2
from PIL import Image

#Here numpy generate matrix
import numpy as np

#Show, Open, Create black picture
from operation import open_picture
from operation import show_picture
from operation import blanck_picture

#Our conditions for moving to the next point
from drawing import *

#Path of our pictures
from paths import path_image_treatment as PIT

#========================================================================



#We make the treated picture into a list.
liste_treat = os.listdir(PIT)

#We crop last points of the draw.
#Now we course the folder.
for pict in liste_treat:

    img = open_picture(PIT + "contour10.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    copy = img.copy()


    #===========================================

    #Variables
    pointsx = []  #x pos
    pointsy = []  #y pos
    last = []     #last point
    historic = [] #All last points
    t = 0         #We decide to move to the top (x+1)
                  #bot for us

    #===========================================


    #We search the first left top white point.
    for y in range(gray.shape[1]):
        for x in range(gray.shape[0]):
            if gray[x ,y] == 255:
                pointsx.append([x, y])

    #First left top white point.
    x = pointsx[0][0]
    y = pointsx[0][1]

    #===========================================


    ocontinuer = True
    while ocontinuer:

        #List for decide next move.
        current = []

        #Neightboor points of the current position.

                  #0     #1     #2    #3      #4     #5     #6    #7
        listex = [x+1,   x-1,   x,    x,      x+1,   x-1,   x+1,  x-1]
        listey = [y,       y,   y+1,  y-1,    y+1,   y-1,   y-1,  y+1]

        #We ask white neighboors points.
        for i in range(len(listex)):
            if gray[listex[i], listey[i]] == 255:
                current.append(i)

        #We decide to begening to move to the bot.
        if t == 0 and len(current) > 1:
            current = [current[0]]
            t += 1

        #print(last)
        #print(current)


        #===========================================
        #We treat points for decide where keep moving.

        #Move x + 1 delete x - 1 detection
        current = no_bloc(last, current)

        #Delete x - 1 if we have moved to (x + 1; y + 1)
        current = diagonale(current)

        #Delete from historic
        current = arrierre_avant(historic, current, x, y, last)

        #Delete a corner by a lign
        current = corner_to_lign(current, last)

        #Add pixel if we moving by diagonal
        speciale_corner_after_selection(current, copy, gray, x, y)
        #print(current)

        historic.append([x, y])
        #print(x, y)
        #===========================================





        
        #===========================================
        #Increment position
        #Replace last position
        #Break because a noob coded it
        for i in current:

            if i == 0:
                #print("zero")
                x, y = incrementation(x, y, 1, 0, copy)
                last = []; last.append(0); break;

            if i == 1:
                #print("un")
                x, y = incrementation(x, y, -1, 0, copy)
                last = []; last.append(1); break;

            elif i == 2:
                #print("deux")
                x, y = incrementation(x, y, 0, 1, copy)
                last = []; last.append(2); break;

            elif i == 3:
                #print("trois")
                x, y = incrementation(x, y, 0, -1, copy)
                last = []; last.append(3); break;

            elif i == 4:
                #print("quattre")
                x, y = incrementation(x, y, 1, 1, copy)
                last = []; last.append(4); break;

            elif i == 5:
                #print("cinq")
                x, y = incrementation(x, y, -1, -1, copy)
                last = []; last.append(5); break;

            elif i == 6:
                #print("six")
                x, y = incrementation(x, y, 1, -1, copy)
                last = []; last.append(6); break;


            elif i == 7:
                #print("sept")
                x, y = incrementation(x, y, -1, 1, copy)
                last = []; last.append(7); break;

        #print(x, y)
        #print("")

        #===========================================



        #===========================================
        #Display help part

        copy1 = copy.copy()
        cv2.imwrite("ici.png", copy1)
        cv2.imwrite("iciblanck.png", gray)
        copy1 = cv2.resize(copy1, (800, 800))
        #show_picture("copy1", copy1, 0, "")

        blanck_resize = cv2.resize(gray, (800, 800))
        show_picture("copy1", copy1, 1, "")
        #show_picture("blanck_resize", blanck_resize, 0, "")

        #===========================================



show_picture("copy1", copy1, 0, "")

