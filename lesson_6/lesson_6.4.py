'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.'''

class Car:
    speed=0
    is_police=False
    def __init__(self,color,name):
        self.color=color
        self.name=name
    def go(self):
        print('car went')
    def stop(self):
        print('car stop')
    def turn(self,direction):
        print(f'car direction: {direction}')
    def show_speed(self):
        print (self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed>60:
            print('Overspeed! ',end='')
        print(self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Overspeed! ',end='')
        print(self.speed)

class PoliceCar(Car):
    def __init__(self,color,name):
        super().__init__(color,name)
        self.is_police=True

car_town=TownCar('green','chevrolet')
car_town.speed=67
car_town.go()
print(car_town.name,car_town.speed,car_town.color,car_town.is_police)
car_town.show_speed()
car_town.turn('left')
car_town.stop()

car_police=PoliceCar('black','Ford')
car_police.speed=70
print(car_police.name,car_police.speed,car_police.color,car_police.is_police)