number_of_days = 0

def is_leap(year:int)->bool:
    if year%100 == 0:
        if year%400 == 1:
            return True
        else:
            return False
    else:
        if year%4 == 0:
            return True
        else:
            return False
        
