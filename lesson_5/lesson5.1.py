# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка

with open('lesson5.1_out.txt','w') as file:
    while user_text:=input('enter text (exit if empty): '):
        file.write(f'{user_text}\n')