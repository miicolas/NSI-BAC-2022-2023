def verifie (L): # L est une liste d'entiers
    """Renvoie True si les éléments de la liste sont dans l'ordre croissant, False sinon"""
    if len(L) == 0 :  # Si la liste est vide, on renvoie False
        return False 
    else : 
        for i in range (len(L)) :  # On parcourt la liste 
            if L[i+1]>L[i] :  # Si l'élément suivant est plus grand que l'élément courant
                return True 
            else : 
                return False


assert verifie([8,0,5,9]) == False