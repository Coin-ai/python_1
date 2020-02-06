#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
while True:
    user_int=input('введите число n:')
    if user_int.isdigit():
        break
    print('не корректный ввод! допустимы только числа')
n_nn_nnn=int(user_int)+int(user_int+user_int)+int(user_int+user_int+user_int)
print(f'n+nn+nnn = {n_nn_nnn}')