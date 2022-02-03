
class Item:
    def __init__(self,color,power,firm):
        self.color = color
        self.pow = power
        self.firm = firm

class Printer(Item):
    def __init__(self,printing_speed,color,power,firm):
        self.p_sp = printing_speed
        self.color = color
        self.pow = power
        self.firm = firm

    def __repr__(self):
        return 'принтер'


class Scanner(Item):
    def __init__(self,scanning_speed,color,power,firm):
        self.s_sp = scanning_speed
        self.color = color
        self.pow = power
        self.firm = firm

    def __repr__(self):
        return 'сканер'


class Copier(Item):
    def __init__(self,copy_speed,color,power,firm):
        self.c_sp = copy_speed
        self.color = color
        self.pow = power
        self.firm = firm

    def __repr__(self):
        return 'ксерокс'

class Warehouse:

    wh = {}
    comp_dep = {}

    def admissions(item,qnt):
        try:
            int(qnt)
        except ValueError:
            print('некорректное значение количества')
        else:
            if item in Warehouse.wh:
                Warehouse.wh[item] += qnt
            else:
                Warehouse.wh[item] = qnt

    def transmissions(item,qnt,division):
        try:
            int(qnt)
        except ValueError:
            print('некорректное значение количества')
        else:
            Warehouse.wh[item] -= qnt
            Warehouse.comp_dep[division] = [item,+qnt]

    def show():
        print(f'комплектация отделов:{Warehouse.comp_dep}')
        print(f'содержимое склада:{Warehouse.wh}')



printer = Printer(10,'white',85,'Panasonic')
scanner = Scanner(5,'white',70,'LG')
copier = Copier(15,'black',90,'Philips')
warehouse = Warehouse

warehouse.admissions(printer,10)
warehouse.admissions(copier,6)
warehouse.admissions(scanner,4)

warehouse.transmissions(printer, 5, 'склад')
warehouse.transmissions(scanner, 4, 'офис')
warehouse.transmissions(copier, 2, 'офис')
warehouse.transmissions(copier, 1, 'офис')
warehouse.transmissions(printer, 'e', 'склад')

warehouse.show()