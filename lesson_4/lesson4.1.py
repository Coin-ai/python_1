# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# from sys import argv
from optparse import OptionParser

options=OptionParser()
options.add_option('--hours','-u',dest='hours',default=0)
options.add_option('--rph','-r',dest='rph',default=0)
options.add_option('--premium','-p',dest='premium',default=0)
opts,args=options.parse_args()

def salary(hours,rph,premium):
    try:
        return (int(hours)*float(rph))+float(premium)
    except ValueError:
        return 'error input'

print(salary(opts.hours,opts.rph,opts.premium))