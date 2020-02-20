'''Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.'''

with open('lesson5.2_input.txt') as file:
    count_str=0
    for line in file:
        count_str+=1
        print (f'count words in {count_str} row: {len(line.split())}')
    print(f'count rows in file: {count_str}')