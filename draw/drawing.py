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

#nos pts de zone
area = [[[[60, 33], [61, 33], [62, 33], [63, 33], [64, 33],
          [65, 33], [69, 14], [70, 14], [71, 14], [72, 14],
          [73, 14], [74, 14], [75, 14], [76, 14], [77, 14],
          [78, 14], [78, 14], [78, 15], [78, 16], [78, 17],
          [78, 18], [78, 19], [60, 28], [60, 29], [60, 30],
          [60, 31], [60, 32], [60, 33]]], [[[109, 60], [110, 60], [111, 60], [112, 60], [113, 60], [71, 35], [72, 35], [73, 35], [74, 35], [75, 35], [76, 35], [77, 35], [78, 35], [79, 35], [80, 35], [81, 35], [82, 35], [83, 35], [84, 35], [85, 35], [86, 35], [87, 35], [88, 35], [89, 35], [90, 35], [91, 35], [92, 35], [93, 35], [94, 35], [95, 35], [96, 35], [97, 35], [98, 35], [99, 35], [100, 35], [101, 35], [102, 35], [103, 35], [104, 35], [105, 35], [106, 35], [107, 35], [108, 35], [109, 35], [110, 35], [111, 35], [121, 43], [121, 44], [121, 45], [121, 46], [121, 47], [121, 48], [121, 49], [121, 50], [121, 51], [121, 52], [121, 53], [121, 54], [121, 55], [69, 37], [69, 38], [69, 39], [69, 40]]], [[[109, 83], [110, 83], [111, 83], [112, 83], [113, 83], [114, 83], [115, 83], [116, 83], [95, 56], [96, 56], [97, 56], [98, 56], [99, 56], [100, 56], [101, 56], [102, 56], [103, 56], [116, 79], [116, 80], [116, 81], [116, 82], [116, 83], [60, 66], [60, 67], [60, 68], [60, 69]]], [[[94, 140], [95, 140], [96, 140], [97, 140], [98, 140], [99, 140], [100, 140], [101, 140], [102, 140], [103, 140], [104, 140], [105, 140], [106, 140], [107, 140], [108, 140], [109, 140], [108, 89], [109, 89], [110, 89], [111, 89], [112, 89], [113, 89], [114, 89], [115, 89], [116, 89], [117, 89], [124, 126], [124, 127], [124, 128], [124, 129], [124, 130], [124, 131], [58, 102], [58, 103], [58, 104], [58, 105], [58, 106], [58, 107], [58, 108], [58, 109], [58, 110]]], [[[76, 165], [77, 165], [78, 165], [79, 165], [80, 165], [81, 165], [82, 165], [83, 165], [84, 165], [85, 165], [86, 165], [87, 165], [88, 165], [89, 165], [90, 165], [91, 165], [92, 165], [93, 165], [94, 165], [95, 165], [96, 165], [97, 165], [98, 165], [99, 165], [100, 165], [101, 165], [102, 165], [103, 165], [104, 165], [105, 165], [106, 165], [107, 165], [83, 134], [84, 134], [85, 134], [86, 134], [87, 134], [88, 134], [107, 159], [107, 160], [107, 161], [107, 162], [107, 163], [107, 164], [107, 165], [57, 146], [57, 147], [57, 148], [57, 149], [57, 150], [57, 151], [57, 152]]], [[[125, 181], [126, 181], [127, 181], [128, 181], [129, 181], [117, 160], [118, 160], [119, 160], [130, 175], [130, 176], [130, 177], [130, 178], [130, 179], [130, 180], [117, 160], [117, 161], [117, 162], [117, 163], [117, 164], [117, 165], [117, 166], [117, 167]]]]

#nos pts de départ
c = [[65, 33], [71, 35], [109, 60], [103, 56], [109, 83], [109, 89], [94, 140], [88, 134], [107, 165], [117, 165]]



img = open_picture(r"C:\Users\jeanbaptiste\Desktop\chaipas\images\lign_v1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blanck = blanck_picture(img)



counter = 0

for key, value in a.items():
    min_value = 10000
    data = ""
    print(key, oki_picture[counter])

    for key1, value1 in a[key].items():

        if value1 != 0:
            print(value1)
            if value1[0] < min_value:
                min_value = value1[0]
                data  = [key1, value1]

    print(min_value)
    print("")




##    print(data)
##    print("zone ", b[c])
##    print("")

    counter+=1



























