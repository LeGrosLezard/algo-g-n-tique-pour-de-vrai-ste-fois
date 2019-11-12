import os

from paths import full_path

import sys
sys.path.append(full_path)

#Librairy for treating pictures
import cv2
from PIL import Image

import matplotlib.pyplot as plt

#Here numpy generate matrix
import numpy as np

#Show, Open, Create black picture
from starter.operation import open_picture
from starter.operation import show_picture
from starter.operation import blanck_picture
from starter.operation import find_first_points
from starter.operation import incrementation

from contours_complement.drawing import *



#==========================================================================
"""Sort lists"""

from data_regroupement.formes_function import left_position
from data_regroupement.formes_function import name_position_points
from data_regroupement.formes_function import final_informations
def sorting_list(points_detection, original, pictures):
    
    original = open_picture(original)
    show_picture("original", original, 0, "")
    blanck = blanck_picture(original)

    #Recuperate left position.
    liste_placement = left_position(points_detection)
    #print(liste_placement)

    #Recuperate name, position and coordinates.
    dico = name_position_points(pictures, points_detection, liste_placement)
    #print(dico)

    #Final information, name, position.
    position = final_informations(points_detection, dico)
    #print(liste_position)

    return blanck, position



#==========================================================================
"""Recuperate position from the last and the next picture."""

from data_regroupement.formes_function import placement_next_form_x
from data_regroupement.formes_function import placement_next_form_y
def recuperate_points(position, number):

    img = open_picture(position[number][0])
    copy = img.copy()

    try:
        print(position[number], position[number + 1])

        #Placement pixels x and y axis of the last form.
        last = []
        last.append([placement_next_form_x(position, number),
                     placement_next_form_y(position, number)])

        print("last position are: ", last[0], "\n")

    except IndexError:
        pass

    return img


#======================================================================
"""Recuperate whites pixels."""

from data_regroupement.formes_function import drawing_gray_on_blanck
from data_regroupement.formes_function import recuperate_white_pixels
def recuperate_pixels(gray, blanck):

    drawing_gray_on_blanck(gray, blanck)
    liste_white_pixels = recuperate_white_pixels(gray)

    return liste_white_pixels


#======================================================================
"""Recuperate area of extremities."""

from data_regroupement.formes_function import recuperate_extremities
def recuperate_min_points_liaison(blanck, liste_white_pixels, number, area_points):

    #right, left, bot, top
    coordR = recuperate_extremities(blanck, max(liste_white_pixels[2]), liste_white_pixels[0], 1)
    coordL = recuperate_extremities(blanck, min(liste_white_pixels[2]), liste_white_pixels[0], 1)
    coordB = recuperate_extremities(blanck, max(liste_white_pixels[1]), liste_white_pixels[0], 0)
    coordT = recuperate_extremities(blanck, min(liste_white_pixels[1]), liste_white_pixels[0], 0)

    coords = [coordR + coordL + coordB + coordT]

    for i in coords:
        area_points[number].append(i)

    #cv2.imwrite("ici.png", blanck)


#======================================================================
"""Recuperate minimum distance beetween areas."""

from data_regroupement.formes_function import recup_minimum_points
from data_regroupement.formes_function import display_points

def recuperation_distance(mini_zone, area_points, blanck):

    recup_minimum_points(mini_zone, area_points)
    display_points(mini_zone, blanck)



def main_formes(pictures, points_detection, original):

    #Recuperate all data from picture (name and position from original).
    blanck, position = sorting_list(points_detection, original, pictures)

    #Create this list for area extremity.
    area_points = [[] for i in range(len(position))]

    #From data from picture
    for number in range(len(position)):

        #Recuperate points from orignal and can place
        #them before or after the last or next.
        img = recuperate_points(position, number)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #Recuperate points from gray.
        liste_white_pixels = recuperate_pixels(gray, blanck)

        #Recuperate white points from gray.
        recuperate_min_points_liaison(blanck, liste_white_pixels, number, area_points)

    #Define minimum distance from last points.
    mini_zone = []
    recuperation_distance(mini_zone, area_points, blanck)


    blanck_copy = cv2.resize(blanck, (800, 800))
    show_picture("blanckblanck", blanck_copy, 0, "")

    return mini_zone, area_points





pictures = ['../images/blanck/0blanck.jpg', '../images/blanck/2blanck.jpg', 
            '../images/blanck/4blanck.jpg', '../images/blanck/6blanck.jpg', 
            '../images/blanck/8blanck.jpg', '../images/blanck/10blanck.jpg']

points_detection = [[160, 117, 22, 14], [35, 69, 26, 53], [56, 60, 28, 57], [14, 60, 20, 19], 
                   [89, 58, 52, 67], [134, 57, 32, 51]]

