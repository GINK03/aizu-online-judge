
n = int(input())

for i in range(n):
  a = int(input())
  b = int(input())
  s = a+b

  if len(str(s)) > 80:
    print("overflow")
  else:
    print(s)
