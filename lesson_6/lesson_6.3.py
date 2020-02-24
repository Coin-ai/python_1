'''Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).'''

class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name=name
        self.surname=surname
        self.position=position
        self._income={'wage':wage,'bonus':bonus}#self.income=cl_dict={'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name+' '+self.surname
    def get_total_income(self):
        return self._income['wage']+self._income['bonus']

position=Position('John','Doe','SEO',12000,1640)
print(position.get_full_name())
print(position.get_total_income())
position.position='CMO'
position._income['wage']=9000
position._income['bonus']=1140
print(position.get_total_income())
print(position.name,position.surname,position.position,position._income)