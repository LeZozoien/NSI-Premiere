import time
nbp = []
def conversion_bin(*dn):
    quotient = dn//2
    reste = dn%2
    rs1= str(reste)
    while quotient != 0:
        reste = quotient%2
        quotient = quotient//2
        rs1 += str(reste)  
    return rs1[::-1]
def calcul_premier (min,max):
    for n in range(min,max + 1):
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    break
            else :
                nbp.append(n)
    return nbp
def conversion_hexa(dn):
    hex = []
    for elt in dn :
        hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
        rs2 = ""
        while elt !=0:
            rs2= str(hex_list[elt%16]) + rs2
            elt//= 16    
        hex.append(rs2)
    return hex
def test_premier(nb)->bool:
    nb = int(nb)
    for i in range(2, int(nb**0.5)+1):
        if nb % i == 0:
            return False
    return True
 
Programme = True
print("Bonjour,\nBienvenue sur le logiciel CONVERTISSOR.\nVous avez la possiblité de :\n- Calculer dans un intervalle donné tous les nombres premiers : P\n- Convertir une liste de nombre ou un nombre en binaire : B\n- Convertir une liste ou un nombre en hexadésimal : H\n- Tester si un nombre est binaire : T\n- Stopper le programme : S")
print("Que voulez vous faire ?")
while Programme == True :
    choix = input("")
    if choix == "S":
        Programme = False
 
    elif choix == "P" :
        print("Vous avez sélectionné le module de calcule des nombres premiers.")
        min = int(input("Quel est le minimum de votre intervalle ? "))
        max = int(input("Quel le maximum de votre intervalle ? "))
        print(f"Votre intervalle de nombres premiers se situe entre {min} et {max}")
        time.sleep(2)
        print("Voici le résultat de votre demmande :")
        print(calcul_premier(min,max))
        time.sleep(3)
        print("\nVoulez vous continuer avec cette liste de valeur ?\n - Si oui : tapez O\n - Si non : tapez N")
        print("Si voulez arrêter le programme ici\n Tapez S ")
        print("Que voulez vous faire ?")
        choix2 = input("")
        if choix2 == "O" :
            print("Vous pouvez :\n - Convertir cette liste de données en base hexadécimal : H\n - Convertir cette liste de données en base binaire : B")
            print("Que voulez vous faire ?")
            choix3 = input("")
            if choix3 == "H":
                print("Vous avez sélectionné la conversion en base hexadésimal" )
                time.sleep(0.5)
                print("Voici le résultat de votre demande :")
                print(conversion_hexa(nbp))
                time.sleep(1)
                print("Voulez pouvez :\n - Arrêter le programme ici : S\n - Convertir la liste précédente en bianire : B")
                print("Que voulez vous faire ?")
                choix4 = input("")
                if choix4 == "S":
                    Programme = False
                elif choix4 == "B" :
                    break
 
if Programme == False :
    print("\n FIN DU PROGRAMME")