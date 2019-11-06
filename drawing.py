import cv2

#Variables
R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE


def recup_contours(img, blanck):

    edges = cv2.Canny(img, 255,200)
    contours, _ = cv2.findContours(edges, R, P)

    for cnts in contours:
        cv2.drawContours(blanck, [cnts], -1, (255,255,255), 1)
        #cv2.fillPoly(blanck, pts =[cnts], color=(255, 255, 255))
        (x, y, w, h) = cv2.boundingRect(cnts)

    return blanck



def incrementation(x, y, number1, number2, copy):

    x = x + number1
    y = y + number2

    copy[x, y]  = 0, 0, 255

    return x, y



def corner(current, copy, blanck, x,  y):

    #   0
    #   . .
    #     0
    #     0

    
    zero=0;un=0;deux=0;trois=0;quattre=0;
    six=0;sept=0;cinq=0;

    for i in current:
        if i == 0:zero += 1
        if i == 1:un += 1
        if i == 2:deux += 1
        if i == 3:trois += 1
        if i == 4:quattre += 1
        if i == 5:cinq += 1
        if i == 6:six += 1
        if i == 7:sept += 1

    if deux == 0 and sept == 1 and len(current) == 2:
        copy[x , y + 1] = 0, 0, 255
        blanck[x, y + 1] = 255
        print("cooorner")
        

    if quattre == 1 and zero == 0 and\
       len(current) == 2:
        copy[x + 1, y] = 0, 0, 255
        blanck[x + 1, y] = 255
        print("cooorner")





def no_bloc(last, current):

    zero=0;un=0;deux=0;trois=0;quattre=0;
    six=0;sept=0;cinq=0;
    for i in last:
        if i == 0:zero += 1
        if i == 1:un += 1
        if i == 2:deux += 1
        if i == 3:trois += 1
        if i == 4:quattre += 1
        if i == 5:cinq += 1
        if i == 6:six += 1
        if i == 7:sept += 1



    if zero == 1:
        for i in current:
            if i == 1:
                current.remove(i)
    if un == 1:
        for i in current:
            if i == 0:
                current.remove(i)

    if deux == 1:
        for i in current:
            if i == 3:
                current.remove(i)

    if trois == 1:
        for i in current:
            if i == 2:
                current.remove(i)

    return current



def diagonale(current):

    zero=0;un=0;deux=0;trois=0;quattre=0;
    six=0;sept=0;cinq=0;
    for i in current:
        if i == 0:
            zero += 1
        if i == 3:
            trois += 1

        if i == 2:
            deux += 1

        if i == 4:
            quattre += 1


    #print(zero,un,deux,trois,quattre)

    if zero == 1 and quattre == 1 :
        current.remove(4)
        print("diagolane removed")
    if deux == 1 and quattre == 1:
        current.remove(4)
        print("diagolane removed")



    return current



def arrierre_avant(historic, current, x, y, last):

    zero=0;un=0;deux=0;trois=0;quattre=0;
    six=0;sept=0;cinq=0;

    if len(historic) >= 3:
        for i in current:
            if i == 0:zero += 1
            if i == 1:un += 1
            if i == 2:deux += 1
            if i == 3:trois += 1
            if i == 4:quattre += 1
            if i == 5:cinq += 1
            if i == 6:six += 1
            if i == 7:sept += 1

        if x + 1 == historic[-2][0] and\
           y - 1 == historic[-2][1]:
            current.remove(6)

        if x - 1 == historic[-2][0] and\
           y + 1 == historic[-2][1]:
            current.remove(7)


    if len(last) > 0:
        if last[0] == 7 and\
            zero == 1 and six == 1:
            current.remove(0)
            current.remove(6)

    return current


def corner_to_lign(current, last):
    
    zero=0;un=0;deux=0;trois=0;quattre=0;
    six=0;sept=0;
    
    if len(last) > 0:
        for i in current:
            if i == 0:zero += 1
            if i == 1: un += 1
            if i == 0:trois += 1
            if i == 1: quattre += 1


        if last[0] == 7 and\
           zero == 1 and un == 1:
            current.remove(0)

        if last[0] == 6 and\
           zero == 1 and un == 1:
            current.remove(1) 


    return current


def speciale_corner_after_selection(current, copy, blanck, x, y):
    if current[0] == 4:
        copy[x + 1, y]  = 0, 0, 255
        blanck[x + 1, y]  = 255
        print("special corner")


