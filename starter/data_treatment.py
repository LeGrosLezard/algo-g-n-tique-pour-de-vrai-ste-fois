def delete_same_detection(dico, name, PIT):
    """Here we delete contours with same position""" 
    for nb in range(0, len(dico.items()), 2):
        if dico[name.format(PIT, str(nb))][0] ==\
            dico[name.format(PIT, str(nb + 1))][0]:
            #If same localisation
            if dico[name.format(PIT, str(nb))][1] <=\
               dico[name.format(PIT, str(nb + 1))][1]:
                #delete the higter area
                del dico[name.format(PIT, str(nb))]
            else:
                del dico[name.format(PIT, str(nb + 1))]

    return dico



def put_name(key):
    """Here we only recuperate number from blanck treat
    like blanck0contour.png -> 0"""

    name = ""
    for i in key:
        try:
            i = int(i)
            if i == int(i):
                name += str(i)
        except:
            pass

    return name


dico = {'images/treatment/contour0.png': [(160, 117, 22, 14), 137.5], 'images/treatment/contour2.png': [(35, 69, 26, 53), 424.5], 'images/treatment/contour4.png': [(56, 60, 28, 57), 603.0], 'images/treatment/contour6.png': [(14, 60, 20, 19), 154.0], 'images/treatment/contour8.png': [(89, 58, 52, 67), 997.0], 'images/treatment/contour10.png': [(134, 57, 32, 51), 531.5]}


def sort_forms(dico):
    """We replace dico by a new dico with position of
    crop from original"""

    #print(len(dico))
    dico_treated = {}
    if len(dico) >= 1:

        liste = []
        for key, value in dico.items():
            print(key, value[0])
            liste.append(value[0][0] + value[0][2])

        #print(liste)
        liste = sorted(liste)
        #print(liste)

        for i in liste:
            for key, value in dico.items():
                if value[0][0] + value[0][2] == i:
                    dico_treated[key] = value

    #print(dico_treated)
    return dico_treated
