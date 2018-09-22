from Settings import BotSettings as var
from Settings import DataBase as db
from Utils import Engine as UEngine
from threading import Thread
from Engine import Engine
from Log import Log
from VK import VK


class Main(object):
    @staticmethod
    def start():
        try:
            Log.show_info(f'Бот запущен.')
            if not var.main_start:
                VK().Messages().send(message=f'{var.name}: Успешный запуск.')
                var.globalID = VK().Messages().get_history(count=1)['items'][0]['id']
                var.main_start = True
            all_users = VK().Messages().get_chat()['users']
            main_users = VK().Messages().get_chat(chat_id=var.chatCheck)['users']
            for au in all_users:
                if au not in main_users:
                    VK().Messages().send( message='Сорен, тут можно находится только тем, кто есть в основной беседе.')
                    VK().Messages().remove_chat_user(user_id=au)
            while True:
                chat_title = VK().Messages().get_chat()['title']
                if chat_title != var.title:
                    VK().Messages().edit_chat(title=var.title)
                response = VK().Messages().get_history(count=10, offset=-10, start_message_id=var.globalID,
                                                       fields='first_name, last_name')
                if var.bot_online:
                    VK().Account().set_online()
                else:
                    VK().Account().set_offline()
                if not response is False:
                    response = response['items'][::-1]
                    if len(response):
                        for item in response:
                            if int(item['id']) > var.globalID and item['from_id'] != var.mainID:
                                var.globalID = int(item['id'])
                                s = ''
                                p = None
                                if 'body' in item:
                                    if len(item['body']) > 0:
                                        s += str.encode(item['body']).decode('utf-8')
                                    else:
                                        s += '(None)'
                                log = s
                                u = item['from_id']
                                if 'attachments' in item:
                                    log += ' ('
                                    for a in item['attachments']:
                                        tp = a['type']
                                        a = a[str(tp)]
                                        if tp == 'doc':
                                            log += f'doc: {a["title"]} (doc{a["owner_id"]}_{a["id"]}'
                                            if 'access_key' in a:
                                                log += '_' + a["access_key"]
                                            log += ')'
                                        if tp == 'photo':
                                            p = a['photo_604']
                                            log += f'photo: photo{a["owner_id"]}_{a["id"]}'
                                            if 'access_key' in a:
                                                log += '_' + a["access_key"]
                                        if tp == 'audio':
                                            log += f'audio: {a["artist"]} - ' \
                                                   f'{a["title"]} (audio{a["owner_id"]}_{a["id"]}'
                                            if 'access_key' in a:
                                                log += '_' + a["access_key"]
                                            log += ')'
                                        if tp == 'video':
                                            log += f'video: {a["title"]} (video{a["owner_id"]}_{a["id"]}'
                                            if 'access_key' in a:
                                                log += '_' + a["access_key"]
                                            log += ')'
                                        if tp == 'link':
                                            log += f'link: {a["title"]} ({a["url"]})'
                                        if tp == 'sticker':
                                            log += f'sticker: product_{a["product_id"]} id_{a["sticker_id"]}'
                                        log += ', '
                                    log = log[:len(log)-2]
                                    log += ')'
                                if 'geo' in item:
                                    log += f' (geo: {item["geo"]["coordinates"]})'
                                    if 'place' in item['geo']:
                                        log += f' ({item["geo"]["place"]["country"]}, {item["geo"]["place"]["city"]})'
                                if 'fwd_messages' in item:
                                    log += f' (forward: '
                                    for mes in item['fwd_messages']:
                                        log += f'{UEngine.get_username_by_id(mes["user_id"])} ({mes["body"]}), '
                                    log = log[:len(log)-2]
                                    log += ')'
                                Log.show_vk(UEngine.get_username_by_id(u) + ': ' + log)
                                f = open('DB\\money.txt', 'r')
                                money = eval(f.read())
                                if not str(item['user_id']) in money:
                                    money[str(item['user_id'])] = 0
                                money[str(item['user_id'])] += 1
                                f.close()
                                f = open('DB\\money.txt', 'w')
                                f.write(str(money))
                                f.close()
                                if 'action' in item:
                                    main_users = VK().Messages().get_chat(chat_id=var.chatCheck)['users']
                                    if item['action'] == 'chat_title_update':
                                        VK().Messages().edit_chat(title=var.title)
                                    if item['action'] == 'chat_photo_update':
                                        VK().Messages().set_chat_photo(file=var.photo)
                                    if item['action'] == 'chat_invite_user_by_link':
                                        if not int(item['user_id']) in db.black and item['user_id'] in main_users:
                                            VK().Messages().send(message='Добро пожаловать, ' +
                                                                         UEngine.get_link_by_id(item['user_id']) + '.')
                                        else:
                                            VK().Messages().send(message='Сорен, ты в ЧС или тебя нет в основной беседе.')
                                            VK().Messages().remove_chat_user(user_id=item['action_mid'])
                                    if item['action'] == 'chat_invite_user' or item['action'] == 'chat_kick_user':
                                        if not int(item['from_id']) in db.privilege:
                                            VK().Messages().remove_chat_user(user_id=item['from_id'])
                                            if int(item['from_id']) != int(item['action_mid']):
                                                VK().Messages().remove_chat_user(user_id=item['action_mid'])
                                        response = VK().Messages().get_chat()['users']
                                        for user in response:
                                            if int(user) in db.black or not user in main_users:
                                                VK().Messages().remove_chat_user(user_id=user)
                                    if item['action'] == 'chat_pin_message':
                                        if not int(item['action_mid']) in db.admins:
                                            VK().Messages().remove_chat_user(user_id=item['action_mid'])
                                            VK().Messages().unpin()
                                            VK().Messages().pin(message_id=var.pin_id['message_id'])
                                        else:
                                            var.pin_id['message_id'] = item['id']
                                            f = open('DB\\pin.txt', 'w')
                                            f.write(str(var.pin_id))
                                            f.close()
                                    if item['action'] == 'chat_unpin_message':
                                        if not int(item['action_mid']) in db.admins:
                                            VK().Messages().remove_chat_user(user_id=item['action_mid'])
                                        VK().Messages().pin(message_id=var.pin_id['message_id'])
                                elif len(s) > 2:
                                    if (var.debug_mode and int(u) == var.czarID) or not var.debug_mode:
                                        c = s[0]
                                        if c in var.prefixes:
                                            s = s[1:len(s)]
                                            md = 'a' if int(u) in db.admins else ('m' if int(u) in db.moders else 'u')

                                            def start_thread():
                                                Engine().cmd(s, p, u, md, item['id'])

                                            Thread(target=start_thread).start()
                                    else:
                                        if s[0] in var.prefixes:
                                            VK().Messages().send('Бот в режиме дебага.')
        except Exception as e:
            Log.show_error(e)
