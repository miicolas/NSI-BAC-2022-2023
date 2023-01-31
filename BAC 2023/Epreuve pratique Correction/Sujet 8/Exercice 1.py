def max_dico(dico):
    """Retourne la clé et la valeur maximale d'un dictionnaire"""
    max_value = max(dico.values()) # On récupère la valeur maximale du dictionnaire
    max_key = [k for k, v in dico.items() if v == max_value][0] # On récupère la clé associée à la valeur maximale
    return (max_key, max_value) # On renvoie la clé et la valeur maximale



dico = {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}
print(max_dico(dico))