from fractions import gcd


while True:
  try:
    a, b = map(int, input().split())
    left = gcd(a,b)
    print( left, a*b//(left))
  except:
    break
