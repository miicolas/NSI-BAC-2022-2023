def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les entiers
    de 1 Ã   n, False sinon
    '''
    for i in range(1, len(tab)+1):
        if i not in tab:
            return False
    return True


def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui reprÃ©sente un ordre
    de gÃ¨nes de chromosome
    '''
    assert est_un_ordre(ordre)  # ordre n'est pas un ordre de gÃƒÂ¨nes
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < len(ordre)-1:
        if (ordre[i+1]-ordre[i]) not in [-1, 1]: # l'ÃƒÂ©cart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[i-1] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb
