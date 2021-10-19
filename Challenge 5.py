li = []
check = [2, 1, -1, -2]
row = []
column = []
verf = False
for i in range(8):
    li.append([])
    for j in range(8):
        li[i].append(chr(65+i)+ str(j+1))

loc = input("Please input the knight's errand")

x = 0
y = 0
for i in range(8):
    for j in range(8):
        if loc == li[j][7-i]:
            x = j
            y = 7-i
            break

for i in check:
    for j in check:
        if i/j != 1 and i/j != -1:
            if -1 < x+i < 8 and -1 < y+j < 8:
                for k in range(len(row)):
                    if x+i == row[k] and y+j == column[k]:
                        verf = True
                if verf is False:
                    row.append(x+i)
                    column.append(y+j)
verf = False

for i in range(8):
    for j in range(8):
        if loc == li[j][7-i]:
            print('Kn', end=" ")
        else:
            for k in range(len(row)):
                if li[j][7-i] == li[row[k]][column[k]]:
                    verf = True
            if verf is True:
                print("xx", end=" ")
                verf = False
            else:
                print(li[j][7-i], end=" ")
    print()
