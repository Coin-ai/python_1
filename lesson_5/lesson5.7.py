'''Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''

import json

count_firm=0
all_prfit=0
average_profit=0
firms={}

with open('lesson5.7_input.txt',encoding='utf=8') as file:
    for line in file:
        name,type,proceeds,cost=line.split()
        profit=int(proceeds)-int(cost)
        if profit>=0:
            count_firm+=1
            all_prfit+=profit
        firms[name]=profit
    if count_firm:
        average_profit=round(all_prfit/count_firm,2)
firms=[firms,{'average_profit':average_profit}]
with open('lesson5.7_out_json.txt','w',encoding='utf=8') as file:
    json.dump(firms,file)