villes_coordonnees = {
    "Rangoon": (96.1666667, 16.7833333),
    "New York": (-74.0063889, 40.7141667),
    "Baghdad": (44.3938889, 33.3386111),
    "Karachi": (67.0822, 24.9056),
    "Shanghai": (121.399722, 31.045556),
    "Mexico": (-99.138611, 19.434167),
    "Jakarta": (106.829444, -6.174444),
    "São Paulo": (-46.665803, -23.473293),
    "Tokyo": (139.751389, 35.685),
    "Seoul": (126.9783, 37.5985),
    "Calcutta": (88.369722, 22.569722),
    "Saint Petersburg": (30.264167, 59.894444),
    "Delhi": (77.216667, 28.666667),
    "Bangkok": (100.501444, 13.753979),
    "Manila": (120.9822, 14.6042),
    "Lagos": (3.395833, 6.453056),
    "Peking": (116.388333, 39.928889),
    "Moscow": (37.615556, 55.752222),
    "Istanbul": (28.964722, 41.018611),
    "Bombay": (72.825833, 18.975),
    "Bogotá": (-74.062827, 4.649178),
    "London": (-0.093689, 51.514125),
    "Madras": (80.283333, 13.083333),
    "Santiago": (-70.666667, -33.45),
    "Sydney": (151.205475, -33.861481),
    "New Delhi": (77.2, 28.6),
    "Lima": (-77.05, -12.05),
    "Lahore": (74.343611, 31.549722),
    "Kinshasa": (15.3, -4.3),
    "Cairo": (31.25, 30.05),
    "Bangalore": (77.583333, 12.983333),
    "Wuhan": (114.273405, 30.580125),
    "Toronto": (-79.416667, 43.666667),
    "Dhaka": (90.4086111, 23.7230556),
    "Rio de Janeiro": (-43.233333, -22.9),
}

villes_population = {
    "Rangoon": 4477782,
    "New York": 8107916,
    "Baghdad": 5672516,
    "Karachi": 11627378,
    "Shanghai": 14608512,
    "Mexico": 8720916,
    "Jakarta": 8540306,
    "São Paulo": 10021437,
    "Tokyo": 31480498,
    "Seoul": 10323448,
    "Calcutta": 4631819,
    "Saint Petersburg": 4039751,
    "Delhi": 10928270,
    "Bangkok": 5104475,
    "Manila": 10443877,
    "Lagos": 8789133,
    "Peking": 7480601,
    "Moscow": 10381288,
    "Istanbul": 9797536,
    "Bombay": 12692717,
    "Bogotá": 7102602,
    "London": 7421228,
    "Madras": 4328416,
    "Santiago": 4837248,
    "Sydney": 4394585,
    "New Delhi": 10928270,
    "Lima": 7646786,
    "Lahore": 6312576,
    "Kinshasa": 7787832,
    "Cairo": 7734602,
    "Bangalore": 4931603,
    "Wuhan": 4184206,
    "Toronto": 4612187,
    "Dhaka": 6493177,
    "Rio de Janeiro": 6023742,
}

villes_pays = {
    "Myanmar": ["Rangoon"],
    "États-Unis": ["New York"],
    "Irak": ["Baghdad"],
    "Pakistan": ["Karachi", "Lahore"],
    "Chine": ["Shanghai", "Peking", "Wuhan"],
    "Mexique": ["Mexico"],
    "Indonésie": ["Jakarta"],
    "Brésil": ["São Paulo", "Rio de Janeiro"],
    "Japon": ["Tokyo"],
    "Corée du Sud": ["Seoul"],
    "Inde": ["Calcutta", "Delhi", "Bombay", "Madras", "New Delhi", "Bangalore"],
    "Russie": ["Saint Petersburg", "Moscow"],
    "Thaïlande": ["Bangkok"],
    "Philippines": ["Manila"],
    "Nigeria": ["Lagos"],
    "Turquie": ["Istanbul"],
    "Colombie": ["Bogotá"],
    "Royaume-Uni": ["London"],
    "Chili": ["Santiago"],
    "Australie": ["Sydney"],
    "Pérou": ["Lima"],
    "République démocratique du Congo": ["Kinshasa"],
    "Égypte": ["Cairo"],
    "Canada": ["Toronto"],
    "Bangladesh": ["Dhaka"],
}

# a) On dispose d’un dictionnaire villes_coordonnees qui associe 
# à chaque nom de ville (chaîne) ses coordonnées sous forme d’un 
# tuple (longitude, latitude). Afficher les noms de toutes les villes 
# dont la latitude est inférieure à 23,43 degrés.

for ville, coords in villes_coordonnees.items(): # Pour chaque paire ville-coords de ville_coordonnées :
    if coords[1] < 23.43 : print(ville)          # Si la latitude est inférieure à 23,43, on affiche le nom de la ville


# b) On dispose également d’un dictionnaire villes_population 
# qui associe à chaque nom de ville (chaîne) son nombre d’habitants (entier). 
# Afficher les coordonnées de la ville ayant le plus d’habitants.

# Initialisation des variables maximums
max_hab = list(villes_population.values())[0]
ville_max = list(villes_population.keys())[0]

for ville, habitants in villes_population.items():                  # Pour chaque paire ville-habitants de villes_population :
    if habitants > max_hab: max_hab, ville_max = habitants, ville   # Si le nombre d'habitants de cette ville est supérieur au nombre max:
                                                                    # on remplace le nombre maximum par le nombre d'habitants de cette ville
                                                                    # et la ville_max par le nom de cette ville

print(ville_max, villes_coordonnees[ville_max]) # On affiche le nom de la ville avec le plus d'habitants

# c) On dispose enfin d’un dictionnaire villes_pays qui associe 
# à chaque nom de pays (chaîne) un tableau de ses villes. Afficher 
# le nombre total d’habitants des villes d’un pays donné et la latitude 
# et la longitude moyenne de ces villes.

for pays, villes in villes_pays.items(): # Pour chaque paire pays-villes de villes_pays :

    # Initialisation des totaux de chaque pays
    tot_hab = 0
    tot_pos = [0, 0]

    for ville in villes: # Pour chaque paire pays-villes de villes_pays :
        tot_hab += villes_population[ville] # On ajoute le nombre d'habitants de cette ville au total
        tot_pos = tot_pos[0]+villes_coordonnees[ville][0], tot_pos[1]+villes_coordonnees[ville][1] # On ajoute les coordonnées au total
    
    # On divise les totaux par le nombre de villes dans ce pays
    tot_hab /= len(villes)
    tot_pos = tot_pos[0]/len(villes), tot_pos[1]/len(villes)

    # On affiche le résultat
    print(pays, tot_hab, tot_pos)