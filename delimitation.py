#Library
import cv2

#Opening, Displaying, Creating picture.
from operation import open_picture
from operation import show_picture
from operation import blanck_picture

from paths import path_image_treatment as PIT


#Contours parameters
R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE

#Name variable
counter = 0

#Openning picture
img = open_picture('images/lign_v1.jpg')

#Gray and edges filters.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img, 255,200)

#Contours are writte into a black picture.
contours, _ = cv2.findContours(edges, R, P)
for cnts in contours:

    blanck = blanck_picture(img)
    cv2.drawContours(blanck, [cnts], -1, (255,255,255), 1)

    name = PIT + "contour" + str(counter) + ".png"
    cv2.imwrite(name, blanck)

    counter += 1














