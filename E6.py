def mainf():
    suma, sumb = 0, 0
    for x in range(1,101):
        suma+=x**2
        sumb+=x
    print("answer: ", sumb**2-suma)
mainf()
