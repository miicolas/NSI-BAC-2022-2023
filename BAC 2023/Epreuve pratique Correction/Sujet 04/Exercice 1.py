def a_doublon(tab): 
    for i in range(len(tab)-1): 
        if tab[i] == tab[i+1] : 
            return True
    return False