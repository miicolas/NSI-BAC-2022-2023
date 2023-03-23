def convertir (tab):
    s= 0 
    for i in range(len(tab)): 
        s += tab[i]*2**(len(tab)-i-1)
    return s

print(convertir([1, 0, 1, 0, 0, 1, 1]))