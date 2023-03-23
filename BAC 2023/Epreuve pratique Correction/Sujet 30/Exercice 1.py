def moyenne (tab): 
    s = 0
    for i in range (len(tab)): 
        s+= tab[i]
    return s/ len(tab)

print(moyenne([1.0, 2.0, 4.0]))