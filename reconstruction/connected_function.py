import cv2
from starter.operation import open_picture
from starter.operation import show_picture
import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\chaipas")

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




def road_test(listex, listey, width, height, blanck, gray, oki_picture,
              section, nb1, nb2, x, y, dico_picture, nb, nb_add1, nb_add2):

    """We course 50 pixels. If we course all of them stop
    If we are less -10 width or height stop
    If we meet a red pixel stop and count last run
    increment x or y
    """

    #Course 50 pixels.
    for counter in range(50):
        if counter == 49:
            raising(blanck)
            break

        #Break if we pass border of picture.
        if x >= width - 10 or y >= height - 10:
            raising(blanck)
            break

        #Stop if we meet red pixel.
        stop = end_condition(x , y, (0, 0, 255), blanck)
        if stop is True:
            drawing(blanck, gray, (255, 255, 255))

            #Add it to schema dictionnary
            for key, value in dico_picture.items():
                if key == oki_picture[nb][0]:
                    dico_picture[key][section] = [counter, x, y]

            #Raise white pixel for display
            raising(blanck)
            break

        #Put pixel.
        blanck[x, y] = 255, 255, 255
        
        blanck[x + nb_add1, y + nb_add2] = 255, 255, 255
        copy1 = cv2.resize(blanck, (400, 400))
        show_picture("copy1", copy1, 1, "")
        x += nb1
        y += nb2








