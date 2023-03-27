def min_et_max (tab) : 
    d = {'min': tab[0], 'max':tab[0]}
    if len(tab)== 1 : 
        d['min'] = tab[0]
        d['max'] = tab[0]
        return d 
    for i in range (len(tab)): 
        if d['min']> tab[i]: 
            d['min'] = tab[i]
        elif d['max']< tab[i]: 
            d['max'] = tab[i]
    return d 

print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
print(min_et_max([0, 1, 2, 3]))
print(min_et_max([3]))
print(min_et_max([1, 3, 2, 1, 3]))
print(min_et_max([-1, -1, -1, -1, -1]))
