input1 = input("please enter your words to be spongebobcified")
counter = 0
for i in input1:
    if counter == 0:
        print(i.upper(), end = '')
    else:
        print(i.lower(), end = '')
    counter = not counter