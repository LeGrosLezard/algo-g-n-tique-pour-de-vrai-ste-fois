import os

import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\chaipas")

from paths import path_image_treatment as PIT

#Library
import cv2

#Opening, Displaying, Creating picture.
from starter.operation import open_picture
from starter.operation import show_picture
from starter.operation import blanck_picture

#Contours parameters
R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE



def filters(img):
    #Gray and edges filters.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img, 255,200)
    return edges


def create_dico(number, PIT, name):

    dico = {}
    
    for i in range(number):
        dico[name.format(PIT, str(i))] = []

    return dico


def add_dico(dico, cnt, number, name, PIT):


    for key, value in dico.items():
        if key == name.format(PIT, str(number)):
            value.append(cv2.boundingRect(cnt))
            value.append(cv2.contourArea(cnt))
                
    return dico



def make_contours(pict):

    #Openning picture
    img = open_picture(pict)

    #filters.
    edges = filters(img)

    #Contours are writte into a black picture.
    contours, _ = cv2.findContours(edges, R, P)

    #initialise dico
    name = "{}contour{}.png"
    dico_data = create_dico(len(contours), PIT, name)

    for nb, cnt in enumerate(contours):

        blanck = blanck_picture(img)
        cv2.drawContours(blanck, [cnt], -1, (255,255,255), 1)

        dico_data = add_dico(dico_data, cnt, nb, name, PIT)

        cv2.imwrite(name.format(PIT, str(nb)), blanck)
        show_picture("img", img, 0, "")


    print(dico_data)
    return dico_data





#crop_contour(r"C:\Users\jeanbaptiste\Desktop\chaipas\images\lign_v1.jpg")
