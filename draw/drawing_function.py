import cv2

#Show, Open, Create black picture
from starter.operation import open_picture
from starter.operation import show_picture
from starter.operation import blanck_picture



def draw_shema(number, schema, posX, posY, blanck):
    """recup x, y from other form it give info for area"""
    x = posX; y = posY;

    for i in range(number):
        blanck[x, y] = 255, 255, 255

        if schema == "corner4":
            x -= 1; y-= 1
            blanck[x+1, y] = 255, 255, 255

        if schema == "corner7":
            x += 1; y-= 1
            blanck[x, y-1] = 255, 255, 255

        if schema == "corner5":
            x += 1; y+= 1
            blanck[x, y+1] = 255, 255, 255

        if schema == "corner6":
            x -= 1; y+= 1
            blanck[x, y+1] = 255, 255, 255

        if schema == "lign horrizontale1":y += 1;
        if schema == "lign horrizontale2":y -= 1;
        if schema == "lign verticale1":x -= 1;
        if schema == "lign verticale2":x += 1;


    return x, y




def min_distance(a):

    liste = []; counter = 0;
    
    for key, value in a.items():
        min_value = 10000; data = "";

        for key1, value1 in a[key].items():
            if value1 != 0:
                if value1[0] < min_value:
                    min_value = value1[0]
                    data  = [key1, value1]

        liste.append(data)

        counter+=1

    return liste



def draw_form(form1, blanck):
    
    for x in range(form1.shape[0]):
        for y in range(form1.shape[1]):
            if form1[x, y] > 100:
                blanck[x, y] = 255, 255, 255

def recup_points(form1):
    liste_w = []
    for x in range(form1.shape[0]):
        for y in range(form1.shape[1]):
            if form1[x, y] > 100:
                liste_w.append([x, y])    

    return liste_w



def draw_lines_to_zone(liste_w, liste, pict, blanck, zone):

    for el in liste_w:
        if el[0] > zone[0]-2 and el[0] < zone[0] + 2:
            #print(abs((el[0] + el[1]) - (zone[0] + zone[1])))
            if abs((el[0] + el[1]) - (zone[0] + zone[1])) < 8:
                #blanck[el[0], el[1]] = 0, 0, 255 demo^^
                cv2.line(blanck, (el[1], el[0]),
                         (liste[pict][1][2], liste[pict][1][1]), (255, 255, 255), 1)

        elif el[1] > zone[1]-2 and el[1] < zone[1] + 2:
            #print(abs((el[0] + el[1]) - (zone[0] + zone[1])))
            if abs((el[0] + el[1]) - (zone[0] + zone[1])) < 8:
                #blanck[el[0], el[1]] = 0, 0, 255
                cv2.line(blanck, (el[1], el[0]),
                         (liste[pict][1][2], liste[pict][1][1]), (255, 255, 255), 1)



def finish_picture(img, blanck):
    R = cv2.RETR_TREE
    P = cv2.CHAIN_APPROX_NONE

    blanck1 = blanck_picture(img)
    cv2.imwrite("final.png", blanck)
    gray = cv2.cvtColor(blanck, cv2.COLOR_BGR2GRAY)


    contours, _ = cv2.findContours(gray, R, P)
    for cnt in contours:
        cv2.drawContours(blanck1, [cnt], -1, (255,255,255), 2)
        cv2.fillPoly(blanck1, pts =[cnt], color=(255, 255, 255))
    return blanck1




