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
from operation import find_first_points
from operation import incrementation

#Our conditions for moving to the next point
from drawing import *

def redraw_contour(pict):

    img = open_picture(pict)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    copy = img.copy()


    #===========================================
    #Variables
    last = []     #last point
    historic = [] #All last points
    t = 0         #We decide to move to the top (x+1)
                  #bot for us
    histo_current = []
    #===========================================


    #We search the first left top white point.
    x, y = find_first_points(gray)

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
        out = speciale_corner_after_selection(current, copy, gray, x, y)
        if out != [""]:
            historic.append([out[0][0], out[0][1]])
        #print(current)

        historic.append([x, y])

        #print(x, y)
        #===========================================
        histo_current.append(current[0])




        
        #===========================================
        #Increment position
        #Replace last position
        #Break because a noob coded it
        for i in current:

            if i == 0:
                #print("zero")
                x, y = incrementation(x, y, 1, 0, copy, "color_copy")
                last = []; last.append(0); break;

            if i == 1:
                #print("un")
                x, y = incrementation(x, y, -1, 0, copy, "color_copy")
                last = []; last.append(1); break;

            elif i == 2:
                #print("deux")
                x, y = incrementation(x, y, 0, 1, copy, "color_copy")
                last = []; last.append(2); break;

            elif i == 3:
                #print("trois")
                x, y = incrementation(x, y, 0, -1, copy, "color_copy")
                last = []; last.append(3); break;

            elif i == 4:
                #print("quattre")
                x, y = incrementation(x, y, 1, 1, copy, "color_copy")
                last = []; last.append(4); break;

            elif i == 5:
                #print("cinq")
                x, y = incrementation(x, y, -1, -1, copy, "color_copy")
                last = []; last.append(5); break;

            elif i == 6:
                #print("six")
                x, y = incrementation(x, y, 1, -1, copy, "color_copy")
                last = []; last.append(6); break;


            elif i == 7:
                #print("sept")
                x, y = incrementation(x, y, -1, 1, copy, "color_copy")
                last = []; last.append(7); break;

        #print(x, y)
        #print("")

        #===========================================
        #End condition
      
        if len(historic) > 10:
            if historic[0] == historic[-1]:
                ocontinuer = False
                print(historic)
                print("")
                print(histo_current)

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

    #===========================================
    #Saving blanck contour draw
    path = "images/blanck/"
    cv2.imwrite(path + str(pict[:-4]) + "blanck" + ".jpg", gray)
    #show_picture("blanck_resize", blanck_resize, 0, "y")

    #===========================================

#redraw_contour(r"C:\Users\jeanbaptiste\Desktop\chaipas\images\treatment\contour0.png")
