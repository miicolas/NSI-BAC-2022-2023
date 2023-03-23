def moyenne(liste_notes) : 
    s_note = 0
    s_coeff = 0 
    for i, j in liste_notes : 
        s_note += i*j
        s_coeff += j

    return s_note/s_coeff

print(moyenne([(15, 2), (9, 1), (12, 3)])) 
