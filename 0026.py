
xs = [ [0 for i in range(10)] for k in range(10) ]

import sys
for line in sys.stdin:
  x,y,s = map(int, line.strip().split(',') )

  if s == 1:
    xs[y][x]   += 1
    if y+1 <= 10:
      xs[y+1][x] += 1
    if y-1 >= 0:
      xs[y-1][x] += 1
    if x+1 <= 10:
      xs[y][x+1] += 1
    if x-1 >= 0:
      xs[y][x-1] += 1

  if s == 2:
    xs[y][x]   += 1
    if y+1 <= 10:
      xs[y+1][x] += 1
    if y-1 >= 0:
      xs[y-1][x] += 1
    if x+1 <= 10:
      xs[y][x+1] += 1
    if x-1 >= 0:
      xs[y][x-1] += 1
    if x-1 >= 0 and y+1 <= 10:
      xs[y+1][x-1] += 1
    if x-1 >= 0 and y-1 >= 0 :
      xs[y-1][x-1] += 1
    if x+1 <= 10 and y+1 <= 10:
      xs[y+1][x+1] += 1
    if x+1 <= 10 and y-1 >= 0 :
      xs[y-1][x+1] += 1
      
  if s == 3:
    xs[y][x]   += 1
    if y+1 <= 10:
      xs[y+1][x] += 1
    if y-1 >= 0:
      xs[y-1][x] += 1
    if x+1 <= 10:
      xs[y][x+1] += 1
    if x-1 >= 0:
      xs[y][x-1] += 1

    if x-1 >= 0 and y+1 <= 10:
      xs[y+1][x-1] += 1
    if x-1 >= 0 and y-1 >= 0 :
      xs[y-1][x-1] += 1
    if x+1 <= 10 and y+1 <= 10:
      xs[y+1][x+1] += 1
    if x+1 <= 10 and y-1 >= 0 :
      xs[y-1][x+1] += 1

    if x+2 <= 10:
      xs[y][x+2] += 1
    if x-2 >= 0:
      xs[y][x-2] += 1
    if y+2 <= 10:
      xs[y+2][x] += 1
    if y-2 >= 0:
      xs[y-2][x] += 1

#for x in xs:
#  print(x)

sums = 0
maxs = 0
for x in xs:
  sums += len( [a for a in x if a == 0] )
  maxs = max([max(x), maxs])
print(sums)
print(maxs)
