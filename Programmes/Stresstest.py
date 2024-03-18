from time import *
from math import *


def find_primes(x:int) -> list:
    entier_a_tester = 1
    maximum_a_tester = x
    liste_premiers = []
    liste_premiers.append(2)
    liste_premiers.append(3)

    entier_a_tester = 4

    while entier_a_tester <= maximum_a_tester:
        premier = 1
        for nb in liste_premiers:
            if entier_a_tester % nb == 0:
                premier = 0
                break
        if premier:
            liste_premiers.append(entier_a_tester)
        entier_a_tester += 1
        if entier_a_tester % 10000 == 0:
            print(entier_a_tester)


    return(liste_premiers)

print(find_primes(1000000))