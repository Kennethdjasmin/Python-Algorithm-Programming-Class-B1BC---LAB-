li1 = []
in1 = -1

while in1 != 0:
    print('Create new user    -> [1]')
    print("Edit user's data   -> [2]")
    print("Remove user's data -> [3]")
    print("Print all users    -> [9]")
    print('Quit program       -> [0]')
    in1 = int(input("Please input your number of choice:\n"))
    if in1 == 0:
        print("Bye ;_;")
    if in1 == 1:
        name = input("please enter user's name")
        age = input("please enter user's age")
        job = input("please enter user's job")
        li1.append({'name': name, 'age': age, 'job': job})
        print('\n\n')
    elif in1 == 2:
        name = input("please enter the user's name")
        check = -1
        # invalid = True
        for i in li1:
            if i['name'] == name:
                check += 1
                if check >= 1:
                    print("More than one user of the same name detected, do yo"
                          "u wish to change this user's data too?")
                    in2 = input("yes or no?")
                    if in2 == 'no':
                        break
                print("\n\nCurrent user's data:\n", i, "\n")
                i['name'] = input("please enter the user's name")
                i['age'] = input("please enter user's age")
                i['job'] = input("please enter user's job")
                print("\n\nNew user's data:\n", i, "\n")
                # invalid = False
        # if invalid:
        #     print("Don't know whose name is that \_(:v)_/")
    elif in1 == 3:
        # invalid = True
        name = input("please enter the user's name")
        check = -1
        for i in li1:
            if i['name'] == name:
                check+=1
                # invalid = False
        if check >= 1:
            for i in range(len(li1)):
                if i >= len(li1):
                    i = 0
                if li1[i]['name'] == name:
                    print("\n\nCurrent user's data:\n", li1[i], "\n")
                    print("More than one user of the same name detected, \n"
                          "please select which data do you want to delete")
                    in2 = input("yes or no?")
                    if in2 == 'yes':
                        del li1[i]
        else:
            for i in range(len(li1)):
                if li1[i]['name'] == name:
                    del li1[i]
                    break
        # if invalid:
        #     print("Don't know whose name is that \_(:v)_/")
    elif in1 == 9:
        for i in range(len(li1)):
            print(li1[i])
        print(f"A total of {i} users' data stored\n")









