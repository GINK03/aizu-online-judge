
from collections import namedtuple

Point = namedtuple('Point', ('x', 'y'))

def sign (p1, p2, p3):
  return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);

while True:
  try:
    x = list(map(float, input().split()))
    p1 = Point(x[0], x[1])
    p2 = Point(x[2], x[3])
    p3 = Point(x[4], x[5])
    pp = Point(x[6], x[7])
    b1 = sign(pp, p1, p2) < 0.0
    b2 = sign(pp, p2, p3) < 0.0
    b3 = sign(pp, p3, p1) < 0.0
    if (b1 == b2) and(b2 == b3):
      print('YES')
    else:
      print('NO')
  except:
    break 
