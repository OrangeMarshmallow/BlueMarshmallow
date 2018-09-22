from Plugins.Base import BasePlugin as base
from bs4 import BeautifulSoup
import requests
import ast


class CSGOStatPlayerPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'CSGO stat player'
        self.description = 'Отправляет общую статистику игрока в CSGO'
        self.words = ["csgostatplayer"]

    def func(self):
        global _str
        try:
            if len(self.text) > 0:
                try:
                    profile_id = str(self.text)
                    soup1 = BeautifulSoup(requests.get('https://steamcommunity.com/id/' + str(profile_id)).text,
                                          'html5lib').text
                    soup2 = BeautifulSoup(requests.get('https://steamcommunity.com/profiles/' + str(profile_id)).text,
                                          'html5lib').text
                    if 'g_rgProfileData' in soup1 or 'g_rgProfileData' in soup2:
                        soup = soup1 if 'g_rgProfileData' in soup1 else soup2
                        steam_id = soup[soup.find('g_rgProfileData '):][:soup.find(';') - 3]
                        steam_id = steam_id[steam_id.find('steamid') + 10:]
                        key = 'C12C0CEE9C4FEDB109B9B36C82C88F08'
                        url = f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key={key}&steamid={steam_id}'

                        r = requests.get(url)
                        soup = BeautifulSoup(r.text, 'html5lib').text

                        dict_soup = ast.literal_eval(soup)['playerstats']['stats']

                        _filter = {
                            'total_kills': 'Убито',
                            'total_deaths': 'Смертей',
                            'total_time_played': 'Сыграно времени',
                            'total_planted_bombs': 'Заложено бомб',
                            'total_defused_bombs': 'Обезврежено бомб',
                            'total_wins': 'Побед',
                            'total_damage_done': 'Нанесено урона',
                            'total_money_earned': 'Денег заработано',
                            'total_rescued_hostages': 'Заложников спасено',
                            'total_kills_headshot': 'Хедшотов',
                            'total_kills_enemy_weapon': 'Убито вражеским оружием',
                            'total_weapons_donated': 'Подарено оружий',
                            'total_shots_hit': 'Попаданий',
                            'total_shots_fired': 'Выстрелов',
                            'total_rounds_played': 'Сыграно раундов',
                            'total_matches_won': 'Выиграно матчей',
                            'total_matches_played': 'Сыграно матчей',
                            'total_mvps': 'Лучший игрок'
                        }

                        all_hits = 0
                        all_shots = 0
                        all_kills = 0
                        all_heads = 0
                        all_deaths = 0
                        all_mvps = 0
                        all_rounds = 0
                        all_won = 0
                        all_games = 0

                        _str = ''
                        for i in dict_soup:
                            if i['name'] == 'total_shots_hit':
                                all_hits = i['value']
                            if i['name'] == 'total_shots_fired':
                                all_shots = i['value']
                            if i['name'] == 'total_kills':
                                all_kills = i['value']
                            if i['name'] == 'total_deaths':
                                all_deaths = i['value']
                            if i['name'] == 'total_kills_headshot':
                                all_heads = i['value']
                            if i['name'] == 'total_mvps':
                                all_mvps = i['value']
                            if i['name'] == 'total_rounds_played':
                                all_rounds = i['value']
                            if i['name'] == 'total_matches_won':
                                all_won = i['value']
                            if i['name'] == 'total_matches_played':
                                all_games = i['value']

                            if i['name'] in _filter:
                                _str += f'{_filter[i["name"]]}: {i["value"]}\n'
                        _str += '\nПрочее:\n'
                        _str += f'Лучший игрок: {int(all_mvps/all_rounds * 10000) / 100}%\n'
                        _str += f'Попаданий: {int(all_hits/all_shots * 10000) / 100}%\n'
                        _str += f'Голов: {int(all_heads/all_kills * 10000) / 100}%\n'
                        _str += f'Побед: {int(all_won/all_games * 10000) / 100}%\n'
                        _str += f'КД: {int(all_kills/all_deaths * 100) / 100}\n'

                    self.result['message'] = _str
                except Exception as e:
                    print(e)
                    self.result['message'] = 'Некорректный id.'
            else:
                self.result['message'] = 'Введите id.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
