import matplotlib.pyplot as plt
import cv2
import os

from paths import path_blanck

#Show, Open, Create black picture
from starter.operation import open_picture
from starter.operation import show_picture
from starter.operation import blanck_picture

def displaying(original, picture, liste):
    """Here we show the orginal picture
    with part of the current picture
    with detection write in the orginal picture"""

    #Open original picture.
    original = open_picture(original)

    copy = original.copy()

    cv2.rectangle(copy, (liste[0], liste[1]),
                  (liste[0] + liste[2],
                   liste[1] + liste[3]), (0, 0, 255), 1)

    #Open part of orginal picture.
    img = open_picture(picture)

    #Display them in double window.
    plt.subplot(121),plt.imshow(copy)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img) 
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
     
    plt.show()


