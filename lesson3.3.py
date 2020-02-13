# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def sum_2max(*nums):
    nums=list(nums)
    nums.remove(min(nums))
    return sum(nums)

def input_int(msg):
    try:
        return int(input(msg))
    except ValueError:
        print ('error! only numbers')
        return input_int(msg)

print(sum_2max(input_int('enter number 1: '),input_int('enter number 2: '),input_int('enter number 3: ')))