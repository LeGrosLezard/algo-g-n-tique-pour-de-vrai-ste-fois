import matplotlib.pyplot as plt
import cv2
import os



#Show, Open, Create black picture
from operation import open_picture
from operation import show_picture
from operation import blanck_picture

def displaying(picture, liste):
    original = open_picture("images/" + "lign_v1.jpg")

    path = "images/blanck/"
    liste_treat = os.listdir(path)

    for i in range(len(liste_treat)):

        copy = original.copy()

        cv2.rectangle(copy, (liste[i][0], liste[i][1]),
                      (liste[i][0] + liste[i][2],
                       liste[i][1] + liste[i][3]), (0, 0, 255), 1)
        


        img = open_picture(picture[i])

        




        plt.subplot(121),plt.imshow(copy)
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img) 
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
         
        plt.show()


