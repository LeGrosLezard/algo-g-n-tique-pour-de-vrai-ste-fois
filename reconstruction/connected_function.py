def treat_mini(minini):
    """Recuperate first form and next form"""

    treat_minini = []

    for i in minini:
        treat_minini.append([i[0][0], i[0][1]])
        treat_minini.append([i[1][0], i[1][1]])

    return treat_minini


def treat_shems(liste):
    """Recuperate all schemas expect situation
    who's represent points"""

    schemas_ran = [j for i in liste for j in i if j != "SITUATION"]
    return schemas_ran


def make_dico(schemas_ran):
    """Recuperate all schema into a dico"""

    dico_schema = {}

    for i in schemas_ran:
        dico_schema[i] = 0

    return dico_schema


def drawing(blanck, gray, color):
    """Identify white pixels and draw it on blanck"""

    for y in range(gray.shape[1]):
        for x in range(gray.shape[0]):
            if gray[x, y] > 100:
                blanck[x, y] = color

    return blanck


def end_condition(x , y, c, blanck):
    """If our search points touch a color pixel
    return True"""

    if blanck[x, y][0] == c[0] and\
       blanck[x, y][1] == c[1] and\
       blanck[x, y][2] == c[2]:
        return True
    


def raising(blanck):
    """Raise our search detection"""

    for x in range(blanck.shape[1]):
        for y in range(blanck.shape[0]):
            if blanck[x ,y][0] == 255 and\
               blanck[x, y][1] == 255 and\
               blanck[x, y][2] == 255:
                blanck[x, y] = 0, 0, 0

    return blanck


def picture_schema_dico(picture):
    
    dico_picture = {}

    for i in picture:
        dico_picture[i] = {'corner4':0, 'lign verticale1':0,
                           'lign verticale2':0, 'corner7':0,
                           'lign horrizontale1':0, 'lign horrizontale2':0,
                           'corner5':0, 'corner6':0}
    return dico_picture


def add_list_next_last(picture):


    oki_picture = []
    for i in range(0, len(picture), 1):
        try:
            oki_picture.append([picture[i], picture[i + 1]])
            oki_picture.append([picture[i + 1], picture[i]])
        except:
            pass


    return oki_picture













