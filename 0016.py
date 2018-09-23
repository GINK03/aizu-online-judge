
import math
x, y, radian = 0, 0, 0
while True:
  try:
    step, radian = map(int, input().split(',') )
  except EOFError as ex:
    break
  y2 = step*math.sin(math.radians(radian))
  x2 = step*math.cos(math.radians(radian))

  x += x2
  y += y2
print(x, y)
