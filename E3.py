from math import sqrt

def divid (number):
    all_div = []
    for x in range(int(sqrt(number)), 1, -1):
        if number % x == 0:
            all_div.append(x)
    return all_div

def check_divid(div_list):
    for x in div_list:
        count = 0
        for j in range(2, x-1):
            if x%j == 0:
                count += 1
        if count == 0:
            return print("answer: ",x)

divid_list = divid(600851475143)
check_divid(divid_list)