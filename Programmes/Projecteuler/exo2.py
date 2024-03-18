from functools import lru_cache
from sys import *
set_int_max_str_digits(1000000)


@lru_cache(maxsize=10000)
def get_fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return get_fib(x - 2) + get_fib(x - 1)
    
my_list = []
x = 1


while True:
    valeur = get_fib(x)
    if len(str(valeur)) == 1000:
        my_list.append(x)
        break
    else:
        pass
    print(len(str(valeur)), str(valeur)[0:5], x)
    x += 1

print(my_list)