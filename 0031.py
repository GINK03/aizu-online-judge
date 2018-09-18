import math
while True:
  try:
    n = int(input())
    ans = []
    while n != 0:
      if n%2 == 1:
        n -= 1
        ans.append( 1 )
      else:
        buff = []
        tmp = n
        while True:
          tmp //= 2
          buff.append(2)
          if tmp%2 != 0:
            n -= math.pow(2, len(buff))
            ans.append( math.pow(2, len(buff)) )
            break
    print( ' '.join( [f'{int(a)}' for a in ans] ) )
  except:
    break
