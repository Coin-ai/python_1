# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(*arg):
	try:
		return arg[0]/arg[1]
	except ZeroDivisionError:
		print('error! zero division')
		return division(arg[0],num_input('please enter  divisor: '))

def num_input(text):
	while True:
		try:
			user_num=int(input(text))
			break
		except ValueError:
			print('error! only numbers')
	return user_num

print(division(num_input('please enter dividend: '),num_input('please enter  divisor: ')))