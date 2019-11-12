import cv2


#==========================================================================
"""Sort lists"""


def display(dico):
    for cle, valeur in dico.items():
        print(cle, valeur)
        print("")


def left_position(liste):
    """Recuperate x + w points from original."""

    liste_placement = sorted([i[0] + i[2] for i in liste])
    #print(liste_placement)

    return liste_placement


def name_position_points(pictures, liste, liste_placement):
    """Recuperate name, points and x + w points from original."""

    dico = {}

    for nb, name in enumerate(pictures):
        for i in liste_placement:
            if liste[nb][0] + liste[nb][2] == i:
                dico[name] = [liste_placement.index(i), liste[nb]]

    #print(dico)
    return dico


def final_informations(points_detection, dico):
    """Sort picture by their left position."""

    liste_position = []
    for i in range(len(points_detection)):
        for key, value in dico.items():
            if value[0] == i:
                liste_position.append([key, value[1]])

    #print(liste_positionnage)
    return liste_position








#==========================================================================
"""Recuperate position from the last and the next picture."""


def placement_next_form_x(position, number):
    """Recuperate x + w position from the first and the next form."""

    left_position_1 = position[number][1][0] + position[number][1][2]
    left_position_2 = position[number + 1][1][0] + position[number + 1][1][2]

    pos_x = 0

    #print(left_position_1, left_position_2)


    if left_position_2 > left_position_1:
        print("next to right of ", abs(left_position_2-left_position_1), "pxs")
        pos_x = "right", abs(left_position_2-left_position_1)
    else:
        print("next to left of ", abs(left_position_2-left_position_1), "pxs")
        pos_x = "left", abs(left_position_2-left_position_1)

    return pos_x


def placement_next_form_y(position, number):
    """Recuperate y position from the first and the next form."""

    pos_y = 0

    top_position_1 = position[number][1][1]
    top_position_2 = position[number + 1][1][1]

    #Placement pixels y axis.

    #print(top_position_1, top_position_2)


    if top_position_1 > top_position_2:
        print("la prochaine en haut de :", abs(top_position_2 - top_position_1), "pxs")
        pos_y = "height", abs(top_position_2 - top_position_1)
    else:
        print("la prochaine en bas de:", abs(top_position_2 - top_position_1), "pxs")
        pos_y = "bottom", abs(top_position_2 - top_position_1)

    return pos_y




#======================================================================
"""Recuperate whites pixels."""


def drawing_gray_on_blanck(gray, blanck):
    """Draw if we find a white pixel"""

    for x in range(gray.shape[1]):
        for y in range(gray.shape[0]):
            if gray[x, y] >= 200:
                blanck[x, y] = 255, 255, 255


def recuperate_white_pixels(gray):
    """Recuperate only x, y and both if it's a white pixel."""

    liste_white_pixels = [[[x, y] for x in range(gray.shape[1])\
                           for y in range(gray.shape[0]) if gray[x, y] >= 200],
                          [x for x in range(gray.shape[1])\
                           for y in range(gray.shape[0]) if gray[x, y] >= 200],
                          [y for x in range(gray.shape[1])\
                           for y in range(gray.shape[0]) if gray[x, y] >= 200]]


    #All points liste_white_pixels[0]
    #X points liste_white_pixels[1]
    #Y points liste_white_pixels[2]

    #print(liste_white_pixels)
    return liste_white_pixels





#======================================================================
"""Recuperate area of extremities."""

def recuperate_extremities(blanck, extremity, liste, points):

    coordinate = [pxs for pxs in liste if pxs[points] == extremity]

    for pxs in liste:
        if pxs[points] == extremity:
            blanck[pxs[0], pxs[1]] = 0, 0, 255

    blanck_copy = cv2.resize(blanck, (800, 800))
    #show_picture("blanckblanck", blanck_copy, 0, "")

    return coordinate






#======================================================================
"""Recuperate minimum distance beetween areas."""


def recup_minimum_points(mini_zone, area_points):
    """We run list form one and next list form.
    We compare distance beetween poitns and recup the minimum distance"""

    #All points
    for nb, _ in enumerate(area_points):

        #minimum value.
        min_val = 100000

        try:
            #First list
            for el_list1 in area_points[nb][0]:
                #Second list
                for el_list2 in area_points[nb + 1][0]:
                    #abs(x1 - x2), abs(y1 - y2)
                    x = abs(el_list1[0] - el_list2[0])
                    y = abs(el_list1[1] - el_list2[1])
                    #Sum(it)
                    E = abs(x + y)

                    #Compare it to minimum value
                    if E < min_val:
                        #Update minimum value
                        mini = []
                        mini.append([el_list1, el_list2]) 
                        min_val = E

            #Add minimums distance points
            for i in mini:
                mini_zone.append(i)

        except IndexError:
            pass


def display_points(mini_zone, blanck):

    for pxs in mini_zone:
        for p in pxs:
            blanck[p[0], p[1]] = 255, 0, 0
