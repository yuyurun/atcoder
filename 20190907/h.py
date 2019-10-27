import sys
F = sys.stdin
num = 0
for line in F:
    if num == 0:
        n = int(line)
    else:
        print(line)
    num += 1
    if num == n+1:
        break
    #print(line.strip("\n"))

