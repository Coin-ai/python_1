'''Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.'''

from random import randint

with open('lesson5.5_out_in.txt','w+') as file:
    file.write(' '.join([str(randint(1,100)) for _ in range(10)]))
    file.seek(0)
    print(sum(map(int, file.read().split())))