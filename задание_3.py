
class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.position = position
        self._income = {'wage':wage,'bonus':bonus}
        self.name = name
        self.surname = surname

class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def full(self):
        return f'Работник: {self.get_full_name()}, на должности {self.position}, получает {self.get_total_income()} руб.'

worker_1 = Position('Иван','Алексеев','Инженер',20000,20000)
worker_2 = Position('Олег','Хлебов','Бухгалтер',30000,5000)

print(worker_1.full())
print(worker_2.full())
