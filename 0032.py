
import sys

square = 0
hishi  = 0
for line in sys.stdin:
  line = line.strip()
  es = list(map(lambda x: int(x) * int(x), line.split(',')))
  #print(es)

  e1, e2, e3 = es
  if e1 + e2 == e3:
    square += 1
    continue
  e1, e2, e3 = sorted(es)
  if e1 + e2 == e3:
    ...
  else:
    hishi += 1

print(square)
print(hishi)
