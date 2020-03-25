n = int(input())
a = list(map(int, input().split()))

import fractions

f = 1
for aa in a:
    ff=fractions.gcd(f,aa)
    f = int(f*aa/ff)

print(0)
#ans = 0
#for aa in a:
#   ans += f/aa
#
#print(int(ans%(1000000000+7)))
