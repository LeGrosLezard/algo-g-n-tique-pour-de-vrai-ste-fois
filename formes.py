#for paths
import os

#Librairy for treating pictures
import cv2
from PIL import Image

#Here numpy generate matrix
import numpy as np

#Show, Open, Create black picture
from operation import open_picture
from operation import show_picture
from operation import blanck_picture


path = "images/blanck/"

#We make the treated picture into a list.
liste_treat = os.listdir(path)

for pict in liste_treat:
    img = open_picture(path + pict)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)















































    gray_resize = cv2.resize(gray, (800, 800))
    show_picture("gray_resize", gray_resize, 0, "")
































