import math
n = int(input())

for i in range(n):
  x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())


  if abs((x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)) < 1e-10:
    print('YES')
  else:
    print('NO')
