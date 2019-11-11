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

from connected_function import treat_mini
from connected_function import treat_shems
from connected_function import make_dico
from connected_function import end_condition
from connected_function import drawing
from connected_function import raising
from connected_function import picture_schema_dico
from connected_function import add_list_next_last
from connected_function import road_test


minini = [[[65, 33], [71, 35]], [[109, 60], [103, 56]], [[109, 83], [109, 89]], [[94, 140], [88, 134]], [[107, 165], [117, 165]]]


picture = ['../images/blanck/6blanck.jpg', '../images/blanck/2blanck.jpg', '../images/blanck/4blanck.jpg',
           '../images/blanck/8blanck.jpg', '../images/blanck/10blanck.jpg', '../images/blanck/0blanck.jpg',]

a = [['corner4', 'lign verticale', 'corner7', 'lign horrizontale', 'corner7', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'SITUATION', 'corner5', 'lign verticale', 'corner6', 'lign horrizontale', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6'],
     ['corner4', 'lign verticale', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner7', 'lign horrizontale', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'SITUATION', 'corner5', 'corner6', 'lign horrizontale', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner5', 'lign horrizontale', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'lign verticale', 'corner5', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6'],
     ['corner4', 'lign verticale', 'corner7', 'lign horrizontale', 'corner7', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'corner7', 'corner7', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'SITUATION', 'lign horrizontale', 'corner5', 'lign verticale', 'corner5', 'corner5', 'lign verticale', 'corner5', 'lign verticale', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner6', 'corner6', 'corner6', 'lign horrizontale', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'lign verticale', 'corner6', 'corner6', 'lign verticale', 'corner6'],
     ['corner4', 'lign verticale', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'lign verticale', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'lign verticale', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner4', 'corner7', 'lign horrizontale', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'corner7', 'lign verticale', 'SITUATION', 'corner5', 'lign verticale', 'corner6', 'lign horrizontale', 'corner6', 'lign verticale', 'corner6', 'corner6', 'lign verticale', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'lign verticale', 'corner5', 'lign verticale', 'corner5', 'lign verticale', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner5', 'corner6', 'lign horrizontale', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'corner6', 'lign verticale', 'corner6', 'corner6', 'lign verticale', 'corner6', 'corner6', 'lign verticale', 'corner6', 'corner6', 'corner6']]


schema = ['corner4', 'lign verticale', 'corner7', 'lign horrizontale', 'corner5', 'corner6']


img = open_picture("ici.png")
copy = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blanck = blanck_picture(img)

dico_picture = picture_schema_dico(picture)

#Sort list last, next picture 
oki_picture = add_list_next_last(picture)

#Treat minini
treat_minini = treat_mini(minini)


for nb in range(len(treat_minini)):
    blanck = blanck_picture(img)

    img1 = open_picture(oki_picture[nb][0])
    img2 = open_picture(oki_picture[nb][1])

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    #Recuperate dimensions of picture
    height, width, chann = img1.shape

    #position of current form
    x = treat_minini[nb][0]
    y = treat_minini[nb][1]

    #Next form in red
    drawing(blanck, gray2, (0, 0, 255))

    copy1 = cv2.resize(blanck, (400, 400))
    show_picture("copy1", copy1, 0, "")



    find = False
    for i in schema:

        if i == "corner4":

            x = treat_minini[nb][0]
            y = treat_minini[nb][1]

            listex = [x+1,        x,        x+1,  x-1]
            listey = [y,          y+1,      y-1,  y+1]

            road_test(listex, listey, width, height, blanck, gray,
                      oki_picture, "corner4", 1, 1, x, y, dico_picture, nb, 1, 0)

        elif i == 'lign verticale':
            for i in range(2):
                

                x = treat_minini[nb][0]
                y = treat_minini[nb][1]

                listex = [x,       x+1,     x+1]
                listey = [y+1,     y+1,      y-1]


                if i == 0:

                    road_test(listex, listey, width, height, blanck, gray,
                              oki_picture, 'lign verticale1', 1, 0, x, y, dico_picture, nb, 0, 0)
                elif i == 1:

                    road_test(listex, listey, width, height, blanck, gray,
                              oki_picture, 'lign verticale2', -1, 0, x, y, dico_picture, nb, 0, 0)


        elif i == 'corner7':

            listex = [x-1,   x,      x+1,   x-1]
            listey = [  y,   y+1,    y+1,   y-1]


            x = treat_minini[nb][0]
            y = treat_minini[nb][1]

            road_test(listex, listey, width, height, blanck, gray,
                      oki_picture, "corner7", -1, 1, x, y, dico_picture, nb, 0, 1)



        elif i == 'lign horrizontale':

            listex = [x+1,   x-1,   x+1,   x-1,   x+1,  x-1]
            listey = [y,       y,   y+1,   y-1,   y-1,  y+1]


            for i in range(2):
                

                x = treat_minini[nb][0]
                y = treat_minini[nb][1]
                
                listex = [x,       x+1,     x+1]
                listey = [y+1,     y+1,      y-1]


                if i == 0:

                    road_test(listex, listey, width, height, blanck, gray,
                              oki_picture, 'lign horrizontale1', 0, -1, x, y, dico_picture, nb, 0, 0)
                elif i == 1:

                    road_test(listex, listey, width, height, blanck, gray,
                              oki_picture, 'lign horrizontale2', 0, 1, x, y, dico_picture, nb, 0, 0)



        elif i == 'corner5':

            listex = [x+1,   x-1,      x,   x+1,  x-1]
            listey = [y,       y,     y-1,  y-1,  y+1]


            x = treat_minini[nb][0]
            y = treat_minini[nb][1]

            road_test(listex, listey, width, height, blanck, gray,
                      oki_picture, "corner5", -1, -1, x, y, dico_picture, nb, 0, 1)



        elif i == 'corner6':

            listex = [x-1,    x,      x+1,   x-1]
            listey = [y,     y-1,    y+1,   y-1] 

            x = treat_minini[nb][0]
            y = treat_minini[nb][1]


            road_test(listex, listey, width, height, blanck, gray,
                      oki_picture, "corner6", -1, 1, x, y, dico_picture, nb, 0, 1)



    print(dico_picture)











