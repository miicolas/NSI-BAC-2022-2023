def couples_consecutifs (tab) : 
    r = []
    for i in range(len(tab)-1) : 
        if tab[i+1] - tab[i] == 1 : 
            r.append((tab[i], tab[i+1]))
    return r 

print(couples_consecutifs([1, 4, 5, 3]))
print(couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]))
