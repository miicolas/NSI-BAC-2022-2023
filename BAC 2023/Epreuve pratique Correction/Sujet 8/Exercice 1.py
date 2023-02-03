def max_dico(dico):
    """Retourne la clé et la valeur maximale d'un dictionnaire"""
    max_like = 0
    for pseudo in dico:
        if dico[pseudo]>max_like:
            max_pseudo = pseudo
            max_like=dico[pseudo]
    return max_pseudo,max_like
 
dico = {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}
print(max_dico(dico))
