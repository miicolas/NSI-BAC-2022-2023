def nbr_occurences (chaine): 
    """Écrire une fonction nbr_occurrences prenant comme paramètre une chaîne de
    caractères chaine et renvoyant le dictionnaire des nombres d’occurrences des
    caractères de cette chaîne"""
    dico = {} # on crée un dictionnaire vide
    t = len(chaine) # on calcule la taille de la chaîne
    for letter in range(t): # on itère sur les caractères de la chaîne
        if chaine[letter] in dico: # si le caractère est déjà dans le dictionnaire
            dico[chaine[letter]] += 1 # on incrémente sa valeur
        else:
            dico[chaine[letter]] = 1 # sinon on l'ajoute au dictionnaire
    return dico
    
print(nbr_occurences("bonjour"))
