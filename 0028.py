import sys
i_f = {}
for line in sys.stdin:
  v = int(line)
  if i_f.get(v) is None:
    i_f[v] = 0
  i_f[v] += 1

ans = {}
for i, f in i_f.items():
  if ans.get(f) is None:
    ans[f] = []
  ans[f].append(i)
ans = [ (a,vs) for a, vs in ans.items() ]
ans = max(ans, key=lambda x:x[0])
#print(ans)

for i in sorted(ans[1]):
  print(i)
