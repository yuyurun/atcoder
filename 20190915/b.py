s = input()

size = len(s)
judge = 0
ki = ['R','U','D']
gu = ['L','U','D']


for i in range((size+1)//2):
    if s[i*2] not in ki:
        judge += 1

for i in range(size//2):
    if s[i*2+1] not in gu:
        judge += 1
        
if judge == 0:
    print('Yes')
else:
    print('No')
