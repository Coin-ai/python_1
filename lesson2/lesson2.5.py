# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list=[7,5,3,3,2]

while True:
    try:
        user_num=int(input('enter number:'))
        break
    except ValueError:
        print('error! only numbers')
my_list2=my_list.copy()

#sort
my_list2.append(user_num)
my_list2.sort(reverse=True)
print(my_list2)

#if can't use sort
for ind,val in enumerate(my_list):
    if val<user_num:
        my_list.insert(ind, user_num)
        break
else:
    my_list.append(user_num)
print(my_list)