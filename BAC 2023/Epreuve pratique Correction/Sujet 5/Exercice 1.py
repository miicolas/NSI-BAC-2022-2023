import random 
def lancer (n):
    """renvoie une liste de n nombres aléatoires entre 1 et 6"""  
    return [random.randint(1,6) for i in range (n)]  # On crée une liste de n nombres aléatoires entre 1 et 6

def paire_6(tab): 
    """renvoie True si le tableau tab contient au moins deux 6, False sinon"""
    return tab.count(6)>= 2 # On compte le nombre d'occurrences de 6 dans le tableau et on renvoie True si le nombre d'occurrences est supérieur ou égal à 2



print(paire_6(lancer(5)))