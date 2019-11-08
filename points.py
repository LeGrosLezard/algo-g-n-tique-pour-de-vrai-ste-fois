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

original = img = open_picture("images/lign_v1.jpg")
show_picture("original", original, 0, "")
blanck = blanck_picture(img)

picture = ['images/blanck/contour0blanck.jpg', 
           'images/blanck/contour2blanck.jpg',
           'images/blanck/contour4blanck.jpg', 
           'images/blanck/contour6blanck.jpg', 
           'images/blanck/contour8blanck.jpg', 
           'images/blanck/contour10blanck.jpg',]

def extremity(liste, coordinate, placement):
    point = 0

    for i in liste:
        if i[placement] == coordinate:
            point = i
            return point


def drawing_circle(*args):
    cv2.circle(args[0], (args[1], args[2]), 1, args[3], 1)

def drawsing_lines(*args):
    cv2.line(args[0], (args[1], args[2]), (args[3], args[4]),
             args[5], 2)




for i in picture:


    img = open_picture(i)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    liste_pointsX = [x for x in range(gray.shape[0]) for y in range(gray.shape[1]) if gray[x, y] == 255]
    liste_pointsY = [y for x in range(gray.shape[0]) for y in range(gray.shape[1]) if gray[x, y] == 255]
    all_points = [[x, y] for x in range(gray.shape[0]) for y in range(gray.shape[1]) if gray[x, y] == 255]


    a = extremity(all_points, min(liste_pointsY), 1)
    b = extremity(all_points, max(liste_pointsY), 1)

    c = extremity(all_points, min(liste_pointsX), 0)
    d = extremity(all_points, max(liste_pointsX), 0)


    drawsing_lines(blanck, a[1], a[0], b[1], b[0], (0,255,0))
    drawsing_lines(blanck, c[1], c[0], d[1], d[0], (0,255,0))


    drawing_circle(blanck, a[1], a[0], (0, 0, 255))
    drawing_circle(blanck, b[1], b[0], (0, 0, 255))

    drawing_circle(blanck, c[1], c[0], (255, 0, 0))
    drawing_circle(blanck, d[1], d[0], (255, 0, 0))
    

blanck = cv2.resize(blanck, (800, 800))
show_picture("blanck", blanck, 0, "")
























