import sys

command_1 = sys.argv[1]
command_2 = sys.argv[2]

if command_1.isdigit() == True and command_2.isdigit() == True:
    with open('bakery.csv','r') as file:
        count = 0
        f = file.readline()
        while f:
            if count >= int(command_1)-1:
                print(f)
            count += 1
            if count >= int(command_2):
                break
            f = file.readline()
else:
    print('Не корректные данные')



