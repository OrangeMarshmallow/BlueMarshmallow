from Plugins.Base import BasePlugin as base
from Utils import Engine as UEngine
from bs4 import BeautifulSoup
from VK import VK
import requests


class InformationPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Информация'
        self.description = 'Отправляет информацию о человеке'
        self.words = ["информация", "инфо", "инфа", "information", "info", "infa"]

    def func(self):
        try:
            _inf = ''

            if len(str(self.text)) < 1:
                self.result['message'] = 'Введите корректный id'
                return True
            user_id = 0
            if not UEngine.is_int(self.text):
                try:
                    _id = int(UEngine.get_user_id(self.text))
                    if _id is False:
                        self.result['message'] = 'Введите корректный id'
                        return True
                    else:
                        user_id += _id
                except Exception as e:
                    print(e)
            else:
                user_id += int(self.text)
            try:
                if UEngine.is_int(user_id):
                    if user_id == 0:
                        self.result['message'] = 'Введите корректный id'
                        return True
                    fields = "id, domain, online, first_name, last_name, bdate, status, country, city, home_town, " \
                             "mobile_phone, home_phone, occuration, relation, last_seen, sex"
                    response = VK().Users().get(user_ids=user_id, fields=fields, name_case='nom')
                    _user = response[0]

                    r = requests.get('https://vk.com/foaf.php?id='+str(user_id))
                    soup = BeautifulSoup(r.text, 'html5lib').renderContents().decode('utf-8')
                    date = soup[soup.find('<ya:created dc:date=') + 21:]
                    date = date[:date.find('"')]
                    date = date.replace('T', ' , ')
                    date = date.replace('+', ' +')
                    _inf += f'Зарегистрировался: {date}\n'

                    _inf += 'ID: ' + str(_user['id'])
                    if 'domain' in _user:
                        _inf += ' (' + _user['domain'] + ')'
                    if _user['online'] == 1:
                        _inf += ' [online]'
                    else:
                        if 'last_seen' in _user:
                            _inf += ' [last online: ' + UEngine.get_date_by_stamp(_user['last_seen']['time']) + ']'
                        else:
                            _inf += '[offline]'
                    _inf += '\n'
                    _inf += 'Имя: ' + _user['first_name'] + '\n'
                    _inf += 'Фамилия: ' + _user['last_name'] + '\n'
                    _inf += 'Пол: '
                    if 'sex' in _user:
                        if int(_user['sex']) == 1:
                            _inf += 'Женский'
                        elif int(_user['sex']) == 2:
                            _inf += 'Мужской'
                        else:
                            _inf += 'Неизвестно'
                    _inf += '\n'
                    if 'bdate' in _user:
                        _inf += 'Дата рождения: ' + _user['bdate'] + '\n'
                    if 'status' in _user:
                        if len(_user['status']) > 0:
                            _inf += 'Статус: ' + _user['status'] + '\n'
                    if 'country' in _user:
                        if 'city' in _user:
                            _inf += 'Живет: ' + _user['country']['title'] + ', ' + _user['city']['title'] + '\n'
                    if 'home_town' in _user:
                        if len(_user['home_town']) > 0:
                            _inf += 'Родной город: ' + _user['home_town'] + '\n'
                    if 'mobile_phone' in _user:
                        _inf += 'Мобильный: ' + _user['mobile_phone'] + '\n'
                    if 'home_phone' in _user:
                        _inf += 'Домашний: ' + _user['home_phone'] + '\n'
                    if 'career' in _user:
                        for career in _user['career']:
                            if career['company']:
                                _inf += 'Работа: ' + career['company'] + ' (' + career['position'] + ')\n'
                                break
                    if 'relation' in _user:
                        if _user['relation'] != 0:
                            if _user['relation'] == 6:
                                _inf += 'Семейное положение: В активном поиске'
                            elif _user['relation'] == 1:
                                _inf += 'Семейное положение: Не женат'
                            else:
                                _inf += 'Семейное положение: ' + _user['relation_partner']['first_name'] + ' ' \
                                        + _user['relation_partner']['last_name'] + ' (' + str(
                                    _user['relation_partner']['id']) + ')\n'
                    self.result['message'] = _inf
                else:
                    self.result['message'] = 'Введите корректный id'
            except Exception as exc:
                # if False:
                print(exc)
                self.result['message'] = 'Введите корректный id'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
