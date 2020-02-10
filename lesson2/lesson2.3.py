# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
while True:
    try:
        num_month=int(input('enter month number 01-12:'))
        if not (0<num_month<13):
            print('error num month')
            continue
        break
    except ValueError:
        print('error! only numbers')


seasons=['зима','зима','весна','весна','весна','лето','лето','лето','осень','осень','осень','зима']
print(seasons[num_month-1])

seasons_dict={1:'зима',2:'зима',3:'весна',4:'весна',5:'весна',6:'лето',7:'лето',8:'лето',9:'осень',10:'осень',11:'осень',12:'зима'}
print(type(seasons_dict))
print(seasons_dict[num_month])