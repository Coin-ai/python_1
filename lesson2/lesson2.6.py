# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }


params={'название':0,'цена':float,'количество':int,'единица измерения':0}
item_list=[]
analytics={
    'название':set(),
    'цена':set(),
    'количество':set(),
    'единица измерения':set()
}
add_item=True
num_item=1

while True:
    while add_item:
        if (answer:=input('Add item? [y/n]')) and answer in 'yY':
            break
        elif not answer or answer not in 'nN':
            print('please type: y - yes or n - no ')
            continue
        add_item=False
    else:
        break
    item_param={}
    while True:
        try:
            user_num=int(input('enter item number:'))
            break
        except ValueError:
            print('error! only numbers')
    for key,val in params.items():
        if val:
            while True:
                try:
                    item_param[key]=val(input(key+': '))
                    analytics[key].add(item_param[key])
                    break
                except ValueError:
                    print('error! only numbers')
        else :
            item_param[key]=input(key + ': ')
            analytics[key].add(item_param[key])
    item_list.append((user_num, item_param))
#    item_list.append((num_item,item_param))
    num_item+=1
print(item_list)

analytics={key:list(val) for key,val in analytics.items()}
print(analytics)