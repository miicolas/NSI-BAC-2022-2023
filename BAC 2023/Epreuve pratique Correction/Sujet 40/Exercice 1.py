def nombres_de_mots (phrase) : 
    mot = 0
    for i in phrase : 
        if i == ' ' : 
            mot += 1
    if phrase[len(phrase)-1] == '?' or phrase[len(phrase)-1] == '!' : 
        return mot
    else : 
        return mot + 1 


assert nombres_de_mots('Bonjour je suis nicolas ?') == 4 , 'test 1'
assert nombres_de_mots('Bonjour !') == 1 , 'test 2' 
assert nombres_de_mots('Bonjour je nicolas.') == 3 , 'test 3'  
