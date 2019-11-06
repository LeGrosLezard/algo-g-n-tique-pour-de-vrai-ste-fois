import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from operation import open_picture
from operation import show_picture
from operation import blanck_picture


def recup_contours(img):

    edges = cv2.Canny(img, 255,200)
    contours, _ = cv2.findContours(edges, R, P)

    for cnts in contours:
        cv2.drawContours(blanck, [cnts], -1, (255,255,255), 1)
        #cv2.fillPoly(blanck, pts =[cnts], color=(255, 255, 255))
        (x, y, w, h) = cv2.boundingRect(cnts)

    return blanck



R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE


img = open_picture('images/lign_v1.jpg')
copy = img.copy()
blanck = blanck_picture(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blanck = recup_contours(img)
blanck = cv2.cvtColor(blanck, cv2.COLOR_BGR2GRAY)



pointsx = []
pointsy = []

for y in range(blanck.shape[1]):
    for x in range(blanck.shape[0]):

        if blanck[x ,y] == 255:
            pointsx.append([x, y])
            pointsy.append(y)

x = pointsx[0][0]
y = pointsx[0][1]


copy[x, y] = 0, 0, 255





def incrementation(x, y, number1, number2, copy):

    x = x + number1
    y = y + number2

    copy[x, y]  = 0, 0, 255

    return x, y



def corner(current, copy, blanck):
    zero=0;un=0;deux=0;trois=0;quattre=0;
    six=0;sept=0;

    for i in current:
        if i == 7:
            sept += 1
        if i == deux:
            deux += 1

    if deux == 0 and sept == 1:
        copy[x , y + 1] = 0, 0, 255
        blanck[x, y + 1] = 255
        print("cooorner")
        


def no_bloc(last, current):

    zero=0;un=0;deux=0;trois=0;
    for i in last:
        if i == 0:zero += 1
        if i == 1:un += 1
        if i == 2:deux += 1
        if i == 3:trois += 1

    if zero == 1:
        for i in current:
            if i == 1:
                current.remove(i)
    if un == 1:
        for i in current:
            if i == 0:
                current.remove(i)

    if deux == 1:
        for i in current:
            if i == 3:
                current.remove(i)

    if trois == 1:
        for i in current:
            if i == 2:
                current.remove(i)
    
    return current



def diagonale(current):

    zero=0;un=0;deux=0;trois=0;quattre=0;
    for i in current:
        if i == 0:
            zero += 1
        if i == 3:
            trois += 1

        if i == 2:
            deux += 1

        if i == 4:
            quattre += 1


    #print(zero,un,deux,trois,quattre)

    if zero == 1 and quattre == 1 :
        current.remove(4)
        print("diagolane removed")
    if deux == 1 and quattre == 1:
        current.remove(4)
        print("diagolane removed")



    return current



def arrierre_avant(historic, current, x, y):

    sept=0;six=0;

    if len(historic) >= 3:
        for i in current:
            if i == 6:six += 1
            if i == 7: sept += 1

        if x + 1 == historic[-2][0] and\
           y - 1 == historic[-2][1]:
            current.remove(6)

        if x - 1 == historic[-2][0] and\
           y + 1 == historic[-2][1]:
            current.remove(7)
        
    return current


def corner_to_lign(current, last):
    
    zero=0;un=0;deux=0;trois=0;quattre=0;
    six=0;sept=0;
    
    if len(last) > 0:
        for i in current:
            if i == 0:zero += 1
            if i == 1: un += 1
            if i == 0:trois += 1
            if i == 1: quattre += 1


        if last[0] == 7 and\
           zero == 1 and un == 1:
            current.remove(0)

        if last[0] == 6 and\
           zero == 1 and un == 1:
            current.remove(1) 


    return current


last = []
historic = []
t = 0
while True:

    current = []

    listex = [x+1,   x-1,   x,    x,      x+1,   x-1,   x+1,  x-1]
    listey = [y,       y,   y+1,  y-1,    y+1,   y-1,   y-1,  y+1]


    

    for i in range(len(listex)):
        if blanck[listex[i], listey[i]] == 255:
            current.append(i)

    if t == 0 and len(current) > 1:
        current = [current[0]]
        t += 1

    print(last)
    print(current)

    corner(current, copy, blanck)
    current = no_bloc(last, current)
    current = diagonale(current)
    current = arrierre_avant(historic, current, x, y)
    current = corner_to_lign(current, last)
    print(current)
    
    historic.append([x, y])

    print(x, y)
    for i in current:

        if i == 0:

            print("zero")
            x, y = incrementation(x, y, 1, 0, copy)
            last = []
            last.append(0)
            break
        if i == 1:

            print("un")
            x, y = incrementation(x, y, -1, 0, copy)
            last = []
            last.append(1)
            break


        elif i == 2:

            print("deux")
            x, y = incrementation(x, y, 0, 1, copy)
            last = []
            last.append(2)
            break

        elif i == 3:
            print("trois")
            break

        elif i == 4:
            print("quattre")
            break

        elif i == 5:
            print("cinq")
            break

        elif i == 6:
            print("six")
            break


        elif i == 7:
            print("sept")
            x, y = incrementation(x, y, -1, 1, copy)
            last = []
            last.append(7)
            break

    print(x, y)
    print("")




    #copy[78, 16] = 255, 0, 0

    copy1 = copy.copy()
    cv2.imwrite("ici.png", copy1)
    cv2.imwrite("iciblanck.png", blanck)
    copy1 = cv2.resize(copy1, (800, 800))
    show_picture("copy1", copy1, 0, "")
























