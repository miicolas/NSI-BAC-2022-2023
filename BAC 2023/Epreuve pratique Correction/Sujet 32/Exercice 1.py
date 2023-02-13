def min_et_max (tab) : 
    """renvoie un dictionnaire contenant la valeur minimale et la valeur maximale de tab"""
    r = {'min': tab[0], 'max': tab[0]}
    if len(tab) == 1 : 
        r['max'] = tab[0]
        r['min'] = tab[0]
    else: 
        for i in range(len(tab)): 
            if tab[i] > r['max'] : 
                r['max'] = tab[i]
            if tab[i] < r['min'] : 
                r['min'] = tab[i]

    return r

assert min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert min_et_max([0, 1, 2, 3]) == {'min': 0, 'max': 3}
assert min_et_max([3]) == {'min': 3, 'max': 3}
assert min_et_max([1, 3, 2, 1, 3]) == {'min': 1, 'max': 3}
assert min_et_max([-1, -1, -1, -1, -1]) == {'min': -1, 'max': -1}



