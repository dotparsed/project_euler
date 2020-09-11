def mainf(numb):
    i = 0
    while True:
        i += 20
        summ = 0
        for x in range(1, numb+1):
             if i % x == 0:
                 summ += 1
             else:
                 break
        if summ == numb:
            return print("answer", i)

mainf(20)