
x = input().lower()

term_data = {}
for word in x.split():
  if term_data.get(word) is None:
    term_data[word] = [0, len(word)]
  term_data[word][0] += 1

term_data = [(term, data) for term, data in term_data.items() ]
print(max(term_data, key=lambda x:x[1][0])[0], max(term_data, key=lambda x:x[1][1])[0] )
