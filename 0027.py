import datetime
import sys
i_weekday = { i:weekday for i, weekday in enumerate('Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split() ) }
while True:
  M, D = map(int, input().split())
  if M == 0:
    sys.exit()
  dt = datetime.datetime.strptime(f'2004-{M}-{D}', '%Y-%m-%d')
  #print(dt)
  print(i_weekday[ dt.weekday() ] )
