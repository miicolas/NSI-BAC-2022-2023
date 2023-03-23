def verifie (tab) : 
    for i in range (len(tab)-1): 
        if tab[i]> tab[i+1] : 
            return False
    return True
        
        
print(verifie([5]))