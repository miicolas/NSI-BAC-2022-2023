from random import randint


def lancer(n):
    tab = []
    for i in range(n):
        tab.append(randint(1, 6))

    return tab


def paire_6(tab):
    c = 0
    for i in range(len(tab)):
        if tab[i] == 6:
            c += 1

    if c >= 2:
        return True
    else:
        False


print(lancer(5))
print(paire_6(lancer(5)))
