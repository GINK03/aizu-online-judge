while True:
  try:
    n = int(input())
    results = []
    for i in range(10):
      for j in range(10):
        for k in range(10):
          for l in range(10):
            results.append( n == sum([i, j, k, l]) )
    print(len(list(filter(lambda x:x==True, results))))
  except:
    break
