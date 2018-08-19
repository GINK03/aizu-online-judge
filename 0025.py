import sys
lines = []
for index, line in enumerate(sys.stdin):
  line = line.strip()
  if index%2 == 0:
    lines.append( [line] )
  else:
    lines[-1].append( line )
#print(lines)
lines = iter(lines)
for line in lines:
  i1 = line
  xs = list(map(int, i1[0].split() ))
  ys = list(map(int, i1[1].split() ))
  full_match = 0
  spec_match = 0
  for x, y in zip(list(xs), list(ys)):
    #print(x, y, y in xs)
    if x == y:
      full_match += 1
    elif y in xs:
      spec_match += 1
  print(full_match, spec_match)
