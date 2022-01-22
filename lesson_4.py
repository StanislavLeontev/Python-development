import os

des_dir = r'C:\Users\Стасек\PycharmProjects'
size_dict = {
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0
}

for dirpath, dirnames, filenames in os.walk(des_dir):
    os.chdir(dirpath)
    for i in range(len(filenames)):
        if os.stat(filenames[i]).st_size < 100:
            size_dict[100] += 1
        elif os.stat(filenames[i]).st_size < 1000:
            size_dict[1000] += 1
        elif os.stat(filenames[i]).st_size < 10000:
            size_dict[10000] += 1
        elif os.stat(filenames[i]).st_size < 100000:
            size_dict[100000] += 1
        else:
            pass

print(size_dict)