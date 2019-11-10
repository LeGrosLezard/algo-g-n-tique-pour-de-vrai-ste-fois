import os

#Path of our pictures
from paths import path_image_treatment as PIT

from parcourage import redraw_contour

#We make the treated picture into a list.
liste_treat = os.listdir(PIT)

#We crop last points of the draw.
#Now we course the folder.
for pict in liste_treat:
    redraw_contour(PIT + pict)
