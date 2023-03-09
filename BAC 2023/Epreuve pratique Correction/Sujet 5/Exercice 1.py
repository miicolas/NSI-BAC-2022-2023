import random 
def lancer(n) :
        return [random.randint(1,6) for i in range(n)]

def paire_6(tab) :
    c = 0
    for i in range(len(tab)): 
        if tab[i] == 6 : 
            c += 1
    if c >= 2 : 
        return True
    else: 
        return False

lancer1 = lancer(5)
print(lancer1, paire_6(lancer1))


lancer2 = lancer(5)
print(lancer2, paire_6(lancer2))

lancer3 = lancer(3)
print(lancer3, paire_6(lancer3))

lancer4 = lancer(0)
print(lancer4, paire_6(lancer4))