def fusion (tab1, tab2): 
    tab_final = []
    i, j = 0, 0
    while i < len(tab1) and j< len(tab2) : 
        if tab1[i] > tab2[j] : 
            tab_final.append(tab2[j])
            j = j + 1
        elif tab1[i]< tab2[j] : 
            tab_final.append(tab1[i])
            i = i +1
        else :
            tab_final.append(tab1[i])
            tab_final.append(tab2[j])
            i = i + 1
            j = j + 1

    tab_final.extend(tab1[i:])
    tab_final.extend(tab2[j:])
    return tab_final

print(fusion([3, 5], [2, 5]))


