# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

user_list=[]

while answer:=input('enter value (end list if empty): '):
    user_list.append(answer)

size=len(user_list)-1
i=0
while i<size:
    user_list[i],user_list[i+1]=user_list[i+1],user_list[i]
    i+=2
print(user_list)