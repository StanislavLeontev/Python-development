
class Cell:

    def __init__(self,qnt):
        self.qnt = qnt

    def __add__(self, other):
        return self.qnt + other.qnt

    def __sub__(self, other):
        if self.qnt - other.qnt <= 0:
            return 'вычесть невозможно'
        else:
            return self.qnt - other.qnt

    def __mul__(self, other):
        return self.qnt * other.qnt

    def __floordiv__(self, other):
        if self.qnt // other.qnt == 0:
            return 'поделить невозможно'
        else:
            return self.qnt // other.qnt

    def make_order(self,row):
        rw = ''
        for i in range(self.qnt // row):
            for j in range(row):
                rw += '*'
            rw += '\n'
        for i in range(self.qnt % row):
            rw += '*'
        return rw

cell_1 = Cell(12)
cell_2 = Cell(6)
cell_3 = Cell(14)

print(f'сложение: {cell_1 + cell_2}')
print(f'вычитание: {cell_1 - cell_2}')
print(f'ошибка при вычитании: {cell_1 - cell_3}')
print(f'умножение: {cell_1 * cell_2}')
print(f'деление: {cell_1 // cell_2}')
print(f'ошибка при делении: {cell_1 // cell_3}')
print(f'матрица клеток 1:\n{cell_1.make_order(4)}')
print(f'матрица клеток 2:\n{cell_2.make_order(2)}')
print(f'матрица клеток 3:\n{cell_3.make_order(3)}')