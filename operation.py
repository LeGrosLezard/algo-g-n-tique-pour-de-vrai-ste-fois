import cv2
import numpy as np


import time
def open_picture(image):
    """We open picture for read it."""

    img = cv2.imread(image)
    return img


def show_picture(name, image, mode, destroy):
    """We Show the picture

        - mode 1 is for an automatic display,
        - mode 0 wait a press key for destroy picture,
        -destroy y is for remove picture.
    """


    cv2.imshow(name, image)
    cv2.waitKey(mode)

    if destroy == "y":
        cv2.destroyAllWindows()



def save_picture(name, picture):
    """saving picture we need:

        - his name "".extension,
        - the picture readed.
        
    """

    cv2.imwrite(name, picture)



def blanck_picture(img):
    """ Create a black picture bgr, we need:

        - his dimensions (width and height),
        - his color (0, 0, 0) is blanck default.

    """

    blank_image = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
    blank_image[0:, 0:] = 0, 0, 0

    return blank_image



def find_first_points(gray):


    pointsx = []  #x pos
    pointsy = []  #y pos

    #We search the first left top white point.
    for y in range(gray.shape[1]):
        for x in range(gray.shape[0]):
            if gray[x ,y] == 255:
                pointsx.append([x, y])

    #First left top white point.
    x = pointsx[0][0]
    y = pointsx[0][1]

    return x, y



def incrementation(x, y, number1, number2, copy, mode):
    """We increment our position if we take descision
to move on this point"""

    x = x + number1
    y = y + number2

    
    if mode == "color_copy":
        copy[x, y]  = 0, 0, 255

    return x, y
