#Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
while True:
    try:
        total_seconds=int(input('введите количество секунд:'))
        break
    except ValueError:
        print('не корректный ввод! допустимы только числа')
hours=total_seconds//3600
minutes=total_seconds%3600//60
seconds=total_seconds%60
# print ('%02d:%02d:%02d'%(hours,minutes,seconds))
print(f'введенное вами время {hours:02d}:{minutes:02d}:{seconds:02d}')