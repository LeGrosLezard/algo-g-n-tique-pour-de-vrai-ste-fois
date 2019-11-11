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

            listex = [x+1,        x,        x+1,  x-1]
            listey = [y,          y+1,      y-1,  y+1]

            #We stop if we course more 50 pixels
            for counter in range(50):
                if counter == 49:
                    raising(blanck)
                    break

                if x >= width - 10 or y >= height - 10:break


                #We stop if we get pixel form color
                stop = end_condition(x , y, (0, 0, 255), blanck)
                if stop is True:
                    drawing(blanck, gray, (255, 255, 255))

                    #dico remplissage
                    for key, value in dico_picture.items():
                        if key == oki_picture[nb][0]:
                            dico_picture[key]['corner4'] = counter

                    
                    print(counter)
                    raising(blanck)
                    break

                blanck[x, y] = 255, 255, 255
                blanck[x + 1, y] = 255, 255, 255
                copy1 = cv2.resize(blanck, (400, 400))
                show_picture("copy1", copy1, 0, "")
                x += 1
                y += 1




        elif i == 'lign verticale':
            for i in range(2):
                

                x = treat_minini[nb][0]
                y = treat_minini[nb][1]
                
                listex = [x,       x+1,     x+1]
                listey = [y+1,     y+1,      y-1]

                for counter in range(50):
                    if counter == 49:
                        raising(blanck)
                        break

                    if x >= width - 10 or y >= height - 10:break


                    stop = end_condition(x , y, (0, 0, 255), blanck)
                    if stop is True:
                        drawing(blanck, gray, (255, 255, 255))

                        #dico remplissage
                        for key, value in dico_picture.items():
                            if key == oki_picture[nb][0] and i == 0:
                                dico_picture[key]['lign verticale1'] = counter
                            elif key == oki_picture[nb][0] and i == 1:
                                dico_picture[key]['lign verticale2'] = counter

                        
                        print(counter)
                        raising(blanck)
                        break

                    blanck[x, y] = 255, 255, 255
                    copy1 = cv2.resize(blanck, (400, 400))
                    show_picture("copy1", copy1, 0, "")

                    if i == 0:
                        x+=1
                        y

                    elif i == 1:
                        x -= 1




        elif i == 'corner7':

            listex = [x-1,   x,      x+1,   x-1]
            listey = [  y,   y+1,    y+1,   y-1]


            x = treat_minini[nb][0]
            y = treat_minini[nb][1]


            #We stop if we course more 50 pixels
            for counter in range(50):
                if counter == 49:
                    raising(blanck)
                    break

                if x >= width - 10 or y >= height - 10:break

                #We stop if we get pixel form color
                stop = end_condition(x , y, (0, 0, 255), blanck)
                if stop is True:
                    drawing(blanck, gray, (255, 255, 255))
 
                    #dico remplissage
                    for key, value in dico_picture.items():
                        if key == oki_picture[nb][0]:
                            dico_picture[key]['corner7'] = counter
                    
                    print(counter)
                    raising(blanck)
                    break

                blanck[x, y] = 255, 255, 255
                blanck[x, y + 1] = 255, 255, 255
                copy1 = cv2.resize(blanck, (400, 400))
                show_picture("copy1", copy1, 0, "")
                x -= 1
                y += 1




        elif i == 'lign horrizontale':

            listex = [x+1,   x-1,   x+1,   x-1,   x+1,  x-1]
            listey = [y,       y,   y+1,   y-1,   y-1,  y+1]


            for i in range(2):
                

                x = treat_minini[nb][0]
                y = treat_minini[nb][1]
                
                listex = [x,       x+1,     x+1]
                listey = [y+1,     y+1,      y-1]

                for counter in range(50):
                    if counter == 49:
                        raising(blanck)
                        break

                    if x >= width - 10 or y >= height - 10:break

                    stop = end_condition(x , y, (0, 0, 255), blanck)
                    if stop is True:
                        drawing(blanck, gray, (255, 255, 255))

                        for key, value in dico_picture.items():
                            if key == oki_picture[nb][0] and i == 0:
                                dico_picture[key]['lign horrizontale1'] = counter
                            elif key == oki_picture[nb][0] and i == 1:
                                dico_picture[key]['lign horrizontale2'] = counter



                        print(counter)
                        raising(blanck)
                        break

                    blanck[x, y] = 255, 255, 255
                    copy1 = cv2.resize(blanck, (400, 400))
                    show_picture("copy1", copy1, 0, "")

                    if i == 0:
                        y -= 1

                    elif i == 1:
                        y += 1








        elif i == 'corner5':

            listex = [x+1,   x-1,      x,   x+1,  x-1]
            listey = [y,       y,     y-1,  y-1,  y+1]


            x = treat_minini[nb][0]
            y = treat_minini[nb][1]


            #We stop if we course more 50 pixels
            for counter in range(50):
                if counter == 49:
                    raising(blanck)
                    break

                if x >= width - 10 or y >= height - 10:break

                #We stop if we get pixel form color
                stop = end_condition(x , y, (0, 0, 255), blanck)
                if stop is True:
                    drawing(blanck, gray, (255, 255, 255))

                    #dico remplissage
                    for key, value in dico_picture.items():
                        if key == oki_picture[nb][0]:
                            dico_picture[key]['corner5'] = counter

                    
                    print(counter)
                    raising(blanck)
                    break

                blanck[x, y] = 255, 255, 255
                blanck[x, y + 1] = 255, 255, 255
                copy1 = cv2.resize(blanck, (400, 400))
                show_picture("copy1", copy1, 0, "")
                x -= 1
                y -= 1



        elif i == 'corner6':

            listex = [x-1,    x,      x+1,   x-1]
            listey = [y,     y-1,    y+1,   y-1] 

            x = treat_minini[nb][0]
            y = treat_minini[nb][1]


            #We stop if we course more 50 pixels
            for counter in range(50):
                if counter == 49:
                    raising(blanck)
                    break

                if x >= width - 10 or y >= height - 10:break

                #We stop if we get pixel form color
                stop = end_condition(x , y, (0, 0, 255), blanck)
                if stop is True:
                    drawing(blanck, gray, (255, 255, 255))


                    #dico remplissage
                    for key, value in dico_picture.items():
                        if key == oki_picture[nb][0]:
                            dico_picture[key]['corner6'] = counter

                    
                    print(counter)
                    raising(blanck)
                    break

                blanck[x, y] = 255, 255, 255
                blanck[x, y + 1] = 255, 255, 255
                copy1 = cv2.resize(blanck, (400, 400))
                show_picture("copy1", copy1, 0, "")
                x -= 1
                y += 1



    print(dico_picture)











