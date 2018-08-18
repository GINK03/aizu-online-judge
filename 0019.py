from functools import reduce
n = int(input())
factional = reduce(lambda x,y:y*x, [i for i in range(1, n+1)])
print(factional)
