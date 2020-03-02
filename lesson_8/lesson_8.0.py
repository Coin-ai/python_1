'''== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
Если цифра есть на карточке - она зачеркивается и игра продолжается.
Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
Если цифра есть на карточке - игрок проигрывает и игра завершается.
Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:
```

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
6 7 49 57 58
14 26 - 78 85

23 33 38 48 71
-- Карточка компьютера ---
7 87 - 14 11
16 49 55 88 77

15 20 - 76 -
Зачеркнуть цифру? (y/n)
```

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

P.S.
что-то тут все пляшет с визулизацией. Вот скрин: http://prntscr.com/r96tyh'''

import random

class Game:
    def __init__(self):
        self.kegs=list(range(1,91))
        self.players=[]
    def next_round(self):
        keg=self.kegs.pop(random.randint(0,len(self.kegs)-1))
        print(f'next keg : {keg} (still left {len(self.kegs)})')
        return self.test_tickets(keg)
    def add_player(self,name,ctn_ticket=1,bot=0):
        self.players.append(Player(name,ctn_ticket,bot))
    def test_tickets(self,keg=0):
        for ind_p,player in enumerate(self.players[:]):
            print(player.name+' Cards')
            for ind_t,ticket in enumerate(player.tickets[:]):
                print(ticket)
                if keg:
                    if not player.bot:
                        while True:
                            if(answer:=input(f'{keg} in {player.name} card? [y/n]').lower().strip()) and answer=='y':
                                do=True
                                break
                            elif answer=='n':
                                do=False
                                break
                            print('please type: y - yes or n - no ')
                        if (stat:=ticket.search_num(keg,do)):
                            if stat==1:
                                self.players[ind_p].tickets.pop(ind_t)
                                print(f'{player.name} ticket cant win!')
                                if not self.players[ind_p].tickets:
                                    self.players.pop(ind_p)
                                    print(f'{player.name} Lose!')
                                    if len(self.players)==1:
                                        print(f'{self.players[0].name} Win!')
                                        return False
                            elif stat==2:
                                print(f'{player.name} Win!')
                                return False
                    else:
                        if (stat:=ticket.search_num(keg,auto=True)):
                            print(f'{player.name} Win!')
                            return False
        return True
    def game_start(self):
        self.test_tickets()
        while self.next_round():
            pass

class Player:
    def __init__(self,name,ctn_ticket=1,bot=0):
        self.name=name
        self.bot=bot
        self.tickets=[]
        for _ in range(ctn_ticket):
            self.add_ticket()
    def add_ticket(self):
        self.tickets.append(Ticket())

class Ticket:
    def __init__(self):
        self.card=[]
        self.gen_card()
        self.ctn=15
    def gen_card(self):
        nums=random.sample(range(1, 91), 15)
        for i in range(3):
            self.card+=self.space_to_card(nums[i*5:(i+1)*5])
        # self.card=self.space_to_card(nums[0:5])+self.space_to_card(nums[5:10])+self.space_to_card(nums[10:15])
    def space_to_card(self,nums):
        nums.sort()
        while len(nums)<9:
            nums.insert(random.randint(0,len(nums)),0)
        return nums
    def search_num(self,num,do=False,auto=False):
        if num in self.card:
            if do or auto:
                self.card[self.card.index(num)]='xx'
                self.ctn-=1
                if not self.ctn:
                    return 2
                return False
            else:
                return 1
        elif do:
            return 1
        return False
    def __str__(self):
        out='--'*17+'\n'
        for i in range(3):
            for num in self.card[i*9:(i+1)*9]:
                if not num:
                    out+='  '
                elif num=='xx':
                    out+='xx'
                elif num<9:
                    out+=f' {num}'
                else:
                    out+=str(num)
                out+='  '
            out+='\n'
        out+='--'*17+'\n'
        return out

g=Game()
g.add_player('Player1')
g.add_player('Bot',bot=1)
g.add_player('Bot2',bot=1)
g.game_start()