

ss = list(input())


# make index
ic = { i:c for i,c in enumerate('abcdefghijklmnopqrstuvwxyz') }
#print(ic)

strings = []
for k in range(26):
  ci = { c:(i-k)%26 for i,c in enumerate('abcdefghijklmnopqrstuvwxyz') }
  #print(ci)
  string = ''
  for s in ss:
    if ci.get(s) is None:
      #print(s, end='')
      string += s
    else:
      i = ci[s] 
      c = ic[i]
      #print(c, end='')
      string += c
  strings.append( string )

for string in strings:
  if 'this' in string or 'the' in string or 'that' in string:
    print(string)
    break

