
while True:
  vv = []
  for i in range(8):
    v = [int(e) for e in list(input())]
    vv.append(v)
  for index in reversed(range(len(vv))):
    t = all(x == 0 for x in vv[index])
    #print(t)
    if t == True:
      vv.pop(index)
  height = len(vv)
  for i in reversed(range(len(vv[0]))):
    aa = [vv[h][i] for h in range(height)]
    aa = all([ a==0 for a in aa ])
    if aa == True:
      for h in range(height): 
        del vv[h][i]
  #  print(aa)
  #print(vv)
  obj = { 'A': [[1, 1], [1, 1]] ,
  'B': [[1], [1], [1], [1]],
  'C': [[1, 1, 1, 1]],
  'D': [[0,1],[1,1],[1,0]] ,
  'E': [[1,1,0],[0,1,1]], 
  'F': [[1,0], [1,1], [0,1]], 
  'G': [[0,1,1], [1,1,0]] } 
  #print(obj)
  for k, v in obj.items():
    if v == vv:
      print(k)
      break
  try:
    input()
  except:
    break
