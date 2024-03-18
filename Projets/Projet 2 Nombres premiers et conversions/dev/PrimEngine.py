from PrimLib import *

LOGO = '''
    ____       _           ______            _          
   / __ \_____(_)___ ___  / ____/___  ____ _(_)___  ___
  / /_/ / ___/ / __ `__ \/ __/ / __ \/ __ `/ / __ \/ _ \\
 / ____/ /  / / / / / / / /___/ / / / /_/ / / / / /  __/
/_/   /_/  /_/_/ /_/ /_/_____/_/ /_/\__, /_/_/ /_/\___/
                                   /____/              
        '''

MENU_CHOIX = """
1 : Trouver des nombres premiers
2 : Savoir si un nombre est premier
3 : Convertir en binaire
4 : Convertir en hexadécimal
5 : Convertir en base b
6 : Convertir en décimal d'une base quelconque
7 : Sauvegarder des nombres premiers dans un fichier
8 : Vérifier si un nombre est dyadique
9 : ?
10 : Quitter
"""

reponse = 0

print(LOGO)

while reponse != 10:
    print(MENU_CHOIX)
    reponse = input("Que voulez-vous faire ? ")
    try:
        reponse = int(reponse)
        match reponse:
            case 1:
                try:
                    arg = intput("Jusqu'a quel nombre voulez-vous trouver les nombres premiers ? ")
                    if arg < 1: break
                    convert = input("Voulez-vous convertir ces nombres ? (o/n) ")
                    if convert == 'n':
                        print(crible(arg))
                    else:
                        base = intput("En quelle base voulez-vous convertir ?")
                        res = []
                        for num in crible(arg):
                            res.append(decimal_to_another(num, base))
                        print(res)
                except: print("Erreur")
            case 2:
                try:
                    arg = intput("Quel nombre voulez-vous tester ? ")
                    if arg < 1: break
                    if is_prime(arg):print(arg, "est premier")
                    else:print(arg, "n'est pas premier")
                except: print("Erreur")
            case 3:
                try:
                    arg = intput("Quel nombre voulez-vous convertir ? ")
                    if arg < 1: break
                    print(d2b(arg))
                except: print("Erreur")
            case 4:
                try:
                    arg = intput("Quel nombre voulez-vous convertir ? ")
                    if arg < 1: break
                    print(d2hex(arg))
                except: print("Erreur")
            case 5:
                try:
                    arg = intput("Quel nombre voulez-vous convertir ? ")
                    base = intput("En quelle base voulez-vous le convertir ? ")
                    if arg < 1: break
                    print(decimal_to_another(arg, base))
                except: print("Erreur")
            case 6:
                try:
                    arg = input("Quel nombre voulez-vous convertir ? ")
                    base = intput("De quelle base voulez-vous le convertir ? ")
                    print(another_to_decimal(arg, base))
                except: print("Erreur")
            case 7:
                try:
                    name = input("Quel nom voulez-vous donner au fichier ? ")
                    nb = intput("Jusqu'a quel nombre voulez-vous trouver les nombres premiers ? ")
                    to_store = []
                    for i in crible(nb):
                        to_store.append(str(i)+ "\n")
                    with open(name + ".txt", "w") as file:
                        file.writelines(to_store)
                except: print("Erreur")
            case 8:
                try:
                    arg = float(input("Quel nombre voulez-vous tester ? "))
                    if est_dyadique(arg):print(arg, 'est dyadique')
                    else:print(arg, "n'est pas dyadique")
                except: print("Erreur")
            case 9:
                print("Bien essayé petit filou")
            case 10: pass
            case _:
                print("Bien essayé")
    except: print("Réponse non supportée")

print("A bientot !")