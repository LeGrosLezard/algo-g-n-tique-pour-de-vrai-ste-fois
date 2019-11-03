import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from operation import open_picture
from operation import show_picture
from operation import blanck_picture



R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE

image = ['images/ligne.jpg', 'images/ligne_to.jpg']


def recup_contours(img):

    edges = cv2.Canny(img, 255,200)
    contours, _ = cv2.findContours(edges, R, P)

    for cnts in contours:
        
        cv2.fillPoly(blanck, pts =[cnts], color=(255, 255, 255))
        (x, y, w, h) = cv2.boundingRect(cnts)
        #show_picture("blanck", blanck, 0, "")

    return blanck


def display(copy):

    copy[x-1, y] = 0, 0, 255
    copy[x+1, y] = 0, 0, 255

    copy[x, y:y+10] = 255, 0, 0
    copy[x, y-10:y] = 255, 0, 0

    #show_picture("copy", copy, 0, "")


for im in image:


    img = open_picture(im)
    show_picture("orignal", img, 0, "")

    #make copy
    copy = img.copy()
    blanck = blanck_picture(img)
    blanck_no = blanck_picture(img)

    #make contours
    blanck = recup_contours(img)


    for x in range(blanck.shape[0]):
        for y in range(blanck.shape[1]):

            #For diplay
            copy = blanck.copy()

            if blanck[x, y][0] == 0 and\
               blanck[x, y][1] == 0 and\
               blanck[x, y][2] == 0:
                pass

            else:
                counter = 0
                for i in copy[x, y:y+10].tolist():
                    if str(i) == "[0, 0, 0]":
                        counter += 1

                if counter < 10 and counter > 0 and\
                   copy[x, y+10][0] == 255 and\
                   copy[x, y+10][1] == 255 and\
                   copy[x, y+10][2] == 255:
                    #print(img[x, y])
                    img[x, y:y+10] = img[x, y]

                display(copy)


    show_picture("img", img, 0, "")

