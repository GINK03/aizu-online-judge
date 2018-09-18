from itertools import combinations


while True:
  n, s = map(int, input().split())
  if n == 0 and s == 0:
    break
  
  count = 0
  for t in combinations(list(range(0,10)), n):
    if sum(t) == s:
      count += 1
  print(count)
