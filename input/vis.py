       f = False
        list_input = v.split()
        num = int(list_input[-1])
        rules = {}
        for rule in list_input[:-1]:
          n,w = rule.split(':')
          rules[int(n)] = w
        for j,w in rules.items():
          if num%j == 0:
            print(w,end='')
            f = True
        if f == False:
          print(num)
