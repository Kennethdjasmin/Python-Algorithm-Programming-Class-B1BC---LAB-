temp = [11, 9, 7, 2], ['A', 'B', 'C', 'D']

try:
    var = int(input("Please input an integer"))
except:
    print("I said an integer! >:|")

num = int(var)
for i in range(4):
    if num % temp[0][i] == 0:
        print(temp[1][i])

"""
var = int(input("Please input an integer"))
if var % 11 == 0:
    print("A")
if var % 9 == 0:
    print("B")
if var % 7 == 0:
    print("C")
if var % 2 == 0:
    print("D")

"""