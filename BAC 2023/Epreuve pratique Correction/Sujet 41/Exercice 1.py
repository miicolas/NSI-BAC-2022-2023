def rechercher(caractere,chaine):
    "Renvoie le nombre de fois que caractere apparait dans chaine"
    c = 0  
    for i in range(len(chaine)): 
        if chaine[i]==caractere:
            c+=1 
    return c

print(rechercher('e',"sciences"))