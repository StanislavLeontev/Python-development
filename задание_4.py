
class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('начало движения')

    def stop(self):
        print('остановка')

    def turn(self,direction):
        print(f'поворот на {direction}')

    def show_speed(self):
        print(f'текущая скорость: {self.speed}')

    def stats(self):
        print(f'Марка авто:{self.name}  Цвет: {self.color}.')
        if self.is_police == True:
            print('Полицейское авто')


class TownCar(Car):
    def show_speed(self):
        print(f'текущая скорость: {self.speed}')
        if self.speed >= 60:
            print('Скорость привышена')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f'текущая скорость: {self.speed}')
        if self.speed >= 40:
            print('Вы привысили скорость')

class PoliceCar(Car):
    pass


TC = TownCar( 70,'red','Volvo',False)
SC = SportCar( 91,'yellow','Audi',False)
WC = WorkCar( 35,'blue','Case',False)
PC = PoliceCar( 44,'white','Chevrolet',True)

def testing(car,dir):
    car.stats()
    car.go()
    car.turn(dir)
    car.show_speed()
    car.stop()
    print(' ')

testing(TC,'лево')
testing(SC,'лево')
testing(WC,'право')
testing(PC,'право')
