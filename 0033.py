
N = int(input())

for n in range(N):
  xs = list(map(int, input().split()))
  
  flag = True
  b1, b2 = [], []
  for x in xs:
    if b1 == [] and b2 == []:
      b1.append(x)
      continue

    if b1 != [] and b2 == []:
      b2.append(x)
      continue

    if x > b1[-1] and x > b2[-1]:
      c1 = x - b1[-1]
      c2 = x - b2[-1]
      if c1 < c2:
        b1.append(x)
      else:
        b2.append(x)
    elif x > b1[-1] and x <= b2[-1]:
      b1.append(x)
    elif x <= b1[-1] and x > b2[-1]:
      b2.append(x)
    else:
      flag = False
      break
  
  if flag == False:
    print('NO')
  else:
    print('YES')
  #print(b1, b2) 
