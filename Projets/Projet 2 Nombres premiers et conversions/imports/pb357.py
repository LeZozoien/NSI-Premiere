from time import *


def find_divisors(x:int)->list[int]:
    result = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            result.add(i)
            result.add(x//i)
    return list(result)


def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

thing = 0

time_start = time_ns()
for i in range(1000000):
    prime = 1
    for j in find_divisors(i):
        if not (is_prime(j+int(i/j))):
            prime = 0
            break
    if prime == 1:
        thing += i
time_1 = time_ns() - time_start

time_start = time_ns()
for i in range(100000):
    prime = 1
    for j in find_divisors(i):
        if not (is_prime(j+int(i/j))):
            prime = 0
            break
    if prime == 1:
        thing += i

time_2 = time_ns() - time_start

print(time_1, time_2)