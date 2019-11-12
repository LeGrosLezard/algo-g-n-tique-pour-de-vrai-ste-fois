import os

#Path of our pictures
from paths import path_image_treatment as PIT


name = "{}contour{}.png"
image_path = r"C:\Users\jeanbaptiste\Desktop\chaipas\images\lign_v1.jpg"



if __name__ == "__main__":

    #
    from starter.delimitation import make_contours
    dico_data = make_contours(image_path)
    #print(dico_data)

    #
    from starter.data_treatment import delete_same_detection
    dico_data = delete_same_detection(dico_data, name, PIT)
    #print(dico_data)

    from starter.data_treatment import sort_forms
    dico_data = sort_forms(dico_data)
    print(dico_data)


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


##    #Let's show part of pictures.
##    for key, value in dico_data.items():
##        #print(key, value[0])
##        #
##        from data_regroupement.display import displaying
##        displaying(image_path, key, value[0])


##    from data_regroupement.formes import main_formes
##    data = [[key for key, value in dico_data.items()],
##            [list(value[0]) for key, value in dico_data.items()]]
##
##    #print("\n", data[0], "\n", data[1])
##
##    mini_zone, area_points = main_formes(data[0], data[1], image_path)
##
##    print(mini_zone, "\n\n\n", area_points)


##    liste_information = []
##    from data_regroupement.points import points_placements
##    for key, value in dico_data.items():
##        #print(keyn value[0])
##        liste_information.append([key, [list(value)]])
##    #print(liste_information)
##    points_placements(image_path, liste_information)













