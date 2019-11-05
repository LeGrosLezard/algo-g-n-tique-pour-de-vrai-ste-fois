def opposite(liste, nb1, nb2):

    try:
        if liste[-2] == nb1 and\
            liste[-1] == nb2:
            print("opposition")
    except IndexError:
        pass


def corner_bot_right(liste, nb1, nb2):

    try:
        if liste[-3] == nb1 and\
               liste[-1] == nb2:
                print("corner bot right")
    except IndexError:
        pass
