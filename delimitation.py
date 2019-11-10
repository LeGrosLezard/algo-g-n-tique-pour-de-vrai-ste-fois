#Library
import cv2

#Opening, Displaying, Creating picture.
from operation import open_picture
from operation import show_picture
from operation import blanck_picture

from paths import path_image_treatment as PIT

def crop_contour(pict):
    #Contours parameters
    R = cv2.RETR_TREE
    P = cv2.CHAIN_APPROX_NONE

    #Name variable
    counter = 0

    #Openning picture
    img = open_picture(pict)
    #copy = img.copy()



    #Gray and edges filters.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img, 255,200)

    picture = []
    liste_position = []
    area_list = []
    #Contours are writte into a black picture.
    contours, _ = cv2.findContours(edges, R, P)
    for cnts in contours:

        blanck = blanck_picture(img)
        cv2.drawContours(blanck, [cnts], -1, (255,255,255), 1)
        x, y, w, h = cv2.boundingRect(cnts)

        #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        show_picture("img", img, 0, "")

        liste_position.append([x, y, w, h])

        name = PIT + "contour" + str(counter) + ".png"
        picture.append(name)
        area_list.append(cv2.contourArea(cnts))
        #print(name)
        cv2.imwrite(name, blanck)

        counter += 1

    print(area_list)
    print(picture)
    print(liste_position)










