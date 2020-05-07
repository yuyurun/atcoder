x = int(input())

if x > 0:
     for i in range(1000000000):
        if x-i**5 > 0 and(x-i**5)**(1/5) ==  int((x-i**5)**(1/5)):
            b = -(x-i**5)**(1/5) 
            a = i
            break
        if (x+i**5)**(1/5) ==  int((x+i**5)**(1/5)):
            b = -(x+i**5)**(1/5) 
            a = -i
            break
else:
     for i in range(1000000000):
         if -x-i**5 >0 and (-x-i**5)**(1/5) ==  int((-x-i**5)**(1/5)):
            a =  -(-x+i**5)**(1/5) 
            b =  i
            break
         if (-x+i**5)**(1/5) ==  int((-x+i**5)**(1/5)):
            a =  -(-x+i**5)**(1/5) 
            b = -i
            break



print(int(a),int(b))
