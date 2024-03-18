a_trouver = 600851475143
racine = a_trouver ** 0.5
diviseurs = []
print(a_trouver, racine)

while a_trouver != 1:
    for i in range(int((racine//1)+1)):
        if a_trouver % (i+1) == 0:
            a_trouver = int(a_trouver/(i+1))
            diviseurs.append(i+1)

    print(a_trouver)

print(diviseurs)