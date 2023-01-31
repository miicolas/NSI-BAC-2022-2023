def a_doublon (lst):
    """Retourne True si la liste lst contient au moins un doublon, False sinon.""" 
    for i in range (len(lst)-1) :  # On parcourt la liste
        if lst[i] == lst[i+1] :  # Si l'élément courant est égal à l'élément suivant
            return True       
    return False

lst = 1, 2, 4, 6, 6
print(a_doublon(lst))