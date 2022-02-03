from re import findall

class Date:

    def __init__(self,day,month,year):
        self.date_dn = f'{day}-{month}-{year}'

    @classmethod
    def method_1(cls,date_cm):
        return findall(r'[\d]+',date_cm)

    @staticmethod
    def method_2(mtd):
        if int(mtd[1]) <= 12 and len(mtd[2]) <= 4:
            print(f'{"-".join(mtd)}  дата валидна')
        else:
            print(f'{"-".join(mtd)}  дата не валидна')


Date.method_2(Date.method_1('25-12-2000'))
Date.method_2(Date.method_1('25-12-20000'))
