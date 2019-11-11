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


picture = ['../images/blanck/6blanck.jpg', '../images/blanck/2blanck.jpg', '../images/blanck/4blanck.jpg',
           '../images/blanck/8blanck.jpg', '../images/blanck/10blanck.jpg', '../images/blanck/0blanck.jpg',]


a = {'../images/blanck/6blanck.jpg': {'corner4': [4, 69, 37], 'lign verticale1': 0, 'lign verticale2': 0, 'corner7': 0, 'lign horrizontale1': 0, 'lign horrizontale2': 0, 'corner5': 0, 'corner6': 0}, '../images/blanck/2blanck.jpg': {'corner4': 0, 'lign verticale1': 0, 'lign verticale2': 0, 'corner7': 0, 'lign horrizontale1': [13, 71, 22], 'lign horrizontale2': 0, 'corner5': 0, 'corner6': 0}, '../images/blanck/4blanck.jpg': {'corner4': 0, 'lign verticale1': [6, 109, 56], 'lign verticale2': 0, 'corner7': 0, 'lign horrizontale1': 0, 'lign horrizontale2': 0, 'corner5': 0, 'corner6': 0}, '../images/blanck/8blanck.jpg': {'corner4': 0, 'lign verticale1': 0, 'lign verticale2': 0, 'corner7': 0, 'lign horrizontale1': [6, 109, 83], 'lign horrizontale2': 0, 'corner5': 0, 'corner6': 0}, '../images/blanck/10blanck.jpg': {'corner4': [6, 94, 140], 'lign verticale1': 0, 'lign verticale2': 0, 'corner7': 0, 'lign horrizontale1': 0, 'lign horrizontale2': 0, 'corner5': 0, 'corner6': 0}, '../images/blanck/0blanck.jpg': {'corner4': 0, 'lign verticale1': 0, 'lign verticale2': [10, 107, 165], 'corner7': 0, 'lign horrizontale1': 0, 'lign horrizontale2': 0, 'corner5': 0, 'corner6': 0}}

b = {'../images/blanck/6blanck.jpg': {'corner4': 0, 'lign verticale1': 0, 'lign verticale2': 0, 'corner7': 0, 'lign horrizontale1': 0, 'lign horrizontale2': 0, 'corner5': 0, 'corner6': 0}, '../images/blanck/2blanck.jpg': {'corner4': 0, 'lign verticale1': 0, 'lign verticale2': [6, 103, 60], 'corner7': [15, 94, 75], 'lign horrizontale1': 0, 'lign horrizontale2': [16, 109, 76], 'corner5': [5, 66, 30], 'corner6': 0}, '../images/blanck/4blanck.jpg': {'corner4': [6, 115, 89], 'lign verticale1': 0, 'lign verticale2': 0, 'corner7': [8, 101, 91], 'lign horrizontale1': [15, 103, 41], 'lign horrizontale2': [6, 109, 89], 'corner5': [15, 88, 41], 'corner6': [11, 114, 45]}, '../images/blanck/8blanck.jpg': {'corner4': 0, 'lign verticale1': 0, 'lign verticale2': [6, 88, 140], 'corner7': [18, 76, 158], 'lign horrizontale1': 0, 'lign horrizontale2': [19, 94, 159], 'corner5': [6, 88, 134], 'corner6': [6, 115, 83]}, '../images/blanck/10blanck.jpg': {'corner4': 0, 'lign verticale1': [10, 117, 165], 'lign verticale2': 0, 'corner7': 0, 'lign horrizontale1': [13, 88, 121], 'lign horrizontale2': 0, 'corner5': [13, 75, 121], 'corner6': [13, 101, 121]}, '../images/blanck/0blanck.jpg': {'corner4': 0, 'lign verticale1': 0, 'lign verticale2': 0, 'corner7': 0, 'lign horrizontale1': 0, 'lign horrizontale2': 0, 'corner5': [29, 88, 136], 'corner6': 0}}

c = [[65, 33], [71, 35], [109, 60], [103, 56], [109, 83], [109, 89], [94, 140], [88, 134], [107, 165], [117, 165]]




img = open_picture(r"C:\Users\jeanbaptiste\Desktop\chaipas\images\lign_v1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blanck = blanck_picture(img)



counter = 0

for key, value in a.items():
    min_value = 10000
    data = ""

    for key1, value1 in a[key].items():
        if value1 != 0:
            if value1[0] < min_value:
                min_value = value1[0]
                data  = [key1, value1]

    print(min_value)

##    print(data)
##    print("zone ", b[c])
##    print("")

    counter+=1
























