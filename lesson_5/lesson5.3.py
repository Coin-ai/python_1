'''Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32'''

with open('lesson5.3_input.txt') as file:
    count_w=0
    all_salary=0
    for line in file:
        if line:
            name,salary=line.rsplit(' ',1)
            if (salary:=float(salary))<20000:
                print (f'{name} salary lower 20 000')
            all_salary+=salary
            count_w+=1
    if count_w: print(f'average salary: {all_salary/count_w:.2f}')