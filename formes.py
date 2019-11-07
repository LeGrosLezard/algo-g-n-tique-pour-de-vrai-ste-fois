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


#displaying(picture, liste)

#======================================================================================

dico = {}

liste_placement = sorted([i[0] + i[2] for i in liste])


for nb, name in enumerate(picture):
    for i in liste_placement:
        if liste[nb][0] + liste[nb][2] == i:
            dico[name] = [liste_placement.index(i), liste[nb]]


display(dico)




































