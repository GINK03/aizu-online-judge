
def eratosthenes(n):
  multiples = set()
  for i in range(2, n+1):
    if i not in multiples:
      yield i
      multiples.update(range(i*i, n+1, i))

while True:
  try:
    print(len(list(eratosthenes(int(input())))))
  except:
    break
