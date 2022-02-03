
data = 0
list = []
while data != 'stop':
    data = input()
    try:
        list.append(int(data))
    except ValueError:
        continue
print(list)