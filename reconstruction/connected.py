#for paths
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



def treat_mini(minini):
    treat_minini = []
    for i in minini:
        treat_minini.append([i[0][0][0], i[0][0][1]])
        treat_minini.append([i[0][1][0], i[0][1][1]])
    return treat_minini


def treat_shems(liste):

    b = [j for i in liste for j in i if j != "SITUATION"]
    return b

def make_dico(b):
    dico_schema = {}
    for i in b:
        dico_schema[i] = 0

    return dico_schema


def color_it(color, picture, blanck):

    for y in range(picture.shape[1]):
        for x in range(picture.shape[0]):
            if picture[x, y] > 100:
                blanck[x, y] = color
    return blanck

def end_condition(x , y, c, blanck):

    if blanck[x, y][0] == c[0] and\
       blanck[x, y][1] == c[1] and\
       blanck[x, y][2] == c[2]:
        return True
    
def drawing(blanck, gray):
    for x in range(gray.shape[1]):
        for y in range(gray.shape[0]):
            if gray[x, y] > 100:
                blanck[x, y] = 255, 255, 255

def raising(blanck):

    for x in range(blanck.shape[1]):
        for y in range(blanck.shape[0]):
            if blanck[x ,y][0] == 255 and\
               blanck[x, y][1] == 255 and\
               blanck[x, y][2] == 255:
                blanck[x, y] = 0, 0, 0

    return blanck









img = open_picture("ici.png")
copy = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blanck = blanck_picture(img)
blanck1 = blanck_picture(img)


minini = [[[[65, 33], [69, 40]]], [[[113, 60], [103, 56]]], [[[116, 83], [117, 89]]], [[[109, 140], [107, 165]]]]

picture = ['../images/blanck/6blanck.jpg', '../images/blanck/2blanck.jpg', '../images/blanck/4blanck.jpg',
           '../images/blanck/8blanck.jpg', '../images/blanck/10blanck.jpg', '../images/blanck/0blanck.jpg',]

a = [['corner4', 'lign verticale', 'corner7', 'lign horrizontale', 'corner7', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'SITUATION', 'corner5', 'lign verticale', 'corner6', 'lign horrizontale', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6'],
     ['corner4', 'lign verticale', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner7', 'lign horrizontale', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'SITUATION', 'corner5', 'corner6', 'lign horrizontale', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner5', 'lign horrizontale', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'lign verticale', 'corner5', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6'],
     ['corner4', 'lign verticale', 'corner7', 'lign horrizontale', 'corner7', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'corner7', 'corner7', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'SITUATION', 'lign horrizontale', 'corner5', 'lign verticale', 'corner5', 'corner5', 'lign verticale', 'corner5', 'lign verticale', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner6', 'corner6', 'corner6', 'lign horrizontale', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'lign verticale', 'corner6', 'corner6', 'lign verticale', 'corner6'],
     ['corner4', 'lign verticale', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner7', 'lign horrizontale', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'lign verticale', 'SITUATION', 'corner5', 'lign verticale', 'corner6', 'lign horrizontale', 'corner6', 'lign verticale', 'corner6', 'corner6', 'lign verticale', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'lign verticale', 'corner5', 'lign verticale', 'corner5', 'lign verticale', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner6', 'lign horrizontale', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'lign verticale', 'corner6', 'corner6', 'lign verticale', 'corner6', 'corner6', 'lign verticale', 'corner6', 'corner6', 'corner6']]


oki_picture = []
for i in range(0, len(picture), 1):
    try:
        oki_picture.append([picture[i], picture[i + 1]])
        oki_picture.append([picture[i + 1], picture[i]])
    except:
        pass


treat_minini = treat_mini(minini)
schema = ['corner4', 'lign verticale', 'corner7', 'lign horrizontale', 'corner5', 'corner6']


for nb in range(len(minini) * 4):
    blanck = blanck_picture(img)

    print(nb)
    print(oki_picture[nb][0])
    img1 = open_picture(oki_picture[nb][0])
    img2 = open_picture(oki_picture[nb][1])

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


    #print(treat_minini[nb], treat_minini[nb+1])


    x = treat_minini[nb][0]
    y = treat_minini[nb][1]


    for ptx in range(blanck.shape[1]):
        for pty in range(blanck.shape[0]):
            if gray2[ptx, pty] > 100:
                blanck[ptx, pty] = 0, 0, 255

    copy1 = cv2.resize(blanck, (800, 800))
    show_picture("copy1", copy1, 0, "")


    find = False
    for i in schema:

        #If we fine color don't run the others.
        if find is True:
            break

        if i == "corner4":

            listex = [x+1,        x,       x+1,     x+1,  x-1]
            listey = [y,          y+1,     y+1,      y-1,  y+1]

            #We stop if we course more 50 pixels
            for counter in range(50):
                if counter == 49:
                    raising(blanck)
                    break

                #We stop if we get pixel form color
                stop = end_condition(x , y, (0, 0, 255), blanck)
                if stop is True:
                    drawing(blanck, gray)
                    find = True
                    break

                blanck[x, y] = 255, 255, 255
                blanck[x + 1, y] = 255, 255, 255
                copy1 = cv2.resize(blanck, (800, 800))
                show_picture("copy1", copy1, 0, "")
                x+=1
                y += 1




        elif i == 'lign verticale':
            for i in range(2):
                
                if find is True:
                    break

                x = treat_minini[nb][0]
                y = treat_minini[nb][1]
                
                listex = [x,       x+1,     x+1]
                listey = [y+1,     y+1,      y-1]

                for counter in range(50):
                    if counter == 49:
                        raising(blanck)
                        break

                    stop = end_condition(x , y, (0, 0, 255), blanck)
                    if stop is True:
                        drawing(blanck, gray)
                        find = True
                        break

                    blanck[x, y] = 255, 255, 255
                    copy1 = cv2.resize(blanck, (800, 800))
                    show_picture("copy1", copy1, 0, "")

                    if i == 0:
                        x+=1
                        y

                    elif i == 1:
                        x -= 1




        elif i == 'corner7':pass
        elif i == 'lign horrizontale':pass
        elif i == 'corner5':pass
        elif i == 'corner6':pass
















