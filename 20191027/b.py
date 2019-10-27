a = int(input())
c = 0

for i in range(1,10):
  j = 10-i
  if a%j == 0:
    a = a/j
    c += 1
  if c == 2:
    break
  if a%j == 0:
    a = a/j
    c += 1
  if c == 2:
    break
if a == 1 and c <= 2:
  print('Yes')
else:
  print('No')
