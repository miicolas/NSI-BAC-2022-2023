def mini(releve, date):
    """Renvoie la date et la valeur minimale d'un relevé de température"""
    min_val = releve[0] # On initialise la valeur minimale à la première valeur du relevé
    min_date = date[0] # On initialise la date minimale à la première date du relevé
    for i in range(1, len(releve)): # On parcourt le relevé 
        if releve[i] < min_val: # Si la valeur courante est plus petite que la valeur minimale
            min_val = releve[i] # On met à jour la valeur minimale
            min_date = date[i] # On met à jour la date minimale

    return min_date, min_val



t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

print(mini(t_moy, annees))
