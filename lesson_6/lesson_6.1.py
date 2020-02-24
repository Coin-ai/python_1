'''Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.'''

from itertools import cycle
import time

class TrafficLight:
    __color=None
    __itr=cycle({'red':7,'yellow':2,'green':4}.items()) # {'red':7,'yellow':2,'green':4,'yellow':2}
    def running(self,test_color):# run in thread?
        self.__color,t=next(self.__itr)
        print(self.__color,end='')
        # test color in class if need before sleep - test_color!=self.__color
        time.sleep(t)
        print('\r', end='')
    def get_color(self):
        return self.__color

traffic_light=TrafficLight()

test_list=('red','yellow','green')
working=True

i=0
while working:
    if i>2:
        working=False
    i+=1
    for test_color in test_list:
        traffic_light.running(test_color)
        if test_color!=traffic_light.get_color():# test_list.color!=traffic_light.running()
            print('Error! Traffic light Stop')
            break
    else:
        continue
    break
else:
    print('end')