def liste_puissances(a, n):
    assert n >= 0, "n doit être positif"
    assert type(n) == int, "n doit être un entier"
    """Retourne la liste des puissances de a jusqu'à a^n"""
    result = [] # on crée une liste vide
    current_power = a # on initialise la puissance actuelle à a
    for i in range(1, n + 1): # on itère n fois
        result.append(current_power) # on ajoute la puissance actuelle à la liste
        current_power *= a # on multiplie la puissance actuelle par a  
    return result

def liste_puissances_borne(a, borne):
    assert type(borne) == int, "la borne doit être un entier"
    assert borne >= 0, "la borne doit être positive"
    """Retourne la liste des puissances de a jusqu'à a^n"""
    result = [] # on crée une liste vide
    current_power = a # on initialise la puissance actuelle à a
    while current_power < borne: # tant que la puissance actuelle est inférieure à la borne
        result.append(current_power)
        current_power *= a # on multiplie la puissance actuelle par a
    return result


assert liste_puissances(3,5) == [3,9,27,81,243]
assert liste_puissances(-2,4) == [-2,4,-16,64]
assert liste_puissances_borne(2,16) == [2,4,8]
        
