def convert(base, num):
    li = []
    temp = num
    res = ""
    while temp > 0:
        li.append(int(temp % base))
        temp = temp // base
    for i in range(len(li)-1, -1, -1):
        res += str(li[i])
    return res

base = int(input("please enter the base to covert from base-10"))
num = int(input("please enter the number to be converted"))
print(convert(base, num))
