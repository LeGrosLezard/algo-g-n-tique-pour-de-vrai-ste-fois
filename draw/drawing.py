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


#nos images
picture = ['../images/blanck/6blanck.jpg', '../images/blanck/2blanck.jpg', '../images/blanck/4blanck.jpg',
           '../images/blanck/8blanck.jpg', '../images/blanck/10blanck.jpg', '../images/blanck/0blanck.jpg',]

#image regroupé pts to pts
oki_picture = [['../images/blanck/6blanck.jpg', '../images/blanck/2blanck.jpg'],
               ['../images/blanck/2blanck.jpg', '../images/blanck/6blanck.jpg'],
               ['../images/blanck/2blanck.jpg', '../images/blanck/4blanck.jpg'],
               ['../images/blanck/4blanck.jpg', '../images/blanck/2blanck.jpg'],
               ['../images/blanck/4blanck.jpg', '../images/blanck/8blanck.jpg'],
               ['../images/blanck/8blanck.jpg', '../images/blanck/4blanck.jpg'],
               ['../images/blanck/8blanck.jpg', '../images/blanck/10blanck.jpg'],
               ['../images/blanck/10blanck.jpg', '../images/blanck/8blanck.jpg'],
               ['../images/blanck/10blanck.jpg', '../images/blanck/0blanck.jpg'],
               ['../images/blanck/0blanck.jpg', '../images/blanck/10blanck.jpg']]

#nos shémas
a = {'0': {'corner4': [4, 69, 37], 'lign verticale1': 0,
           'lign verticale2': 0, 'corner7': 0,
           'lign horrizontale1': 0, 'lign horrizontale2': 0,
           'corner5': 0, 'corner6': 0},
     '1': {'corner4': 0, 'lign verticale1': 0, 'lign verticale2': 0,
           'corner7': 0, 'lign horrizontale1': [13, 71, 22],
           'lign horrizontale2': 0, 'corner5': [5, 66, 30], 'corner6': 0},
     '2': {'corner4': 0, 'lign verticale1': 0, 'lign verticale2': [6, 103, 60],
           'corner7': [15, 94, 75], 'lign horrizontale1': 0, 'lign horrizontale2': [16, 109, 76],
           'corner5': 0, 'corner6': 0},
     '3': {'corner4': 0, 'lign verticale1': [6, 109, 56], 'lign verticale2': 0,
           'corner7': 0, 'lign horrizontale1': [15, 103, 41], 'lign horrizontale2': 0,
           'corner5': [15, 88, 41], 'corner6': [11, 114, 45]},
     '4': {'corner4': [6, 115, 89], 'lign verticale1': 0, 'lign verticale2': 0,
           'corner7': [8, 101, 91], 'lign horrizontale1': 0, 'lign horrizontale2': [6, 109, 89],
           'corner5': 0, 'corner6': 0},
     '5': {'corner4': 0, 'lign verticale1': 0, 'lign verticale2': 0, 'corner7': 0,
           'lign horrizontale1': [6, 109, 83], 'lign horrizontale2': 0,
           'corner5': [8, 101, 81], 'corner6': [6, 115, 83]},
     '6': {'corner4': 0, 'lign verticale1': 0, 'lign verticale2': [6, 88, 140],
           'corner7': [18, 76, 158], 'lign horrizontale1': 0, 'lign horrizontale2': [19, 94, 159],
           'corner5': [6, 88, 134], 'corner6': 0},
     '7': {'corner4': [6, 94, 140], 'lign verticale1': [6, 94, 134], 'lign verticale2': 0,
           'corner7': 0, 'lign horrizontale1': [13, 88, 121], 'lign horrizontale2': 0,
           'corner5': [13, 75, 121], 'corner6': [13, 101, 121]},
     '8': {'corner4': 0, 'lign verticale1': [10, 117, 165], 'lign verticale2': 0, 'corner7': 0,
           'lign horrizontale1': 0, 'lign horrizontale2': 0, 'corner5': 0, 'corner6': 0},
     '9': {'corner4': 0, 'lign verticale1': 0, 'lign verticale2': [10, 107, 165], 'corner7': 0,
           'lign horrizontale1': 0, 'lign horrizontale2': 0, 'corner5': [29, 88, 136], 'corner6': 0}}



##          #0     #1     #2    #3      #4     #5     #6    #7
##listex = [x+1,   x-1,   x,    x,      x+1,   x-1,   x+1,  x-1]
##listey = [y,       y,   y+1,  y-1,    y+1,   y-1,   y-1,  y+1]



img = open_picture(r"C:\Users\jeanbaptiste\Desktop\chaipas\images\lign_v1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)





liste = []

counter = 0

for key, value in a.items():
    min_value = 10000
    data = ""

    for key1, value1 in a[key].items():

        if value1 != 0:
            if value1[0] < min_value:
                min_value = value1[0]
                data  = [key1, value1]

    liste.append(data)
    #print(data)
    #print("")




##    print(data)
##    print("zone ", b[c])
##    print("")

    counter+=1

def draw_shema(number, schema, posX, posY, blanck):

    x = posX
    y = posY


    for i in range(number):
        blanck[x, y] = 255, 255, 255

        if schema == "corner4":
            x -= 1; y-= 1
            blanck[x+1, y] = 255, 255, 255

        if schema == "corner7":
            x += 1; y-= 1
            blanck[x, y-1] = 255, 255, 255

        if schema == "corner5":
            x += 1; y+= 1
            blanck[x, y+1] = 255, 255, 255

        if schema == "corner6":
            x -= 1; y+= 1
            blanck[x, y+1] = 255, 255, 255

        if schema == "lign horrizontale1":y += 1;
        if schema == "lign horrizontale2":y -= 1;
        if schema == "lign verticale1":x -= 1;
        if schema == "lign verticale2":x += 1;


    return x, y


blanck = blanck_picture(img)
for pict in range(len(oki_picture)):
    
    print(oki_picture[pict])
    print(liste[pict])

    form1 = open_picture(oki_picture[pict][0])
    form1 = cv2.cvtColor(form1, cv2.COLOR_BGR2GRAY)

    form2 = open_picture(oki_picture[pict][1])
    form2 = cv2.cvtColor(form2, cv2.COLOR_BGR2GRAY)


    for i in range(len(oki_picture[pict])):

        if i == 0:
            form1 = form1
            form2 = form2
        else:
            form1 = form2
            form2 = form1

        for x in range(form1.shape[0]):
            for y in range(form1.shape[1]):
                if form1[x, y] > 100:
                    blanck[x, y] = 255, 255, 255

        liste_w = []
        for x in range(form1.shape[0]):
            for y in range(form1.shape[1]):
                if form1[x, y] > 100:
                    liste_w.append([x, y])

        print(liste_w)
        if i == 0:
            zone = draw_shema(liste[pict][1][0], liste[pict][0],
                                liste[pict][1][1], liste[pict][1][2], blanck)



            for el in liste_w:
                if el[0] > zone[0]-3 and el[0] < zone[0] + 3:
                    print(abs((el[0] + el[1]) - (zone[0] + zone[1])))
                    if abs((el[0] + el[1]) - (zone[0] + zone[1])) < 10:
                        blanck[el[0], el[1]] = 0, 0, 255

                elif el[1] > zone[1]-3 and el[1] < zone[1] + 3:
                    print(abs((el[0] + el[1]) - (zone[0] + zone[1])))
                    if abs((el[0] + el[1]) - (zone[0] + zone[1])) < 10:
                        blanck[el[0], el[1]] = 0, 0, 255


            print(zone)

            copy1 = cv2.resize(blanck, (800, 400))
            show_picture("copy1", copy1, 0, "")

    print("")



