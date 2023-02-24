def renverse (chaine): 
    if len(chaine) == 0: 
        return chaine 
    else: 
        return renverse(chaine[1:]) + chaine[0] # On renvoie la chaine renversée

chaine = 'informatique'
print (renverse(chaine))