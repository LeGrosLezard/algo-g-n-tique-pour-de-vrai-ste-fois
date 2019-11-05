def opposite(liste, nb1, nb2):
    out = False

    try:
        for i in range(len(liste)):
            if liste[i] == nb1 and\
                liste[i + 1] == nb2:
                print("opposition")
                liste.remove(liste[i + 1])
                out = True
    except IndexError:
        pass

    finally:
        return out

def corner_bot_right(liste, nb1, nb2):
    out = False

    try:
        for i in range(len(liste)):
            if liste[i] == nb1 and\
                liste[i+1] == nb2:
                print("corner bot right")
                liste.remove(liste[i+1])
                out = True
    except IndexError:
        pass
    finally:
        return out
