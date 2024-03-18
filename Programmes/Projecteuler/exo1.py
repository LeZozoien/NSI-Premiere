from time import *

temps2 = time_ns()
print(sum([ i if i%5==0 or i%3==0  else 0  for i in range(1000000000)]))
print((time_ns() - temps2) / 1000000000)
