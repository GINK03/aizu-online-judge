
while True:
  try:
    a, b, c, d, e, f = map(int, input().split())
  except Exception as ex:
    break

  a, b, c = map(lambda x:x/a, [a, b, c])
  d, e, f = map(lambda x:x/d, [d, e, f])

  y = (c - f)/(b - e)
  x = c - b*y
  print(f'{x:0.04f} {y:0.04f}')
