import sys

command = sys.argv[1]

if command.isdigit():
    with open('bakery.csv','a') as file:
        file.write(command + '\n')
else:
    print('некорректное значение')