#for paths
import os

from paths import full_path

import sys
sys.path.append(full_path)


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




def recup_points(gray):
    """Recup x, y and (x, y) points where gray pixels are white."""

    liste_pointsX = [x for x in range(gray.shape[0])
                     for y in range(gray.shape[1]) if gray[x, y] >= 200]
    liste_pointsY = [y for x in range(gray.shape[0])
                     for y in range(gray.shape[1]) if gray[x, y] >= 200]
    all_points = [[x, y] for x in range(gray.shape[0])
                  for y in range(gray.shape[1]) if gray[x, y] >= 200]

    return liste_pointsX, liste_pointsY, all_points



def extremity(liste, coordinate, placement):
    """Recuperate all points from a coordinate"""

    for i in liste:
        if i[placement] == coordinate:
            return i


def drawing_circle(*args):
    """Make circle"""

    cv2.circle(args[0], (args[1], args[2]), 1, args[3], 1)


def drawsing_lines(*args):
    """Make lines"""

    cv2.line(args[0], (args[1], args[2]), (args[3], args[4]),
             args[5], 1)

def recuperate_extremities_points(all_points, liste_pointsX, liste_pointsY, blanck, liste):

    #Recup right, left, top and bot extremities of forms.
    a = extremity(all_points, min(liste_pointsY), 1)
    b = extremity(all_points, max(liste_pointsY), 1)
    c = extremity(all_points, min(liste_pointsX), 0)
    d = extremity(all_points, max(liste_pointsX), 0)

    liste.append([a, b, c ,d])

    #Drawing a line beetween points 
    drawsing_lines(blanck, a[1], a[0], b[1], b[0], (0,255,0))
    drawsing_lines(blanck, c[1], c[0], d[1], d[0], (0,255,0))

    #Drawing a line beetween circles 
    drawing_circle(blanck, a[1], a[0], (0, 0, 255))
    drawing_circle(blanck, b[1], b[0], (0, 0, 255))
    drawing_circle(blanck, c[1], c[0], (255, 0, 0))
    drawing_circle(blanck, d[1], d[0], (255, 0, 0))


def recuperate_mini_distance(liste):
    """Recuperate minimum distance beetween last and next forms.
    We make difference beetween (x1, y1) and (x1, x2)
    and recup the minimum value after sum"""

    mini = []; min_val = 100000;

    for i in liste[-2]:
        for j in liste[-1]:

            a = abs(i[0] - j[0])
            b = abs(i[1] - j[1])
            c = a + b

            if c < min_val:
                mini = []
                mini.append([i, j]) 
                min_val = c

    return mini[0][0][1], mini[0][0][0], mini[0][1][1], mini[0][1][0]



def points_placements(original, liste_information):

    original = img = open_picture(original)
    show_picture("original", original, 0, "")
    blanck = blanck_picture(img)


    liste = []
    minimum_distance = []
    for i in liste_information:

        img = open_picture(i[0])
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #Recup white pixels from gray.
        liste_pointsX, liste_pointsY, all_points = recup_points(gray)
        recuperate_extremities_points(all_points, liste_pointsX,
                                      liste_pointsY, blanck, liste)

        #Recuperate last 2 forms connected from list.
        try:
            #print(liste[-2], "\n")
            #print(liste[-1])
            x1, y1, x2, y2 = recuperate_mini_distance(liste)
            minimum_distance.append((x1, y1, x2, y2))
            drawsing_lines(blanck, x1, y1, x2, y2, (255,255,255))
        except:
            pass


        copy_blanck = cv2.resize(blanck, (800, 800))
        show_picture("copy_blanck", copy_blanck, 0, "")

    #print(liste, "\n")
    #print(minimum_distance)

    return liste, minimum_distance


#de forme
liste_information = [['../images/blanck/6blanck.jpg', [14, 60, 20, 19]],
                    ['../images/blanck/2blanck.jpg', [35, 69, 26, 53]],
                    ['../images/blanck/4blanck.jpg', [56, 60, 28, 57]],
                    ['../images/blanck/8blanck.jpg', [89, 58, 52, 67]],
                    ['../images/blanck/10blanck.jpg', [134, 57, 32, 51]],
                    ['../images/blanck/0blanck.jpg', [160, 117, 22, 14]]]


#points_placements("../images/lign_v1.jpg", liste_information)















