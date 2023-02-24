def nombre_de_mots (phrase) : 
    '''Renvoie le nombre de mots dans la phrase.'''
    n = len(phrase)-1
    m = 0
    for i in phrase : 
        if i == ' ' : 
            m += 1
    if phrase[n] == '?' or phrase[n] == '!' : 
        return m
    else : 
        return m+1
        
phrase = 'Je suis blond ?'

print(nombre_de_mots(phrase))
