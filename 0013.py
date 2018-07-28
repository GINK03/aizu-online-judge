
q = []

while True:
  try:
    i = int(input())
    if i == 0:
      print(q.pop())
    else:
      q.append( i )
  except:
    break
