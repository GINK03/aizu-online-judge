s = int(input())

for i in range(s):
  xs = map(int, input().split())
  xs = [x*x for x in xs]
  
  if xs[0]+xs[2] == xs[1] or xs[1]+xs[0] == xs[2] or xs[2]+xs[1]==xs[0]:
    print('YES')
  else:
    print('NO')
