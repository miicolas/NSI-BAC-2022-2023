def ajoute_dictionnaires (d1,d2):
    """Fusion de deux dictionnaires et si une clé est présente dans les deux dictionnaires, on fait la somme des valeurs associées"""
    assert type(d1) == dict and type(d2) == dict
    d = {} # On crée un nouveau dictionnaire
    for cle in d1: # On parcourt les clés du premier dictionnaire
        d[cle] = d1[cle] # On copie la clé et la valeur associée dans le nouveau dictionnaire
    for cle in d2: # On parcourt les clés du second dictionnaire
        if cle in d:   # Si la clé est présente dans le premier dictionnaire
            d[cle] += d2[cle] # On ajoute la valeur associée à la valeur associée dans le premier dictionnaire
        else:
            d[cle] = d2[cle] # On copie la clé et la valeur associée dans le nouveau dictionnaire
    return d

assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}

