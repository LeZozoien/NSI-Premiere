def div(a:int, b:int)->tuple:
    """Retourne dans l'ordre le quotient, puis le reste de la division euclidienne de a par b"""
    assert isinstance(a, (int, float)) & isinstance(b, (int, float)), "Les arguments doivent être des nombres" # Cas interdit
    assert b != 0, "b doit être différent de 0"  # Cas interdit
    abs_a, abs_b = abs(a), abs(b)
    ispos_a, ispos_b = a >= 0, b >= 0
    ispos_res = not ispos_a ^ ispos_b
    
    quot = 0
    while abs_a >= abs_b:
        abs_a -= abs_b
        quot += 1

    if ispos_res:
        return quot, abs_a
    else:
        if abs_a == 0:
            return -1*quot , 0
        return -1*quot-1 , abs_a - abs_b
    

assert div(10, 3) == (3, 1)
assert div(35, 7) == (5, 0)
assert div(10, -3) == (10//-3, 10%-3)
assert div(35, -7) == (-5, 0)
assert div(3/5, -7/5) == ((3/5)//(-7/5), (3/5)%(-7/5))


## Pseudo-code parce que le pseudocode c'est bien ET C'EST PAS JUSTE L'INVERSE DU PYTHON

# verifier que a est entier et b est entier
# verifier que b est différent de 0
# abs_a <- abs(a)
# abs_b <- abs(b)
# ispos_a <- a >= 0
# ispos_b <- b >= 0
# ispos_res <- non (ispos_a xor ispos_b)

# quot <- 0
# tant que abs_a >= abs_b
#     abs_a <- abs_a - abs_b
#     quot <- quot + 1
# fin tant que

# si ispos_res est vrai:
#     return quot, abs_a
# sinon:
#     si abs_a est égal à 0:
#         return -1 * quot , 0
#     fin si
#     return (-1 * quot) -1 , abs_a - abs_b