import cv2

#Variables
R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE


def recup_contours(img, blanck):
    """Recuperate all contour from a binarized picture"""

    edges = cv2.Canny(img, 255,200)
    contours, _ = cv2.findContours(edges, R, P)

    for cnts in contours:
        cv2.drawContours(blanck, [cnts], -1, (255,255,255), 1)
        #cv2.fillPoly(blanck, pts =[cnts], color=(255, 255, 255))
        (x, y, w, h) = cv2.boundingRect(cnts)

    return blanck


def neightboors_points(liste):
    """Here we ask all points  if they're white
around our position."""


    name = {"0":"zero", "1":"un", "2": "deux",
            "3":"trois", "4":"quattre",
            "5":"cinq", "6":"six",
            "7":"sept"}

    neightboors = {"zero":0, "un":0, "deux":0,
                    "trois":0, "quattre":0,
                    "cinq":0, "six":0,
                    "sept":0}

    for i in liste:
        for key, value in name.items():
            if str(i) == key:
                for key_name, value_name in neightboors.items():
                    if value == key_name:
                        neightboors[key_name] += 1

    return neightboors



def no_bloc(last, current):
    """We search all points around our points.
    If last move was x + 1, we delete the x - 1 detection
    Where 1) we are to x we go to x + 1. Detection give us 2)"""


    #   x                 x-1
    #          ->      
    #  x+1                 x

    #   1)                 2)


    neightboor = neightboors_points(last)

    if neightboor["zero"] == 1:current.remove(1)
    if neightboor["un"] == 1:current.remove(0)
    if neightboor["deux"] == 1:current.remove(3)
    if neightboor["trois"] == 1:current.remove(2)
    if neightboor["quattre"] == 1:
        current.remove(3)
        current.remove(5)


    return current




def diagonale(current):
    """We delete diagonal. x is our last run.
We want to go x -> 2 then 4"""

    #   x    x   2
    #            4  

    neightboor = neightboors_points(current)


    if neightboor["zero"] == 1 and\
       neightboor["quattre"] == 1 or\
       neightboor["deux"] == 1 and\
       neightboor["quattre"] == 1:
        current.remove(4)
        #print("diagonale removed")


    #square
    if neightboor["un"] == 1 and\
       neightboor["cinq"] == 1:
        current.remove(1)
        #print("square")


    return current



def arrierre_avant(historic, current, x, y, last):
    """We ask historic and last list if we gone on this
position.
Historic recup all points from the begening, last recup the last
point."""

    six_removed = False

    if len(historic) >= 3:
        if x + 1 == historic[-2][0] and\
           y - 1 == historic[-2][1]:
            current.remove(6)
            six_removed = True

        if x - 1 == historic[-2][0] and\
           y + 1 == historic[-2][1]:
            current.remove(7)


    


    neightboor = neightboors_points(current)
    if len(last) > 0:
        if last[0] == 7 and\
            neightboor["zero"] == 1 and\
            neightboor["six"] == 1:
            current.remove(0)
            current.remove(6)
            six_removed = True

        if last[0] == 5 and\
           neightboor["deux"] == 1:
            current.remove(2)

        if last[0] == 2 and\
           neightboor["six"] == 1 and\
           six_removed is False:
            current.remove(6)

        if last[0] == 1 and\
           neightboor["quattre"] == 1:
            current.remove(4)

        if last[0] == 6 and\
           neightboor["un"] == 1:
            current.remove(1)




    return current



def corner_to_lign(current, last):
    """We remove this"""


    #  last
    #        current                              1)
    #                 next points




    #  last
    #          last                                 2)
    #       to remove   current




    neightboor = neightboors_points(current)
    
    if len(last) > 0:

        if last[0] == 7 and\
           neightboor["zero"] == 1 and\
           neightboor["un"] == 1:
            current.remove(0)

        if last[0] == 6 and\
           neightboor["zero"] == 1 and\
           neightboor["un"] == 1:
            current.remove(1) 


    return current



def speciale_corner_after_selection(current, copy, blanck, x, y):
    """Here if we move in diagonal, we complete
the corner like"""


    # last
    #        current
    #      to complete   next position

    out = ""
    if current[0] == 4:
        copy[x + 1, y]  = 0, 0, 255
        blanck[x + 1, y]  = 255
        #print("special corner 4")
        out = x + 1, y

    if current[0] == 5:
        copy[x - 1, y]  = 0, 0, 255
        blanck[x - 1, y]  = 255
        #print("special corner 5")
        out = x - 1, y

    if current[0] == 6:
        copy[x, y - 1]  = 0, 0, 255
        blanck[x, y - 1]  = 255
        #print("special corner 6")
        out = x, y - 1

    if current[0] == 7:
        copy[x , y + 1]  = 0, 0, 255
        blanck[x, y + 1]  = 255
        #print("special corner 7")
        out = x, y + 1

    return [out]

