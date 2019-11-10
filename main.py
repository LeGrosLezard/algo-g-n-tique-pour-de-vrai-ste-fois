import os

#Path of our pictures
from paths import path_image_treatment as PIT

from starter.delimitation import make_contours
from starter.data_treatment import delete_same_detection

from contours_complement.parcourage import redraw_contour



#Recuperate contours and save it.
name = "{}contour{}.png"
image_path = r"C:\Users\jeanbaptiste\Desktop\chaipas\images\lign_v1.jpg"
dico_data = make_contours(image_path)
dico_data = delete_same_detection(dico_data, name, PIT)

#Run these contours and rebuild their contours.
for key, value in dico_data.items():
    redraw_contour(key)
    


    
