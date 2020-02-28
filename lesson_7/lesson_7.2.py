'''Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''

from abc import ABC, abstractmethod

class Сlothes(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def fabric_cons():
        pass

class Coat(Сlothes):
    def __init__(self,v):
        self.name='Coat'
        self.type=1
        self.v=v
    @property
    def fabric_cons(self):
        return self.v/6.5 + 0.5

class Сostume(Сlothes):
    def __init__(self,h):
        self.name='Сostume'
        self.type=2
        self.h=h
    @property
    def fabric_cons(self):
        return 2*self.h+0.3

class Warehouse:
    def __init__(self):
        self.store=[]
    def add_coat(self,v):
        self.store.append(Coat(v))
    def add_costume(self,h):
        self.store.append(Сostume(h))
    @property
    def common_cons(self):
        cons=0
        for el in self.store:
            cons+=el.fabric_cons
        return cons

st=Warehouse()
st.add_coat(5)
st.add_coat(3)
st.add_coat(8)

st.add_costume(7)
st.add_costume(5)
st.add_costume(2)

print(st.common_cons)