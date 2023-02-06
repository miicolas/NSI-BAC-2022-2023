def moyenne(tab) : 
    assert len(tab) > 0, "Le tableau est vide"
    assert type(tab) == list, "Le tableau n'est pas un tableau"
    '''
    moyenne(list) -> float
    Entrée : un tableau non vide d'entiers
    Sortie : nombre de type float
    Correspondant à la moyenne des valeurs présentes dans le
    tableau
    ''' 
    somme = 0
    for i in range(len(tab)) :
        somme += tab[i]
    return somme/len(tab)

assert moyenne([1, 2, 3]) == 2
