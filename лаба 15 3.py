k = []
scores = open('3.txt', 'r')
for line in scores:
  splitted_line = line.split(' ')
  for values in splitted_line:
    value_as_int = int(values)
    k.append(value_as_int)
def sr(num):
    return max(k) + min(k)
print(sr(k))
    