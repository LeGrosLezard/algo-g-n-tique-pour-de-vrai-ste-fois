def delete_same_detection(dico, name, PIT):
    
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

    name = ""
    for i in key:
        try:
            i = int(i)
            if i == int(i):
                name += str(i)
        except:
            pass

    return name
