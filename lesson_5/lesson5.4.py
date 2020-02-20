'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.'''

repl_dict={'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}

with open('lesson5.4_input.txt') as file:
    with open('lesson5.4_out.txt','w',encoding='utf=8') as file2:
        for line in file:
            find=line.split(' -',1)[0]
            file2.write(line.replace(find,repl_dict.get(find,find)))