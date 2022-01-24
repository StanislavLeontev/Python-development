import csv


def read():
    dct = {}
    with open('users.csv') as users:
        with open('hobby.csv') as hobby:
            usrs = users.readline()
            hbby = hobby.readline()
            while usrs:
                if hbby:
                    dct[usrs[0:-1]] = hbby[0:-1]
                elif usrs == False and hbby == True:
                    print('error code: 1')
                    break
                else:
                    dct[usrs] = None
                usrs = users.readline()
                hbby = hobby.readline()
            return dct


def write(dct):
    with open('users_hobby.csv', 'w') as f:
        file_writer = csv.writer(f, delimiter=':', lineterminator='\n')
        for row in dct:
            file_writer.writerow([row, dct[row]])


dict = read()
write(dict)
print(dict)