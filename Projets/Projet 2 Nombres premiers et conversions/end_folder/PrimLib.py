def intput(arg): return int(input(arg)) # Même fonction que int(input(arg))

def crible(n:int)->list[bool]:
    '''Retourne une liste de tous les nombres premiers de 0 à n'''
    primes = [True for i in range(n)]   # Tous les nombres sont premiers initialement

    primes[0], primes[1] = False, False # 0 et 1 ne le sont pas

    for i in range(2, int(n/2)):        # Crible d'erastothène
        for k in range(2, int(n/i)+1):  # Suppression des multiples de i
            try:
                primes[k * i] = False   # Les multiples ne sont pas premiers
            except:
                pass

    nbs = []
    for n, i in enumerate(primes):
        if i:
            nbs.append(n)               # Ajout de n si le nombre est premier
            

    return(nbs)

def d2b(*decimal_numbers)->list[int]:
    '''Convertit un (des) nombre(s) décimal (ux) en binaire'''

    return_list = []

    for decimal_number in decimal_numbers:
        return_string = ""              # Initialiser une string à rien

        quot = decimal_number//2
        rest = decimal_number%2

        return_string += str(rest)

        while quot != 0:                # Tant que le quotient n'est pas zero, continuer de le diviser par 2 en ajoutant le 
            rest = quot%2               # reste à return_string
            quot = quot//2

            return_string += str(rest)
            
        return_list.append(return_string[::-1]) # Lire return_string à l'envers
    return return_list

def d2hex(*decimal_numbers)->list[str]:
    '''Convertit un nombre décimal en hexadécimal'''
    
    return_list = []

    for decimal_number in decimal_numbers:
        hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f'] # Tableau de conversion
        return_string = ""              # Initialiser une string à rien

        while decimal_number !=0:
            return_string = str(hex_list[decimal_number%16]) + return_string
            decimal_number //= 16
            # Diviser le nombre par 16 puis ajouter la valeur convertie à return_string

        return_list.append(return_string)
    return return_list

def is_prime(x, base:int | None = 10)->bool:
    '''
    Retourne True si un nombre est premier, False dans le cas contraire
    Peut prendre un argument supplémentaire pour donner le nombre dans une base autre que décimale'''
    # Utilise la méthode naïve pour trouver si un nombre est premier
    if base == 10:
        x = int(x)
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True
    else:
        x = str(x)
        x = another_to_decimal(x, base)
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

def est_dyadique(nombre:float)->bool:
    '''Retourne True si un nombre est dyadique ou False si le nombre ne l'est pas'''
    for i in range(35): # 35 --> Nombre qui marche le mieux
        nombre *= 2
        if nombre % 1 == 0: # Si le nombre est entier lorsqu'il est multiplié par une puissance de 2, il est dyadique
            return True
    return False # Sinon, il ne l'est pas

def find_factors(a_trouver:int)->list[int]:
    '''Décompose un nombre en son produit de facteurs premiers'''
    diviseurs = []
    while a_trouver != 1:
        for i in range(2, a_trouver+1):
            if a_trouver % i == 0:
                a_trouver = a_trouver//i
                diviseurs.append(i)
                break

    return diviseurs

def decimal_to_another(decimal_number:int, base:int | None = 16)->str:
    '''Convertit un nombre décimal dans une autre base'''
    # Technique présente dans le cours
    if base > 36 or base < 1:
        raise ValueError('Base is incorrect')
    if base == 1:
        return "0"*decimal_number
    hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return_string = ""
    while decimal_number !=0:
        return_string = str(hex_list[decimal_number%base]) + return_string
        decimal_number //= base
    return return_string

def another_to_decimal(number:str, base:int)->int:
    '''Convertit un nombre d'une autre base vers décimal'''
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = 0
    for i, char in enumerate(number):
        result += hex_list.index(char) * (base**(len(number)-i-1))
    return result

# Niveau 1
    # Nombres premiers jusqu'à 100 : crible(100)
    # Convertir des nombres premiers en binaire : d2b(nombre) 
        # Attention, nombre peut être une liste

# Niveau 2
    # Demander à l’utilisateur le seuil jusqu’auquel les nombres premiers doivent être listés.
        # --> Implémenté comme argument de la fonction crible
    # Convertir ces nombres premiers en hexadécimal.
        # Utiliser d2hex(nombre)
            # nombre peut être une liste
    # Vérifier si un nombre est premier : is_prime(nombre)
    # Verifier si un nombre est dyadique : est_dyadique(nombre)

# Niveau 3
    # L’utilisateur peut donner le nombre dont il veut tester la primalité dans la base de son choix.
        # Utiliser is_prime() avec l'argument supplémentaire base
    # Décomposer un nombre en produit de facteurs premiers : find_factors(nombre)
    # Proposer une interface utilisateur
        # Voir PrimEngine
    # Ecrire des nombres en base b quelconque : utiliser decimal_to_another(nombre, base)
        # Supporte jusqu'a la base 36
    # Stocker la liste des nombres premiers dans un fichier txt ou csv.

def test_dyadique(nb): 
    if str(nb)[len(str(nb))-1] != "5": return False
    else:return ((nb*(2**35))%1)==0