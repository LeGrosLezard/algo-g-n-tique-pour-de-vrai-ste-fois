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

from drawing import *


path = "images/blanck/"

#We make the treated picture into a list.
liste_treat = os.listdir(path)

for pict in liste_treat:
    img = open_picture(path + pict)
    copy = img.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    x, y = find_first_points(gray)
    print(x, y)

    last = []
    t = 0
    copy[117, 160] = 255, 0, 0

    ocontinuer = True
    while ocontinuer:


                  #0     #1     #2    #3
        listex = [x+1,   x-1,   x,    x]
        listey = [y,       y,   y+1,  y-1]

        region = []

        for i in range(len(listex)):
            if gray[listex[i], listey[i]] > 200:
                print(gray[listex[i], listey[i]])
                region.append(i)

        if t == 0:
            region = [region[0]]
            t += 1

        print(region)
        region = no_bloc(last, region)
        print(region)





        
        for i in region:

            if i == 0:
                x, y = incrementation(x, y, 1, 0, copy)
                last = []
                last.append(i)
                break
   
            if i == 1:
                x, y = incrementation(x, y, -1, 0, copy)
                last = []
                last.append(i)
                break

            if i == 2:
                x, y = incrementation(x, y, 0, 1, copy)
                last = []
                last.append(i)
                break

            if i == 3:
                x, y = incrementation(x, y, 0, -1, copy)
                last = []
                last.append(i)
                break

        print(x, y)



        cv2.imwrite("ici.png", copy)
        cv2.imwrite("iciblanck.png", gray)
        copy1 = cv2.resize(copy, (800, 800))
        show_picture("copy1", copy1, 0, "")
        
























    gray_resize = cv2.resize(gray, (200, 200))

































