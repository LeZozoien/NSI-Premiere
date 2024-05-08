def is_last_calc(calculation:tuple|list)->bool:
    terme_1 = calculation[0]
    calcul = calculation[1]
    terme_2 = calculation[2]
    terme_1, terme_2 = str(terme_1), str(terme_2)
    calculs = ["+", "-", "*", "**", "/", "%", "//"]
    if len(calculation) == 3:
        if calcul in calculs:
            if terme_1.isnumeric() and terme_2.isnumeric():
                return True
    return False