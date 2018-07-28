
while True:
  try:
    sums = 0
    d = int(input())
    n = 600//d
    for s in range(n):
      D = d*((s*d)**2)
      sums += D
    print(sums)
  except:
    break

