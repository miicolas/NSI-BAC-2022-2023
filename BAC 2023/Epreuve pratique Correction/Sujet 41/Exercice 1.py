def recherche(caractere, chaine) : 
    c = 0 
    for i in range(len(chaine)) : 
        if caractere == chaine[i] : 
            c += 1 
    return c

print(recherche('e', "sciences"))
print(recherche('i', "mississippi")) 
print(recherche('a', "mississippi"))