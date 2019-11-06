import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from operation import open_picture
from operation import show_picture
from operation import blanck_picture

from drawing import *

from paths import path_image_treatment as PIT



R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE



liste_treat = os.listdir(PIT)

for pict in liste_treat:

    img = open_picture(PIT + "contour0.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    c_grray = thcheck_gray(gray)
    copy = img.copy()




    pointsx = []
    pointsy = []

    for y in range(gray.shape[1]):
        for x in range(gray.shape[0]):

            if gray[x ,y] == 255:
                pointsx.append([x, y])
                pointsy.append(y)

    x = pointsx[0][0]
    y = pointsx[0][1]









    ok_ok = 0
    last = []
    historic = []
    t = 0
    ocontinuer = True
    while ocontinuer:

        current = []

                  #0     #1     #2    #3      #4     #5     #6    #7
        listex = [x+1,   x-1,   x,    x,      x+1,   x-1,   x+1,  x-1]
        listey = [y,       y,   y+1,  y-1,    y+1,   y-1,   y-1,  y+1]


        

        for i in range(len(listex)):
            if gray[listex[i], listey[i]] == 255:
                current.append(i)

        if t == 0 and len(current) > 1:
            current = [current[0]]
        t += 1

        print(last)
        print(current)

        corner(current, copy, gray,x ,y)
        current = no_bloc(last, current)
        current = diagonale(current)
        current = arrierre_avant(historic, current, x, y, last)
        current = corner_to_lign(current, last)
        print(current)

        speciale_corner_after_selection(current, copy, gray, x, y)



        historic.append([x, y])

        print(x, y)
        for i in current:

            if i == 0:

                print("zero")
                x, y = incrementation(x, y, 1, 0, copy)
                last = []
                last.append(0)
                break

            if i == 1:
                print("un")
                x, y = incrementation(x, y, -1, 0, copy)
                last = []
                last.append(1)
                break


            elif i == 2:

                print("deux")
                x, y = incrementation(x, y, 0, 1, copy)
                last = []
                last.append(2)
                break

            elif i == 3:
                print("trois")
                x, y = incrementation(x, y, 0, -1, copy)
                last = []
                last.append(3)
                break

            elif i == 4:
                print("quattre")
                x, y = incrementation(x, y, 1, 1, copy)
                last = []
                last.append(4)
                break

            elif i == 5:
                print("cinq")
                x, y = incrementation(x, y, -1, -1, copy)
                last = []
                last.append(5)
                break

            elif i == 6:
                print("six")
                x, y = incrementation(x, y, 1, -1, copy)
                last = []
                last.append(6)
                break


            elif i == 7:
                print("sept")
                x, y = incrementation(x, y, -1, 1, copy)
                last = []
                last.append(7)
                break

        print(x, y)
        print("")






        copy1 = copy.copy()
        #cv2.imwrite("ici.png", copy1)
        #cv2.imwrite("iciblanck.png", gray)
        copy1 = cv2.resize(copy1, (800, 800))

        #show_picture("copy1", copy1, 0, "")

        blanck_resize = cv2.resize(gray, (800, 800))
        #show_picture("copy1", copy1, 0, "")
        #show_picture("blanck_resize", blanck_resize, 0, "")


        print(t)
        if t == 50:
            c_copy = thcheck_copy(copy)
            t = 1

            if c_copy > c_grray:
                ok_ok += 1
            print("COMPARAISON", c_grray, c_copy)

        if ok_ok > 10:
            ocontinuer = False




show_picture("copy1", copy1, 0, "")







