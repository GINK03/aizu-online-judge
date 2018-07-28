
w = int(input())
bs = [ x+1 for x in range(w)]
n = int(input())

for i in range(n):
  a, b = map(lambda x:int(x)-1, input().split(','))
  bs[a], bs[b] = bs[b], bs[a]

[print(b) for b in bs]
