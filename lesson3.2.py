# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_func(**kwargs):
    print (kwargs)

while True:
    user_param=input('введите через запятую ваши имя, фамилия, год рождения, город проживания, email, телефон: ')
    user_param=user_param.split(',')
    print (user_param)
    if len(user_param)==6:
        my_func(name=user_param[0], surname=user_param[1],birth=user_param[2],city=user_param[3], email=user_param[4], phone=user_param[5])
        break

    print('неверный формат ввода или не все данные')