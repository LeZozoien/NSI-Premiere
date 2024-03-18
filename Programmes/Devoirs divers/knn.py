def knn_reg(t:list|tuple, w:list|tuple, k:int)->list:
    """ T : valeurs déjà étiquetées (sous la forme x, y, ..., classe)
    W : valeurs à étiqueter (sous la forme x, y, ... et de même dimension que les valeurs de T)
    k : k plus proches voisins"""

    if not isinstance(t, (list, tuple)):
        raise TypeError("t doit être une liste ou un tuple")
    if not isinstance(w, (list, tuple)):
        raise TypeError("w doit être une liste ou un tuple")
    if not isinstance(k, int):
        raise TypeError("k doit être un entier")
    
    m, n = len(t), len(w)
    dim = len(t[0])-1

    if m == 0:
        raise ValueError("t ne peut pas être vide")
    if dim < 2:
        raise ValueError("Les valeurs doivent avoir des coordonnées et une classe")

    for val in t:
        if len(val) != dim:
            raise ValueError("Les valeurs de t doivent avoir la même dimension et une classe")
        if not isinstance(val[len(val)-1], (int, float)):
            raise TypeError("Les classes doivent être des nombres")
        
    for val in w:
        if len(val) != dim:
            raise ValueError("Les valeurs de w doivent avoir la même dimension que celle de t")


    guesses = []

    for i in range(n):
        distances = []
        for j in range(m):
            
            dist = sum([(w[i][d] - t[j][d]) ** 2 for d in range(dim)]) ** 0.5
            distances.append((dist, j))  # Stocker la distance et l'indice du point dans T

        distances.sort()  # Trier les distances
        k_plus_proches = distances[:k]  # Prendre les k plus petites distances
        somme_valeurs = 0
        for dist, index in k_plus_proches:
            somme_valeurs += t[index][dim]  # En supposant que le troisième élément dans T est l'étiquette ou la valeur
        guess = somme_valeurs / k  # Moyenne des valeurs des k voisins les plus proches
        guesses.append([w[i], guess])

    return guesses