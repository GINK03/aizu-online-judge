import math
n = int(input())

base = 100000
for i in range(n):
  base *= 1.05

  base /= 1000

  base = math.ceil(base)

  base *= 1000

print(base)
  
