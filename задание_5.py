
class Stationery:
    def __init__(self,title):
        self.title = title

    def draw(self):
        print(f'{self.title}: Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. Инструмент: {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. Инструмент: {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. Инструмент: {self.title}')

Pn = Pen('Ручка')
Pl = Pencil('Карандаш')
Hl = Handle('Маркер')

Pn.draw()
Pl.draw()
Hl.draw()
