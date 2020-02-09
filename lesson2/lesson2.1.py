# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


error=None
try:
    int('dfg')
except Exception as exc:
    error=exc

type_list=[123,-321.2,complex(3,4),'string',[1,'st'],(3,7),{1},{'key':'val'},True,b'txt',bytearray(b'txt'),None,ValueError,error]

for val in type_list:
    print(val,type(val))