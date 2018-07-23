
n, m = map(int, input().split(' '))

ns = [i for i in range(n)]

for i in range(m):
  ha = int(input())
  ns[ha] = None

#print(n, m)
#print(ns)

count = 0
while True:
  size = len(ns)
  ns2 = []
  for j in range(0, size, 2):
    flag = ns[j] is not None and ns[j+1] is not None
    if flag:
      ns2.append( 0 )
      count += 1
    elif ns[j] is not None or ns[j+1] is not None:
      ns2.append( 0 )
    else:
      ns2.append( None)
  #print(ns2)
  ns = ns2
  if len(ns) == 1:
    break
print(count)
      
