# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

my_list=[2,1,4,3,6,5,8,7,9]
size=len(my_list)-1
i=0
while i<size:
    my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
    i+=2
print(my_list)