#========================================================================
"""Importation of module"""


import os

import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\chaipas")

#Librairy for treating pictures
import cv2
from PIL import Image

#Here numpy generate matrix
import numpy as np

#Show, Open, Create black picture
from starter.operation import open_picture
from starter.operation import show_picture
from starter.operation import blanck_picture
from starter.operation import find_first_points
from starter.operation import incrementation

#Our conditions for moving to the next point
from contours_complement.drawing import recup_contours
from contours_complement.drawing import neightboors_points
from contours_complement.drawing import no_bloc
from contours_complement.drawing import diagonale
from contours_complement.drawing import arrierre_avant
from contours_complement.drawing import corner_to_lign
from contours_complement.drawing import speciale_corner_after_selection

def search_neightboors(current, gray, x, y, t):

    #Neightboor points of the current position.

              #0     #1     #2    #3      #4     #5     #6    #7
    listex = [x+1,   x-1,   x,    x,      x+1,   x-1,   x+1,  x-1]
    listey = [y,       y,   y+1,  y-1,    y+1,   y-1,   y-1,  y+1]


    #We ask white neighboors points.
    current = [i for i in range(len(listex))\
               if gray[listex[i], listey[i]] == 255]

    out = current, ""

    #We decide to begening to move to the bot.
    if t == 0 and len(current) > 1:
        current = [current[0]]
        t += 1

        out = current, t

    return out


def choice_next_points(current, last, historic, x, y, copy, gray):

    #Move x + 1 delete x - 1 detection
    current = no_bloc(last, current)

    #Delete x - 1 if we have moved to (x + 1; y + 1)
    current = diagonale(current)

    #Delete from historic
    current = arrierre_avant(historic, current, x, y, last)

    #Delete a corner by a lign
    current = corner_to_lign(current, last)

    #Add pixel if we moving by diagonal.
    out = speciale_corner_after_selection(current, copy, gray, x, y)
    if out != [""]:
        historic.append([out[0][0], out[0][1]])

    return current


def end_condition(historic, histo_current):

    ocontinuer = True

    #End condition
    if len(historic) > 10:
        if historic[0] == historic[-1]:
            ocontinuer = False
            print(historic)
            print("")
            print(histo_current)

    return ocontinuer



def displaying(gray, copy):

    #Display help part
    copy1 = copy.copy()
    #cv2.imwrite("ici.png", copy1)
    #cv2.imwrite("iciblanck.png", gray)
    copy1 = cv2.resize(copy1, (800, 800))
    #show_picture("copy1", copy1, 0, "")

    blanck_resize = cv2.resize(gray, (800, 800))
    show_picture("copy1", copy1, 1, "")
    #show_picture("blanck_resize", blanck_resize, 0, "")


def movement(last, current, x, y, copy):

    for i in current:

        if i == 0:
            x, y = incrementation(x, y, 1, 0, copy, "color_copy")
            last.append(0); break;
        elif i == 1:
            x, y = incrementation(x, y, -1, 0, copy, "color_copy")
            last.append(1); break;
        elif i == 2:
            x, y = incrementation(x, y, 0, 1, copy, "color_copy")
            last.append(2); break;
        elif i == 3:
            x, y = incrementation(x, y, 0, -1, copy, "color_copy")
            last.append(3); break;
        elif i == 4:
            x, y = incrementation(x, y, 1, 1, copy, "color_copy")
            last.append(4); break;
        elif i == 5:
            x, y = incrementation(x, y, -1, -1, copy, "color_copy")
            last.append(5); break;
        elif i == 6:
            x, y = incrementation(x, y, 1, -1, copy, "color_copy")
            last.append(6); break;
        elif i == 7:
            x, y = incrementation(x, y, -1, 1, copy, "color_copy")
            last.append(7); break;

    return x, y



def redraw_contour(pict, name):

    #Open picture, filter, copy
    img = open_picture(pict)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    copy = img.copy()

    #Variables
    last = []          #last point
    historic = []      #All last points
    t = 0              #We decide to move to the top (x+1)
    histo_current = [] #All deplacements


    #We search the first left top white point.
    x, y = find_first_points(gray)

    ocontinuer = True
    while ocontinuer:

        #List for decide next move.
        current = []
        current, t = search_neightboors(current, gray, x, y, t)

        #choice of the next point.
        choice_next_points(current, last, historic,
                           x, y, copy, gray)
        last = []

        #Recup historic
        historic.append([x, y])
        histo_current.append(current[0])

        #Increment position and Replace last position
        x, y = movement(last, current, x, y, copy)

        #End condition
        ocontinuer = end_condition(historic, histo_current)

        #Displaying
        displaying(gray, copy)


    #Saving blanck contour draw
    path = "images/blanck/{}"
    print(path.format(name + "blanck.jpg"))
    cv2.imwrite(path.format(name + "blanck.jpg"), gray)
    #show_picture("blanck_resize", blanck_resize, 0, "y")



#redraw_contour(r"C:\Users\jeanbaptiste\Desktop\chaipas\images\treatment\contour0.png")
