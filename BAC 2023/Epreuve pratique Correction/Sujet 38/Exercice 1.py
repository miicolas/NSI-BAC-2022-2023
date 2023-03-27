def correspond (mot, mot_a_trous): 
    if len(mot) != len(mot_a_trous):
        return False
    for i in range (len(mot)): 
        if mot[i] != mot_a_trous[i] and mot_a_trous[i]!= '*': 
            return False
    
    return True

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
print(correspond('STOP', 'S*'))
print(correspond('AUTO', '*UT*'))