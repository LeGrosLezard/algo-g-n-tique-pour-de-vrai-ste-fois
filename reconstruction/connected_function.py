

def treat_mini(minini):
    treat_minini = []
    for i in minini:
        treat_minini.append([i[0][0][0], i[0][0][1]])
        treat_minini.append([i[0][1][0], i[0][1][1]])
    return treat_minini


def treat_shems(liste):

    b = [j for i in liste for j in i if j != "SITUATION"]
    return b

def make_dico(b):
    dico_schema = {}
    for i in b:
        dico_schema[i] = 0

    return dico_schema


def color_it(color, picture, blanck):

    for y in range(picture.shape[1]):
        for x in range(picture.shape[0]):
            if picture[x, y] > 100:
                blanck[x, y] = color
    return blanck

def end_condition(x , y, c, blanck):

    if blanck[x, y][0] == c[0] and\
       blanck[x, y][1] == c[1] and\
       blanck[x, y][2] == c[2]:
        return True
    
def drawing(blanck, gray):
    for x in range(gray.shape[1]):
        for y in range(gray.shape[0]):
            if gray[x, y] > 100:
                blanck[x, y] = 255, 255, 255

def raising(blanck):

    for x in range(blanck.shape[1]):
        for y in range(blanck.shape[0]):
            if blanck[x ,y][0] == 255 and\
               blanck[x, y][1] == 255 and\
               blanck[x, y][2] == 255:
                blanck[x, y] = 0, 0, 0

    return blanck





