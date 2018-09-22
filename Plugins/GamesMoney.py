from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var
from Utils import Engine as UEngine
import string as string_imp
from VK import VK
import datetime
import operator
import random
import codecs


class GamesMoneyPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Игры на деньги'
        self.description = 'Всякие разные игры со ставками'
        self.words = ["игра", "game"]
        # self.debug = True

    def func(self):
        try:
            banned = [465994133]
            if not int(self.user) in banned:
                bd_business = eval(codecs.open('DB\\bd_business.txt', 'r', 'utf-8').read())
                money = eval(open('DB\\money.txt', 'r').read())
                bank = eval(open('DB\\bank.txt', 'r').read())
                business = eval(codecs.open('DB\\business.txt', 'r', 'utf-8').read())
                lucky = eval(open('DB\\lucky.txt', 'r').read())
                items = eval(codecs.open('DB\\items.txt', 'r', 'utf-8').read())
                reputation = eval(open('DB\\reputation.txt', 'r').read())
                inventory = eval(codecs.open('DB\\inventory.txt', 'r', 'utf-8').read())
                slots = eval(open('DB\\slots.txt', 'r').read())
                donat = eval(open('DB\\donat.txt', 'r').read())
                credit = eval(open('DB\\credit.txt', 'r').read())
                bonus_code = eval(open('DB\\bonus_code.txt', 'r').read())
                req_game = eval(open('DB\\req_game.txt', 'r').read())
                cases = eval(codecs.open('DB\\cases.txt', 'r', 'utf-8').read())
                # vip = eval(open('DB\\vip.txt', 'r').read())
                if not str(self.user) in credit:
                    credit[str(self.user)] = {'credit': 0, 'day': 0}
                if not str(self.user) in money:
                    money[str(self.user)] = 0
                if not str(self.user) in donat:
                    donat[str(self.user)] = {'donat': 0, 'level': 0, 'vip': 0}
                if not str(self.user) in bank:
                    bank[str(self.user)] = 0
                if not str(self.user) in reputation:
                    reputation[str(self.user)] = 0
                if not str(self.user) in inventory:
                    inventory[str(self.user)] = {'Вещи': {'Телефон': 'Нет', 'Компьютер': 'Нет', 'Консоль': 'Нет'},
                                                 'Недвижимость': {'Дом': 'Нет', 'Офис': 'Нет'},
                                                 'Движимость': {'Машина': 'Нет', 'Самолет': 'Нет', 'Корабль': 'Нет'},
                                                 'Прочее': {'Страна': 'Нет', 'Планета': 'Нет', 'Танк': 'Нет'}
                                                 }
                if not str(self.user) in business:
                    business[str(self.user)] = {}
                    for name in bd_business:
                        business[str(self.user)][name] = {'amount': 0, 'profit': 0}
                if credit['today'] != datetime.datetime.now().day:
                    credit['today'] = datetime.datetime.now().day
                    for i in credit:
                        if i != 'today':
                            if credit[i]['credit']:
                                credit[i]['day'] -= 1
                                if not credit[i]['day']:
                                    money[i] -= credit[i]['credit']
                                    credit[i]['credit'] = 0
                if money['today'] != datetime.datetime.now().day:
                    money['today'] = datetime.datetime.now().day
                    for i in money:
                        if i != 'today':
                            if not i in reputation:
                                reputation[i] = 0
                            if not i in donat:
                                donat[i] = {'donat': 0, 'level': 0, 'vip': 0}
                            money[i] += 100 + (random.randint(0, reputation[i])) + (donat[i]['donat'] * 10)
                if business['today'] != datetime.datetime.now().day:
                    business['today'] = datetime.datetime.now().day
                    for user in business:
                        if user != 'today':
                            for bus in business[user]:
                                if business[user][bus]['amount']:
                                    _wn_bus = random.choice([True, False])
                                    if _wn_bus:
                                        business[user][bus]['profit'] += random.randint(bd_business[bus]['profit']['min'],
                                                                                        bd_business[bus]['profit']['max'])
                                    else:
                                        business[user][bus]['profit'] += random.randint(bd_business[bus]['loss']['min'],
                                                                                        bd_business[bus]['loss']['max'])
                if donat['today'] != datetime.datetime.now().day:
                    donat['today'] = datetime.datetime.now().day
                    for user in donat:
                        if user != 'today':
                            donat[user]['donat'] += 1
                            if donat[user]['donat'] >= 10:
                                donat[user]['level'] = 1
                                donat[user]['vip'] = 1
                            if donat[user]['donat'] >= 50:
                                donat[user]['level'] = 2
                                donat[user]['vip'] = 2
                            if donat[user]['donat'] >= 100:
                                donat[user]['level'] = 3
                                donat[user]['vip'] = 3
                            if donat[user]['donat'] >= 250:
                                donat[user]['level'] = 4
                                donat[user]['vip'] = 4
                            if donat[user]['donat'] >= 500:
                                donat[user]['level'] = 5
                                donat[user]['vip'] = 5
                            if donat[user]['donat'] >= 1000:
                                donat[user]['level'] = 6
                                donat[user]['vip'] = 6
                            if donat[user]['donat'] >= 2000:
                                donat[user]['level'] = 7
                                donat[user]['vip'] = 7
                            if donat[user]['donat'] >= 4000:
                                donat[user]['level'] = 8
                                donat[user]['vip'] = 8
                            if donat[user]['donat'] >= 7000:
                                donat[user]['level'] = 9
                                donat[user]['vip'] = 9
                            if donat[user]['donat'] >= 10000:
                                donat[user]['level'] = 10
                                donat[user]['vip'] = 10
                f = open('DB\\money.txt', 'w')
                f.write(str(money))
                f.close()
                f = open('DB\\bank.txt', 'w')
                f.write(str(bank))
                f.close()
                f = codecs.open('DB\\business.txt', 'w', 'utf-8')
                f.write(str(business))
                f.close()
                f = open('DB\\reputation.txt', 'w')
                f.write(str(reputation))
                f.close()
                f = codecs.open('DB\\inventory.txt', 'w', 'utf-8')
                f.write(str(inventory))
                f.close()
                f = open('DB\\donat.txt', 'w')
                f.write(str(donat))
                f.close()
                tm = f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}'
                if len(str(self.text)) == 0:
                    _rs = f"[{tm}]\n" \
                          f"Раз в день всем начисляется по 100 монет. Также, 1 любое сообщение в беседе = 1 монета\n" \
                          f"Чем больше репутация, тем больше бонус каждый день\n" \
                          f"Также, донат дает бонус на ежедневный бонус и вип-уровень\n" \
                          f"Чем больше вип-уровень, тем больше попыток в вип игре\n" \
                          f"Деньги можно хранить в банке до 7.500.000, но при снятии берется НДС 0.01%-99.9%\n" \
                          f"Доступные игры:\n" \
                          f"Дуэль [ставка] (Вы можете получить 150% или потерять ставку)\n" \
                          f"Казино [ставка] [red/black/green] (Вы можете потерять ставку или выиграть 150% или 1000%)\n" \
                          f"Биржа [ставка] [время] (Никто не знает, что будет после игры)\n" \
                          f"Кейс [номер] (Равные шансы получить и потерять деньги)\n" \
                          f"Слоты [ставка] (Может выпасть джек-пот или % от ставки)\n" \
                          f"Заявка [ставка] (Шанс выиграть 50% если кто-то примет)\n" \
                          f"Стратегия [0 | 1]{10} (Ставка 100, меняется раз в день, шанс выиграть до 2.000)\n" \
                          f"Также доступен магазин, банк, бизнес, кредит, баланс и передача\n" \
                          f"И дополнительные команды: топ, доход, суицид, экономика и вип\n" \
                          f"Примеры:\n" \
                          f"!игра [Рулетка 5 / Дуэль 10 / Казино 50 красное / Кейс 3]\n" \
                          f"!игра [Магазин 1 1 / Банк 3 / бизнес 2 / баланс]\n" \
                          f"!клад дает шанс 5% найти монетки до 100% от вашего баланса 1 раз в минуту для всех"
                    self.result['message'] = _rs
                else:
                    rate = [i for i in self.text.split()]
                    if len(rate):
                        if rate[0] == 'рулетка_пока_не_робит_лол':
                            rate = rate[1:]
                            rate = [int(i) for i in rate if UEngine.is_int(i)]
                            if len(rate):
                                if 10000 >= rate[0] >= 100:
                                    if rate[0] <= money[str(self.user)]:
                                        end = ''
                                        tru = random.randint(0, 6)
                                        if tru == 0:
                                            money[str(self.user)] -= rate[0]
                                            end = f'-{rate[0]}'
                                        if tru == 1:
                                            money[str(self.user)] -= int(rate[0] / 2)
                                            end = f'-{int(rate[0] / 2)}'
                                        if tru == 2:
                                            money[str(self.user)] -= int(rate[0] / 4)
                                            end = f'-{int(rate[0] / 4)}'
                                        if tru == 3:
                                            money[str(self.user)] += 0
                                            end = '0'
                                        if tru == 4:
                                            money[str(self.user)] += int(rate[0] / 4)
                                            end = f'{int(rate[0] / 4)}'
                                        if tru == 5:
                                            money[str(self.user)] += int(rate[0] / 2)
                                            end = f'{int(rate[0] / 2)}'
                                        if tru == 6:
                                            money[str(self.user)] += rate[0]
                                            end = f'{rate[0]}'
                                        self.result['message'] = f'[{tru}] Ваш выигрыш: {end}'
                                        f = open('DB\\money.txt', 'w')
                                        f.write(str(money))
                                        f.close()
                                    else:
                                        self.result['message'] = 'Ваших денег не хватает.'
                                else:
                                    self.result['message'] = 'Допустимая ставка: 100-10.000'
                            else:
                                self.result['message'] = 'Введите ставку'
                        elif rate[0] == 'дуэль':
                            rate = rate[1:]
                            rate = [int(i) for i in rate if UEngine.is_int(i)]
                            if len(rate):
                                if 100 <= rate[0] <= 10000:
                                    if rate[0] <= money[str(self.user)]:
                                        win = random.choice([True, False])
                                        if win:
                                            money[str(self.user)] += int(rate[0] / 2)
                                            self.result['message'] = f'Вы получили {int(rate[0] / 2)}.'
                                        else:
                                            money[str(self.user)] -= rate[0]
                                            self.result['message'] = f'Вы проиграли ставку.'
                                        f = open('DB\\money.txt', 'w')
                                        f.write(str(money))
                                        f.close()
                                    else:
                                        self.result['message'] = 'Ваших денег не хватает.'
                                else:
                                    self.result['message'] = 'Допустимая ставка: 100-10.000'
                            else:
                                self.result['message'] = 'Введите ставку.'
                        elif rate[0] == 'казино':
                            rate = rate[1:]
                            rate = [int(i) for i in rate if UEngine.is_int(i)]
                            if len(rate):
                                if rate[0] <= money[str(self.user)]:
                                    if 100 <= rate[0] <= 10000:
                                        color = random.randint(0, 100)
                                        color = 'red' if color < 45 else ('black' if color < 90 else 'green')
                                        if 'red' in self.text or 'красное' in self.text:
                                            if color == 'red':
                                                money[str(self.user)] += int(rate[0] * 1.5)
                                                self.result['message'] = f'Вы выиграли {int(rate[0] / 2)}'
                                            else:
                                                money[str(self.user)] -= int(rate[0])
                                                self.result['message'] = f'Вы потеряли {rate[0]}'
                                        elif 'black' in self.text or 'черное' in self.text:
                                            if color == 'black':
                                                money[str(self.user)] += int(rate[0] * 1.5)
                                                self.result['message'] = f'Вы выиграли {int(rate[0] / 2)}'
                                            else:
                                                money[str(self.user)] -= rate[0]
                                                self.result['message'] = f'Вы потеряли {rate[0]}'
                                        elif 'green' in self.text or 'зеленое' in self.text:
                                            if color == 'green':
                                                money[str(self.user)] += rate[0] * 10
                                                self.result['message'] = f'Вы выиграли {rate[0] * 10}'
                                            else:
                                                money[str(self.user)] -= rate[0]
                                                self.result['message'] = f'Вы потеряли {rate[0]}'
                                        else:
                                            self.result['message'] = 'Введите red/black/green.'
                                    else:
                                        self.result['message'] = 'Допустимая ставка 100-10.000'
                                else:
                                    self.result['message'] = 'Ваших денег не хватает.'
                            else:
                                self.result['message'] = 'Введите ставку и цвет'
                        elif rate[0] == 'кейс':
                            rate = rate[1:]
                            rate = [(r[0].upper() + r[1:].lower()) for r in rate]
                            if not len(rate):
                                _str = f"[{money[str(self.user)]}] Кейсы дают возможность поднять мани:\n"
                                for i in cases:
                                    _str += f'[{cases[i]["cost"]}] Кейс \'{i}\' ({cases[i]["profit"]["min"]} - {cases[i]["profit"]["max"]})\n'
                                self.result['message'] = _str
                            else:
                                if rate[0] in cases:
                                    if money[str(self.user)] >= cases[rate[0]]['cost']:
                                        money[str(self.user)] -= cases[rate[0]]['cost']
                                        win = random.randint(cases[rate[0]]['profit']['min'], cases[rate[0]]['profit']['max'])
                                        money[str(self.user)] += win
                                        self.result['message'] = f'Вам выпало {win} монет ({win - cases[rate[0]]["cost"]})'
                                    else:
                                        self.result['message'] = 'Вам не хватает денег.'
                                else:
                                    self.result['message'] = 'Кейса с таким именем нет.'
                        elif rate[0] == 'слоты':
                            rate = rate[1:]
                            if len(rate):
                                if UEngine.is_int(rate[0]):
                                    if int(rate[0]) <= money[str(self.user)]:
                                        if 10000 >= int(rate[0]) >= 100:
                                            money[str(self.user)] -= int(rate[0])
                                            slots['total'] += int(rate[0])
                                            symbols = '♦♣♠'
                                            win = '--'
                                            string = f'Джекпот: {slots["total"]}\n'
                                            for i in range(3):
                                                win += random.choice(symbols)
                                            win += '--\n->'
                                            for i in range(3):
                                                win += random.choice(symbols)
                                            win += '<-\n--'
                                            for i in range(3):
                                                win += random.choice(symbols)
                                            win += '--\n'
                                            win_str = win
                                            win = win[10:13]
                                            string += win_str
                                            winrate = 0
                                            for i in win:
                                                if i == '♦':
                                                    winrate += random.randint(10, 15)
                                                elif i == '♣':
                                                    winrate += random.randint(20, 25)
                                                elif i == '♠':
                                                    winrate += random.randint(30, 35)
                                            if winrate > 30:
                                                if winrate == 105:
                                                    money[str(self.user)] += slots['total']
                                                    self.result['message'] = string + f'[{winrate}] \nТы сорвал джек-пот!' \
                                                                                      f' ({slots["total"]})'
                                                    slots['total'] = 1000
                                                else:
                                                    wn = int(int(rate[0]) * (winrate / random.randint(65, 100)))
                                                    self.result['message'] = string + f'[{winrate}] \nВы выиграли: {wn}' \
                                                                                      f' ({wn - int(rate[0])})'
                                                    money[str(self.user)] += wn
                                                    slots['total'] -= wn
                                            else:
                                                self.result['message'] = 'Вы все проиграли'
                                            if slots['total'] < 0:
                                                slots['total'] = 0
                                        else:
                                            self.result['message'] = 'Принимаются ставки 100-10.000'
                                    else:
                                        self.result['message'] = 'Ваших денег не хватает.'
                                else:
                                    self.result['message'] = 'Введите ставку.'
                            else:
                                self.result['message'] = 'Введите ставку.'
                        elif rate[0] == 'биржа':
                            rate = rate[1:]
                            rate = [int(i) for i in rate if UEngine.is_int(i)]
                            if not len(rate):
                                self.result['message'] = 'Биржа - всегда риск, можно как уйти в +, так и в -'
                            else:
                                if len(rate) == 2:
                                    if rate[0] <= money[str(self.user)]:
                                        if 10000 >= rate[0] >= 100:
                                            if 1000 >= rate[1] >= 10:
                                                strt = rate[0]
                                                money[str(self.user)] -= rate[0]
                                                _min = rate[0]
                                                _max = rate[0]
                                                mon = rate[0]
                                                for _ in range(rate[1]):
                                                    mon += random.randint(-int(rate[0] / 10), int(rate[0] / 10))
                                                    _min = mon if _min > mon else _min
                                                    _max = mon if _max < mon else _max
                                                money[str(self.user)] += mon
                                                self.result['message'] = f'Вы забираете: {mon - strt}\n' \
                                                                         f'Последний результат: {mon}\n' \
                                                                         f'Диапазон: {_min}-{_max}'
                                            else:
                                                self.result['message'] = 'Время должно быть боль 10 и меньше 1000'
                                        else:
                                            self.result['message'] = 'Допустимая ставка 100-10.000'
                                    else:
                                        self.result['message'] = 'Недостаточно денег'
                                else:
                                    self.result['message'] = 'Введите ставку и время'
                        elif rate[0] == 'заявка':
                            if len(rate) > 1:
                                if rate[1] == 'создать':
                                    if len(rate) > 2:
                                        if UEngine.is_int(rate[2]):
                                            if int(rate[2]) <= money[str(self.user)]:
                                                if 10000 >= int(rate[2]) >= 100:
                                                    money[str(self.user)] -= int(rate[2])
                                                    req_game[str(req_game['id'])] = {'user': str(self.user), 'rate': int(rate[2]), 'available': True}
                                                    self.result['message'] = f'Заявка создана, ее id: {req_game["id"]}.'
                                                    req_game['id'] += 1
                                                else:
                                                    self.result['message'] = 'Ставка должна быть в диапазоне 100-10.000'
                                            else:
                                                self.result['message'] = 'Ваших денег недостаточно.'
                                        else:
                                            self.result['message'] = 'Вы не ввели ставку.'
                                    else:
                                        self.result['message'] = 'Введите ставку.'
                                elif rate[1] == 'принять':
                                    if len(rate) > 2:
                                        if UEngine.is_int(rate[2]):
                                            if str(rate[2]) in req_game:
                                                if req_game[str(rate[2])]['available']:
                                                    if money[str(self.user)] >= req_game[str(rate[2])]['rate']:
                                                        money[str(self.user)] -= req_game[str(rate[2])]['rate']
                                                        req_game[str(rate[2])]['available'] = False
                                                        if random.choice([True, False]):
                                                            money[str(self.user)] += 2 * req_game[str(rate[2])]['rate']
                                                            self.result['message'] = 'Вы выиграли.'
                                                        else:
                                                            money[req_game[str(rate[2])]['user']] += 2 * req_game[str(rate[2])]['rate']
                                                            self.result['message'] = 'Вы проиграли.'
                                                    else:
                                                        self.result['message'] = 'Ваших денег недостаточно.'
                                                else:
                                                    self.result['message'] = 'Эта ставка недоступна.'
                                            else:
                                                self.result['message'] = 'Такой заявки не существует.'
                                        else:
                                            self.result['message'] = 'Вы не ввели id.'
                                    else:
                                        self.result['message'] = 'Введите ID.'
                                elif rate[1] == 'история':
                                    _str = 'История заявок:\n'
                                    for i in req_game:
                                        if i != 'id':
                                            _str += i + '. ' + UEngine.get_username_by_id(req_game[i]['user']) + ' ' + str(req_game[i]['rate']) + ' (' + ('x' if not req_game[i]['available'] else 'o') + ')\n'
                                    self.result['message'] = _str
                                else:
                                    self.result['message'] = 'Вы можете либо создать, либо принять заявку.'
                            else:
                                _str = ''
                                for i in req_game:
                                    if i != 'id':
                                        if req_game[i]['available']:
                                            _str += f'{i}: {UEngine.get_username_by_id(req_game[i]["user"])} ({req_game[i]["rate"]})\n'
                                self.result['message'] = 'Доступные заявки:\n' + _str
                        elif rate[0] == 'стратегия':
                            stat = eval(codecs.open('DB\\strategy.txt', 'r', 'utf-8').read())
                            if not stat['today']:
                                if len(rate) > 1:
                                    if money[str(self.user)] >= 100:
                                        if len(rate[1]) == 10:
                                            print()
                                            for i in str(rate[1]):
                                                if i != '0' and i != '1':
                                                    self.result['message'] = 'Цирфа должна быть 1|0.'
                                                    return True
                                            money[str(self.user)] -= 100
                                            dt = datetime.datetime.now()
                                            random.seed(dt.year + dt.month + dt.day)
                                            a = 0
                                            ind = 0
                                            op = False
                                            lst = [bool(int(i)) for i in rate[1]]
                                            wns = ''
                                            while ind < len(lst):
                                                current = random.choice([True, False])
                                                if lst[ind] == current and not op:
                                                    a += 1
                                                    wns += str(int(current))
                                                else:
                                                    wns += '*'
                                                    op = True
                                                ind += 1
                                            if a < 10:
                                                self.result['message'] = f'Не повезло, споткнулся на {a+1} шаге ({wns})'
                                            else:
                                                win = random.randint(1, 2000)
                                                money[str(self.user)] += win
                                                stat['winner'] = UEngine.get_username_by_id(self.user)
                                                f = codecs.open('DB\\strategy.txt', 'w', 'utf-8')
                                                f.write(str(stat))
                                                f.close()
                                                self.result['message'] = f'Ахуеть, ты угадал все шаги, твоя награда: {win}'
                                        else:
                                            self.result['message'] = 'Должно быть 10 цифр.'
                                    else:
                                        self.result['message'] = 'У вас должно быть 100+ монет для игры.'
                                else:
                                    self.result['message'] = 'Введите последовательность из десяти 1|0. (ex: 1010101010)'
                            else:
                                self.result['message'] = f'Сегодня уже выиграл: {stat["winner"]}'
                        elif rate[0] == 'суицид_теперь_не_доступен_лол':
                            money[str(self.user)] = -200
                            bank[str(self.user)] = -200
                            reputation[str(self.user)] = 0
                            business[str(self.user)] = {}
                            for name in bd_business:
                                business[str(self.user)][name] = {'amount': 0, 'profit': 0}
                            inventory[str(self.user)] = {'Вещи': {'Телефон': 'Нет', 'Компьютер': 'Нет', 'Консоль': 'Нет'},
                                                         'Недвижимость': {'Дом': 'Нет', 'Офис': 'Нет'},
                                                         'Движимость': {'Машина': 'Нет', 'Самолет': 'Нет',
                                                                        'Корабль': 'Нет'},
                                                         'Прочее': {'Страна': 'Нет', 'Планета': 'Нет', 'Танк': 'Нет'}
                                                         }
                            credit[str(self.user)] = {'credit': 0, 'day': 0}
                            for i in req_game:
                                if req_game[i]['user'] == str(self.user):
                                    req_game[i]['available'] = False
                            self.result['message'] = 'Бб.'
                        elif rate[0] == 'топ':
                            self.text = self.text.replace('топ', '')
                            users = VK().Messages().get_chat(fields='first_name, last_name')['users']
                            users_ids = [i['id'] for i in users]
                            rate = [txt.lower() for txt in self.text.split()]
                            if not len(rate):
                                self.result['message'] = 'Тут можно узнать топ богачей\n-Баланс\n-Банк\nБизнес'
                            else:
                                if rate[0] == 'баланс':
                                    _str = 'Топ балансов:\n'
                                    ind = 0
                                    mas = sorted(money.items(), key=operator.itemgetter(1), reverse=True)
                                    d = str(mas)
                                    d = d.replace('(', '')
                                    d = d.replace("',", "':")
                                    d = d.replace(')', '')
                                    d = d.replace('[', '{')
                                    d = d.replace(']', '}')
                                    d = eval(d)
                                    for k in sorted(d.items(), reverse=True, key=operator.itemgetter(1)):
                                        if k[0] != 'today':
                                            if int(k[0]) in users_ids:
                                                _str += f'{ind+1}. {[ji["first_name"] + " " + ji["last_name"] for ji in users if ji["id"] == int(k[0])][0]}: {k[1]}\n'
                                                ind += 1
                                    self.result['message'] = _str
                                elif rate[0] == 'банк':
                                    _str = 'Топ счетов:\n'
                                    ind = 0
                                    mas = sorted(bank.items(), key=operator.itemgetter(1), reverse=True)
                                    d = str(mas)
                                    d = d.replace('(', '')
                                    d = d.replace("',", "':")
                                    d = d.replace(')', '')
                                    d = d.replace('[', '{')
                                    d = d.replace(']', '}')
                                    d = eval(d)
                                    for k in sorted(d.items(), reverse=True, key=operator.itemgetter(1)):
                                        if k[0] != 'today':
                                            if int(k[0]) in users_ids:
                                                _str += f'{ind+1}. {[ji["first_name"] + " " + ji["last_name"] for ji in users if ji["id"] == int(k[0])][0]}: {k[1]}\n'
                                                ind += 1
                                    self.result['message'] = _str
                                elif rate[0] == 'бизнес':
                                    _str = 'Топ бизнесов:\n'
                                    ind = 0
                                    mas = dict()
                                    for user in business:
                                        if user != 'today':
                                            _max = 0
                                            for bs in business[user]:
                                                if business[user][bs]['amount']:
                                                    _max += bd_business[bs]['cost'] * business[user][bs]['amount']
                                            mas[user] = _max
                                    mas = sorted(mas.items(), key=operator.itemgetter(1), reverse=True)
                                    d = str(mas)
                                    d = d.replace('(', '')
                                    d = d.replace("',", "':")
                                    d = d.replace(')', '')
                                    d = d.replace('[', '{')
                                    d = d.replace(']', '}')
                                    d = eval(d)
                                    for k in sorted(d.items(), reverse=True, key=operator.itemgetter(1)):
                                        if k[0] != 'today':
                                            if int(k[0]) in users_ids:
                                                _str += f'{ind+1}. {[ji["first_name"] + " " + ji["last_name"] for ji in users if ji["id"] == int(k[0])][0]}: {k[1]}\n'
                                                ind += 1
                                    self.result['message'] = _str
                                elif rate[0] == 'репутация':
                                    _str = 'Топ репутации:\n'
                                    ind = 0
                                    mas = sorted(reputation.items(), key=operator.itemgetter(1), reverse=True)
                                    d = str(mas)
                                    d = d.replace('(', '')
                                    d = d.replace("',", "':")
                                    d = d.replace(')', '')
                                    d = d.replace('[', '{')
                                    d = d.replace(']', '}')
                                    d = eval(d)
                                    for k in sorted(d.items(), reverse=True, key=operator.itemgetter(1)):
                                        if k[0] != 'today':
                                            if int(k[0]) in users_ids:
                                                _str += f'{ind+1}. {[ji["first_name"] + " " + ji["last_name"] for ji in users if ji["id"] == int(k[0])][0]}: {k[1]}\n'
                                                ind += 1
                                    self.result['message'] = _str
                                else:
                                    self.result['message'] = 'Такого пункта нет'
                        elif rate[0] == 'код':
                            if len(rate) > 1:
                                if rate[1] == 'создать':
                                    if int(self.user) == var.czarID:
                                        if len(rate) > 2:
                                            # code = ''
                                            _alh = string_imp.ascii_uppercase + string_imp.digits
                                            code = ''
                                            _ind_dig = []
                                            while not len(_ind_dig):
                                                code = code[0:0]
                                                for _ in range(3):
                                                    for _ in range(7):
                                                        code += random.choice(_alh)
                                                        if code[len(code) - 1] in string_imp.digits:
                                                            _ind_dig.append(len(code) - 1)
                                                    code += '-'
                                                code = code[:len(code) - 1]
                                            win_code = code
                                            ind = random.choice(_ind_dig)
                                            code = code[:ind] + '*' + code[ind + 1:]
                                            bonus_code[win_code] = {'cost': int(rate[2]), 'users': 1, 'list': []}
                                            self.result['message'] = f'* - цифра 0-9, код: {code}'
                                        else:
                                            self.result['message'] = 'Введите стоимость.'
                                    else:
                                        self.result['message'] = 'Только админ может это делать.'
                                elif rate[1] == 'активировать':
                                    if len(rate) > 2:
                                        if rate[2].upper() in bonus_code:
                                            if bonus_code[rate[2].upper()]['users']:
                                                if not int(self.user) in bonus_code[rate[2].upper()]['list']:
                                                    bonus_code[rate[2].upper()]['users'] -= 1
                                                    bonus_code[rate[2].upper()]['list'].append(int(self.user))
                                                    self.result[
                                                        'message'] = f'Вы активировали код на {bonus_code[rate[2].upper()]["cost"]}'
                                                    money[str(self.user)] += bonus_code[rate[2].upper()]['cost']
                                                else:
                                                    self.result['message'] = 'Вы уже активировали этот код.'
                                            else:
                                                self.result['message'] = 'Этот код уже недоступен.'
                                        else:
                                            self.result['message'] = 'Такого кода нет.'
                                    else:
                                        self.result['message'] = 'Введите код.'
                                else:
                                    self.result['message'] = 'Такого пункта нет, можно актвировать или создать.'
                            else:
                                self.result['message'] = 'Можно создать или актвировтаь бонус-код.'
                        elif rate[0] == 'передать':
                            if len(rate) > 2:
                                nums = [int(s) for s in rate if UEngine.is_int(s)]
                                if len(nums) == 2:
                                    users = VK().Messages().get_chat()['users']
                                    if nums[0] in users or nums[1] in users:
                                        if nums[0] in users and str(self.user) != str(nums[0]):
                                            if nums[1] > 0:
                                                if money[str(self.user)] >= int(nums[1]):
                                                    money[str(self.user)] -= int(nums[1])
                                                    money[str(nums[0])] += int(nums[1])
                                            else:
                                                self.result['message'] = 'Передать можно только положительную сумму.'
                                        elif nums[1] in users and str(self.user) != str(nums[1]):
                                            if nums[0] > 0:
                                                if money[str(self.user)] >= int(nums[0]):
                                                    money[str(self.user)] -= int(nums[0])
                                                    money[str(nums[1])] += int(nums[0])
                                            else:
                                                self.result['message'] = 'Передать можно только положительную сумму.'
                                        self.result['message'] = 'Передано.'
                                    else:
                                        self.result['message'] = 'Пользователя с таким id нет.'
                                else:
                                    self.result['message'] = 'Введите ID и сумму.'
                            else:
                                self.result['message'] = 'Введите ID и сумму.'
                        elif rate[0] == 'добавить':
                            if int(self.user) == var.czarID:
                                self.text = self.text.replace('добавить', '')
                                nums = [int(s) for s in self.text.split() if s.isdigit()]
                                if len(nums) != 2:
                                    self.result['message'] = 'Введите ID и количество.'
                                else:
                                    users = VK().Messages().get_chat()['users']
                                    if nums[0] in users or nums[1] in users:
                                        if nums[0] in users:
                                            money[str(nums[0])] += nums[1]
                                        else:
                                            money[str(nums[1])] += nums[0]
                                        self.result['message'] = 'Деньги добавлены.'
                                    else:
                                        self.result['message'] = 'Пользователя с таким id нет.'
                            else:
                                self.result['message'] = 'Только админ имеет на это право.'
                        elif rate[0] == 'бонус':
                            self.text = self.text.replace('бонус', '')
                            if int(self.user) == var.czarID:
                                if len(str(self.text)) > 0:
                                    if UEngine.is_int(self.text):
                                        for i in money:
                                            if i != 'today':
                                                money[i] += int(self.text)
                                        self.result['message'] = f'Всем начислено по {int(self.text)} монет'
                                    else:
                                        self.result['message'] = 'Введите число'
                                else:
                                    self.result['message'] = 'Введите количество'
                            else:
                                self.result['message'] = 'Только админ может пользоваться этим.'
                        elif rate[0] == 'вайп':
                            if int(self.user) == var.czarID:
                                vip = eval(open('DB\\vip.txt', 'r').read())
                                for i in credit:
                                    credit[i] = {'credit': 0, 'day': 0}
                                slots['total'] = 0
                                vip['total'] = 1000
                                for i in req_game:
                                    req_game[i]['available'] = False
                                for i in money:
                                    if i != 'today':
                                        money[i] = 0
                                for i in bank:
                                    if i != 'today':
                                        bank[i] = 0
                                for i in business:
                                    if i != 'today':
                                        business[str(self.user)] = {}
                                        for name in bd_business:
                                            business[str(self.user)][name] = {'amount': 0, 'profit': 0}
                                for i in reputation:
                                    reputation[i] = 0
                                for i in inventory:
                                    inventory[i] = {'Вещи': {'Телефон': 'Нет', 'Компьютер': 'Нет', 'Консоль': 'Нет'},
                                                    'Недвижимость': {'Дом': 'Нет', 'Офис': 'Нет'},
                                                    'Движимость': {'Машина': 'Нет', 'Самолет': 'Нет', 'Корабль': 'Нет'},
                                                    'Прочее': {'Страна': 'Нет', 'Планета': 'Нет', 'Танк': 'Нет'}
                                                    }
                                for i in credit:
                                    if i != 'today':
                                        credit[i] = {'credit': 0, 'day': 0}
                                f = open('DB\\vip.txt', 'w')
                                f.write(str(vip))
                                f.close()
                            else:
                                self.result['message'] = 'Только админ может это использовать.'
                        elif rate[0] == 'банк':
                            self.text = self.text.replace('банк', '')
                            if bank['today'] != datetime.datetime.now().day:
                                raz = 0
                                if bank['today'] < datetime.datetime.now().day:
                                    raz += datetime.datetime.now().day - bank['today']
                                else:
                                    raz += datetime.datetime.now().day
                                bank['today'] = datetime.datetime.now().day
                                td = random.randint(105, 110) / 100
                                for _ in range(raz):
                                    for i in bank:
                                        if i != 'today':
                                            bank[i] = int(bank[i] * td)
                            _str = f"[{tm}] В банке можно хранить деньги и постепенно увеличивать" \
                                   f" счет на 5-10% в день\n-Положить\n-Снять\n-Баланс"
                            rate = [txt.lower() for txt in self.text.split()]
                            if not len(rate):
                                self.result['message'] = _str
                            else:
                                sm = 0
                                if rate[0] == 'положить':
                                    if len(rate) == 1:
                                        self.result['message'] = f'Вы можете положить {bank[str(self.user)]} или же 1-100%'
                                    else:
                                        if UEngine.is_int(rate[1]):
                                            if int(rate[1]) < 1 or int(rate[1]) > money[str(self.user)]:
                                                self.result['message'] = f'Введите корректное ' \
                                                                         f'количество 1-{money[str(self.user)]}'
                                            else:
                                                sm += int(rate[1])
                                                money[str(self.user)] -= sm
                                                bank[str(self.user)] += sm
                                                self.result['message'] = f'Вы положили: {sm}'
                                        elif '%' in rate[1]:
                                            rate[1] = rate[1].replace('%', '')
                                            if UEngine.is_int(rate[1]):
                                                if int(rate[1]) < 1 or int(rate[1]) > 100:
                                                    self.result['message'] = 'Введите корректное количество 1-100%'
                                                else:
                                                    sm += int(money[str(self.user)] * int(rate[1]) / 100)
                                                    money[str(self.user)] -= sm
                                                    bank[str(self.user)] += sm
                                                    self.result['message'] = f'Вы положили: {sm}'
                                            else:
                                                self.result['message'] = 'Введите число'
                                        else:
                                            self.result['message'] = 'Введите в ?% или сумму'
                                elif rate[0] == 'снять':
                                    nds = 1 - random.randint(1, 9999) / 10000
                                    if len(rate) == 1:
                                        self.result['message'] = f'Вы можете снять {bank[str(self.user)]} или же 1-100%'
                                    else:
                                        if bank[str(self.user)] > 0:
                                            if UEngine.is_int(rate[1]):
                                                if int(rate[1]) < 1 or int(rate[1]) > bank[str(self.user)]:
                                                    self.result['message'] = f'Введите корректное количество ' \
                                                                             f'1-{bank[str(self.user)]}'
                                                else:
                                                    sm = int(rate[1])
                                                    money[str(self.user)] += int(sm * nds)
                                                    bank[str(self.user)] -= sm
                                                    self.result['message'] = f'Вы сняли: {int(sm * nds)} (Из {sm}) (НДС: {100-(nds*100)}%)'
                                            elif '%' in rate[1]:
                                                rate[1] = rate[1].replace('%', '')
                                                if UEngine.is_int(rate[1]):
                                                    if int(rate[1]) < 1 or int(rate[1]) > 100:
                                                        self.result['message'] = 'Введите корректное количество 1-100%'
                                                    else:
                                                        sm = int(bank[str(self.user)] * int(rate[1]) / 100)
                                                        money[str(self.user)] += int(sm * nds)
                                                        bank[str(self.user)] -= sm
                                                        self.result['message'] = f'Вы сняли: {int(sm * nds)} (Из {sm}) (НДС: {100-(nds*100)}%)'
                                                else:
                                                    self.result['message'] = 'Введите число'
                                            else:
                                                self.result['message'] = 'Введите в ?% или сумму'
                                        else:
                                            self.result['message'] = 'Ваш счет пуст.'
                                elif rate[0] == 'баланс':
                                    self.result['message'] = f'Ваш баланс: {bank[str(self.user)]}'
                                else:
                                    self.result['message'] = 'Такого пункта нет'
                        elif rate[0] == 'бизнес':
                            self.text = self.text.replace('бизнес', '')
                            _str = f"[{tm}] Бизнесы приносят доход ежедневно, " \
                                   f"но вас всегда могут обокрасть.\n-Купить\n"
                            for name in bd_business:
                                _str += f'[{bd_business[name]["cost"]}] -{name} ' \
                                        f'{bd_business[name]["profit"]["min"]}-{bd_business[name]["profit"]["max"]} ' \
                                        f'(-{bd_business[name]["loss"]["min"]} - -{bd_business[name]["loss"]["max"]})\n'
                            _str += "-Имеется\n-Баланс\n-Доход\n-Убыток\n-Снять"
                            rate = [txt.lower() for txt in self.text.split()]
                            if not len(rate):
                                self.result['message'] = _str
                            else:
                                if rate[0] == 'купить':
                                    rate[1] = rate[1][0].upper() + rate[1][1:]
                                    if rate[1] == 'Вуз':
                                        rate[1] = 'ВУЗ'
                                    if rate[1] == 'Сми':
                                        rate[1] = 'СМИ'
                                    if rate[1] in bd_business:
                                        if len(rate) > 2:
                                            if UEngine.is_int(rate[2]):
                                                if int(rate[2]) * bd_business[rate[1]]['cost'] <= money[str(self.user)]:
                                                    money[str(self.user)] -= bd_business[rate[1]]['cost'] * int(rate[2])
                                                    business[str(self.user)][rate[1]]['amount'] += int(rate[2])
                                                    self.result['message'] = f'Вы успешно купили этот бизнес (x{rate[2]})'
                                                else:
                                                    self.result['message'] = 'Не хватает денег.'
                                            else:
                                                self.result['message'] = 'Введите корректное количество.'
                                        if money[str(self.user)] >= bd_business[rate[1]]['cost']:
                                            money[str(self.user)] -= bd_business[rate[1]]['cost']
                                            business[str(self.user)][rate[1]]['amount'] += 1
                                            self.result['message'] = 'Вы успешно купили этот бизнес'
                                        else:
                                            self.result['message'] = 'Ваших денег не хватает для покупки'
                                    else:
                                        self.result['message'] = 'Такого бизнеса нет'
                                elif rate[0] == 'имеется':
                                    _str = 'Ваши бизнесы:\n'
                                    for bs in business[str(self.user)]:
                                        if business[str(self.user)][bs]['amount']:
                                            _str += f'[x{business[str(self.user)][bs]["amount"]}] {bs}\n'
                                    self.result['message'] = _str
                                elif rate[0] == 'баланс':
                                    profit = 0
                                    for item in business[str(self.user)]:
                                        profit += business[str(self.user)][item]['profit'] * business[str(self.user)][item][
                                            'amount']
                                    self.result['message'] = f'Ваш баланс: {profit}'
                                elif rate[0] == 'доход':
                                    _str = 'Ваш примерный доход в день: '
                                    _min = 0
                                    _max = 0
                                    for bs in business[str(self.user)]:
                                        if business[str(self.user)][bs]['amount']:
                                            _min += bd_business[bs]['loss']['max'] * business[str(self.user)][bs][
                                                'amount']
                                            _max += bd_business[bs]['profit']['max'] * business[str(self.user)][bs][
                                                'amount']
                                    _str += f'-{_min} - {_max}'
                                    self.result['message'] = _str
                                elif rate[0] == 'убыток':
                                    _str = 'Ваш примерный убыток в день: '
                                    _min = 0
                                    _max = 0
                                    for bs in business[str(self.user)]:
                                        if business[str(self.user)][bs]['amount']:
                                            _min += bd_business[bs]['loss']['min'] * business[str(self.user)][bs]['amount']
                                            _max += bd_business[bs]['loss']['max'] * business[str(self.user)][bs]['amount']
                                    _str += f'{_min}-{_max}'
                                    self.result['message'] = _str
                                elif rate[0] == 'снять':
                                    profit = 0
                                    for item in business[str(self.user)]:
                                        profit += business[str(self.user)][item]['profit'] * business[str(self.user)][item][
                                            'amount']
                                        business[str(self.user)][item]['profit'] = 0
                                    if profit > 0:
                                        steal = random.choice([True, False])
                                        if steal:
                                            full = profit
                                            mns = (random.randint(0, 100) / 100)
                                            profit = int(profit - profit * mns)
                                            money[str(self.user)] += profit
                                            self.result[
                                                'message'] = f'Вы забрали прибыль, но вас обокрали на {full-profit}/{full}'
                                        else:
                                            money[str(self.user)] += profit
                                            self.result[
                                                'message'] = f'В этот раз все обошлось, вы забрали полную прибыль: {profit}'
                                    else:
                                        self.result['message'] = 'У вас пока нет прибыли.'
                                else:
                                    self.result['message'] = 'Такого пункта нет'
                        elif rate[0] == 'инвентарь':
                            _str = 'Ваш инвентарь:\n\n'
                            for i in inventory[str(self.user)]:
                                _str += i + ':\n'
                                for j in inventory[str(self.user)][i]:
                                    _str += '--' + j + ': ' + inventory[str(self.user)][i][j] + '\n'
                            self.result['message'] = _str
                        elif rate[0] == 'магазин':
                            rate = rate[1:]
                            _str = f"[{tm}] Деньги можно купить у админа: id117764726"
                            for i in items:
                                _str += f'\n{i}'
                            if not len(rate):
                                self.result['message'] = _str
                            else:
                                def get_key(_d, value):
                                    for _k, v in _d.items():
                                        if v == value:
                                            return _k

                                tmp_rate = ''
                                if len(rate) == 3:
                                    tmp_rate += rate[2]
                                rate = [(r[0].upper() + r[1:].lower()) for r in rate]
                                if len(rate) == 3:
                                    rate[2] = tmp_rate
                                n = '\n-'
                                if rate[0] in items:
                                    if len(rate) > 1:
                                        if rate[1] in items[rate[0]]:
                                            if len(rate) > 2:
                                                if rate[2] in items[rate[0]][rate[1]]:
                                                    if money[str(self.user)] >= items[rate[0]][rate[1]][rate[2]]['cost']:
                                                        money[str(self.user)] -= items[rate[0]][rate[1]][rate[2]]['cost']
                                                        reputation[str(self.user)] += items[rate[0]][rate[1]][rate[2]][
                                                            'bonus']
                                                        inventory[str(self.user)][rate[0]][rate[1]] = get_key(
                                                            items[rate[0]][rate[1]], items[rate[0]][rate[1]][rate[2]])
                                                        self.result[
                                                            'message'] = f'{rate[0]} -> {rate[1]} -> {rate[2]}: куплено.'
                                                    else:
                                                        self.result[
                                                            'message'] = f'Не хватает еще {items[rate[0]][rate[1]][rate[2]]["cost"] - money[str(self.user)]}'
                                                else:
                                                    self.result[
                                                        'message'] = f'Такого пункта нет:\n-{n.join([i for i in items[rate[0]][rate[1]]])}'
                                            else:
                                                self.result[
                                                    'message'] = f'Выберите:\n-{n.join([("[" + str(items[rate[0]][rate[1]][i]["bonus"]) + "] " + i + " (" + str(items[rate[0]][rate[1]][i]["cost"]) + ")") for i in items[rate[0]][rate[1]]])}'
                                        else:
                                            self.result[
                                                'message'] = f'Такого пункта нет:\n-{n.join([i for i in items[rate[0]]])}'
                                    else:
                                        self.result['message'] = f'Выберите:\n-{n.join([i for i in items[rate[0]]])}'
                                else:
                                    self.result['message'] = f'Такого пункта нет:\n-{n.join([i for i in items])}'
                        elif rate[0] == 'клад_секрет_не_догодаетесь':
                            if lucky['today'] != datetime.datetime.now().day:
                                if lucky['minute'] != datetime.datetime.now().minute:
                                    lucky['minute'] = datetime.datetime.now().minute
                                    lck = random.randint(0, 100000)
                                    if lck <= 5000:
                                        bonus = random.randint(1, 100000)
                                        money[str(self.user)] += bonus
                                        self.result['message'] = f'Нихуя, ты нашел клад! ({bonus})'
                                        nm = VK().Users().get(user_ids=int(self.user), fields='first_name, last_name')[0]
                                        lucky['name'] = nm['first_name'] + ' ' + nm['last_name']
                                        lucky['today'] = datetime.datetime.now().day
                                    else:
                                        self.result['message'] = 'В другой раз повезет.'
                                else:
                                    self.result['message'] = 'Попробуйте через минуту.'
                            else:
                                self.result['message'] = f'Сегодня клад уже нашел {lucky["name"]}'
                        elif rate[0] == 'экономика':
                            all_money = 0
                            for user in money:
                                if user != 'today':
                                    all_money += money[user]
                            for user in bank:
                                if user != 'today':
                                    all_money += bank[user]
                            for user in business:
                                if user != 'today':
                                    for bs in business[user]:
                                        if business[user][bs]['amount']:
                                            all_money += business[user][bs]['amount'] * bd_business[bs]['cost']
                            self.result['message'] = f'Вся экономика в игре стоит: {all_money}'
                        elif rate[0] == 'кредит_больше)не)робит':
                            if len(rate) > 1:
                                if not credit[str(self.user)]['day']:
                                    if UEngine.is_int(rate[1]):
                                        if 1000000 >= int(rate[1]) >= 10:
                                            money[str(self.user)] += int(rate[1])
                                            credit[str(self.user)] = {}
                                            credit[str(self.user)]['credit'] = int(int(rate[1]) * (random.randint(140, 150) / 100))
                                            credit[str(self.user)]['day'] = 5
                                            self.result['message'] = f'Вы успешно взяли в кредит {rate[1]} на 5 дней под 40-50% ({credit[str(self.user)]["credit"]})'
                                        else:
                                            self.result['message'] = 'В кредит можно взять только 10-1.000.000'
                                    else:
                                        self.result['message'] = 'Вы не ввели сумму.'
                                else:
                                    self.result['message'] = f'У вас уже есть кредит ({credit[str(self.user)]["credit"]}), который у вас заберут через {credit[str(self.user)]["day"]} дней.'
                            else:
                                self.result['message'] = 'Вы можете взять кредит, но потом у вас заберут его через 5 дней, с 40-50%'
                        elif rate[0] == 'донат':
                            if int(self.user) == var.czarID:
                                nums = [int(i) for i in rate if UEngine.is_int(i)]
                                if len(nums) == 2:
                                    users = VK().Messages().get_chat()['users']
                                    if nums[0] in users or nums[1] in users:
                                        if nums[0] in users:
                                            donat[str(nums[0])]['donat'] += nums[1]
                                        else:
                                            donat[str(nums[1])]['donat'] += nums[0]
                                        self.result['message'] = 'Донат добавлен.'
                                else:
                                    self.result['message'] = 'Введите ID и кол-во.'
                            else:
                                self.result['message'] = 'Только админ может этим пользоваться.'
                        elif rate[0] == 'вип':
                            if len(rate) == 2:
                                if UEngine.is_int(rate[1]):
                                    if donat[str(self.user)]['level']:
                                        if donat[str(self.user)]['vip']:
                                            vip = eval(open('DB\\vip.txt', 'r').read())
                                            if int(rate[1]) == random.randint(0, 10):
                                                self.result['message'] = f'Вы угадали и забираете банк: {vip["total"]}'
                                                vip['total'] = random.randint(1, 1000)
                                            else:
                                                vip['total'] += random.randint(1, 1000)
                                                self.result['message'] = f'Вы не угадали (Банк: {vip["total"]}).'
                                            donat[str(self.user)]['vip'] -= 1
                                            f = open('DB\\vip.txt', 'w')
                                            f.write(str(vip))
                                            f.close()
                                        else:
                                            self.result['message'] = 'Вы исчерпали попытки'
                                    else:
                                        self.result['message'] = 'Вашего уровня не хватает'
                                else:
                                    self.result['message'] = 'Введите число 1-10'
                            else:
                                self.result['message'] = f'У вас {donat[str(self.user)]["donat"]} доната ' \
                                                         f'({donat[str(self.user)]["level"]} уровень)'
                        elif rate[0] == 'доход':
                            self.result['message'] = f'Ваш ежедневный доход: {reputation[str(self.user)] + (donat[str(self.user)]["donat"] * 10)}'
                        elif rate[0] == 'баланс':
                            self.result['message'] = f'Ваш баланс: {money[str(self.user)]}'
                        elif rate[0] == 'репутация':
                            self.result['message'] = f'Ваша репутация: {reputation[str(self.user)]}'
                        else:
                            self.result['message'] = 'Такого пункта нет, введите !игра'
                    f = open('DB\\money.txt', 'w')
                    f.write(str(money))
                    f.close()
                    f = open('DB\\bank.txt', 'w')
                    f.write(str(bank))
                    f.close()
                    f = codecs.open('DB\\business.txt', 'w', 'utf-8')
                    f.write(str(business))
                    f.close()
                    f = open('DB\\lucky.txt', 'w')
                    f.write(str(lucky))
                    f.close()
                    f = open('DB\\reputation.txt', 'w')
                    f.write(str(reputation))
                    f.close()
                    f = codecs.open('DB\\inventory.txt', 'w', 'utf-8')
                    f.write(str(inventory))
                    f.close()
                    f = open('DB\\slots.txt', 'w')
                    f.write(str(slots))
                    f.close()
                    f = open('DB\\donat.txt', 'w')
                    f.write(str(donat))
                    f.close()
                    f = open('DB\\credit.txt', 'w')
                    f.write(str(credit))
                    f.close()
                    f = open('DB\\bonus_code.txt', 'w')
                    f.write(str(bonus_code))
                    f.close()
                    f = open('DB\\req_game.txt', 'w')
                    f.write(str(req_game))
                    f.close()
            else:
                self.result['message'] = f'Отдыхай.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
