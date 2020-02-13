# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def input_num(msg,flag):
    try:
        if flag==1:
            num=float(input(msg))
            if num<0:
                print('только положительные числа')
                return input_num(msg,flag)
        else:
            num=int(input(msg))
            if num>=0:
                print('только отрицательные числа')
                return input_num(msg,flag)
        return num
    except ValueError:
        print ('error! only numbers')
        return input_num(msg,flag)

def my_func1(num1,num2):
    print(f'use ** {num1**num2}')
    for ind in range(1,abs(num2)):
        num1*=num1
    print(f'use new func {1/num1}')

num1=input_num('введите действительное положительное число: ',1)
num2=input_num('целое отрицательное число: ',2)

my_func1(num1,num2)