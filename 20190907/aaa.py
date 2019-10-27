import sys
for line in sys.stdin: 
    nums = line.split()
    ans = []
    for i in nums:
      if int(i) != 0:
        if int(i) not in ans:
          ans.append(i)
        
    print(' '.join(ans), end="")
