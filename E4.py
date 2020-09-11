def mainf():
    list = []
    for i in range(999,100,-1):
        for j in range(999, 100, -1):
            numx = i*j
            if str(numx) == str(numx)[::-1]:
                list.append(numx)
    print(max(list))

mainf()