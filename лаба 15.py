with open ('1.txt', 'r') as f:
    old_data = f.read()

first = old_data.replace('(', '[')
new = first.replace(')', ']')
with open ('2.txt', 'w') as f:
  f.write(new)

