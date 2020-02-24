'''Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
 Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''

class Stationery:
    title='Stationery'
    def drow(self):
        print(self.title+' drawing start')

class Pen(Stationery):
    title='Pen'
    def drow(self):
        print(self.title+' drawing start!')

class Pencil(Stationery):
    title='Pencil'
    def drow(self):
        print(self.title+' drawing start!!')

class Handle(Stationery):
    title='Handle'
    def drow(self):
        print(self.title+' drawing start!!!')

pen=Pen()
pencil=Pencil()
handle=Handle()
stationery=Stationery()
stationery.drow()
pen.drow()
pencil.drow()
handle.drow()