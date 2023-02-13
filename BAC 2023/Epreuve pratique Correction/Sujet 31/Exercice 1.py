def nb_repetitions (elt, tab):
    """renvoie le nombre d'occurrences de elt dans tab"""

    r= 0 
    for i in range(len(tab)):
        if elt == tab[i]:
            r+= 1
    return r

assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3
assert nb_repetitions('A', [ 'B', 'A', 'B', 'A', 'R']) == 2
assert nb_repetitions(12, [1, '! ', 7, 21, 36, 44]) == 0