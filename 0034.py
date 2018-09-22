import sys
for line in sys.stdin:
  xs = [int(x) for x in line.strip().split(',')]

  v2 = xs.pop()
  v1 = xs.pop()

  sumed = sum(xs)
  #print(sumed)
  #print('time', sumed/(v1+v2) )
  t = sumed/(v1+v2)
  #print('distance', t*v1)

  t = t*v1
  res = 0
  for index, x in enumerate(xs):
    t -= x
    if t == 0.0:
      res = index + 1
      break
    elif t < 0.0:
      res = index + 1
      break

  print(res)
