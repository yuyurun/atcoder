s = input()
 
all_ = ['SUN','MON','TUE','WED','THU','FRI','SAT']
 
 
for i in range(7):
    if all_[i] == s:
        break
        
print(7-i)
