first, second, temp, sum = 1, 2, 0, 0
while temp < 4000000:
    if second%2 == 0:
        sum += second
    temp = first + second
    first = second
    second = temp
print(sum)
