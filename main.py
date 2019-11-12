import os

#Path of our pictures
from paths import path_image_treatment as PIT


name = "{}contour{}.png"
image_path = r"C:\Users\jeanbaptiste\Desktop\chaipas\images\lign_v1.jpg"



if __name__ == "__main__":

    #
    from starter.delimitation import make_contours
    dico_data = make_contours(image_path)

    #
    from starter.data_treatment import delete_same_detection
    dico_data = delete_same_detection(dico_data, name, PIT)
    #print(dico_data)
##
##    #Run these contours and rebuild their contours and recup
##    #their schemas.
##    for key, value in dico_data.items():
##
##
##        #
##        from starter.data_treatment import put_name
##        name = put_name(key)
##
##        #
##        from contours_complement.parcourage import redraw_contour
##        historic, histo_current = redraw_contour(key, name)
##        #print(historic, histo_current)


    #Let's show part of pictures.
    for key, value in dico_data.items():
        #print(key, value[0])
        #
        from data_regroupement.display import displaying
        displaying(image_path, key, value[0])

    














