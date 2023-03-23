def moyenne(tab) :
    somme_note = 0
    somme_coef = 0

    for i, j in tab : 
        somme_note += i*j
        somme_coef += j

    if somme_coef == 0 : 
        return None 
    
    return somme_note/somme_coef

print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print(moyenne([(3, 0), (5, 0)]))