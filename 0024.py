import math

while True:
  try:
    V = float(input())
    for n in range(1, 1000):
      height = 5 * n - 5
      t = math.sqrt( height/4.9 ) 
      v = 9.8 * t
      if v >= V:
        break
    print(n)
  except:
    break
