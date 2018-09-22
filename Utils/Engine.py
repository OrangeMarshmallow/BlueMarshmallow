from Settings import BotSettings as var
from multiprocessing import Process
from bs4 import BeautifulSoup
from Log import Log
from VK import VK
import datetime
import requests
import random
import json


def check_user_in_original_chat(user_id):
    return int(user_id) in VK().Messages().get_chat(chat_id=var.chatCheck)['users']


def get_link_by_id(user_id):
    user_id = str(user_id)
    try:
        user = VK().Users().get(user_ids=user_id)[0]
        return f"@id{user['id']} ({user['first_name']} {user['last_name']})"
    except Exception as e:
        Log.show_error(e)
        return False


def get_username_by_id(user_id):
    try:
        user = VK().Users().get(user_ids=user_id)[0]
        return f"{user['first_name']} {user['last_name']}"
    except Exception as e:
        Log.show_error(e)
        return False


def get_user_online(user_id):
    try:
        return VK().Users().get(user_ids=user_id, fields='online')[0]['online']
    except Exception as e:
        Log.show_error(e)
        return False


def get_user_id(user_text):
    if len(user_text):
        try:
            user = VK().Users().get(user_ids=user_text)
            if len(user):
                if 'error' in user:
                    return False
                elif 'id' in user[0]:
                    return user[0]['id']
        except Exception as e:
            Log.show_error(e)
            return False


def get_user_id_by_message(message_id=None):
    if message_id is None:
        message_id = var.lastID
    return VK().Messages().get_by_id(message_ids=message_id)['items'][0]['user_id']


def get_message_by_id(message_id=None):
    if message_id is None:
        message_id = var.lastID
    return VK().Messages().get_by_id(message_ids=message_id)


def get_date_by_stamp(stamp):
    return str(datetime.datetime.fromtimestamp(stamp))


def user_exist_in_chat(user_id):
    return int(user_id) in VK().Messages().get_chat()['users']


def user_exist_in_friends(user_id):
    return int(user_id) in VK().Friends().get(user_id=var.mainID)['items']


def get_text(r):
    soup = BeautifulSoup(r.text, 'html5lib')
    result = str(soup.find_all("p", {"class": "text"}))
    url = 'http://api.foxtools.ru/v2/TextDecoder'
    post = {'text': result, 'from': 'windows-1252', 'to': 'windows-1251'}
    res = requests.post(url, json=post).text
    s = res[22:len(res) - 14]
    s = s.replace('[', '')
    s = s.replace(']', '')
    s = s.replace('<p class=\\"text\\">\\n', '')
    s = s.replace('\\n</p>, ', '\n')
    s = s.replace('\\n</p>', '')
    s = s.replace('<sup>', '')
    s = s.replace('</sup>', '')
    s = s.replace('<sub>', '')
    s = s.replace('</sub>', '')
    return s


def get_password(num):
    return num * random.randint(99, 999999)


def reset_privilege():
    db.privilege = db.admins + db.moders


def get_group_id_by_text(group_text):
    return -int(VK().Groups().get_by_id(group_ids=group_text)['id'])


def get_random_wall_picture(group_id, count=1):
    import random
    while True:
        max_num = VK().Photos().get(owner_id=group_id, album_id='wall', count=0)['count']
        if max_num > count:
            photos_result = ''
            for _ in range(count):
                num = random.randint(1, max_num)
                photos = VK().Photos().get(owner_id=group_id, album_id='wall', count=1, offset=num)['items']
                photos_result += 'photo' + str(group_id) + '_' + str(photos[0]['id']) + ','
            return photos_result


def get_random_wall_post(group_id, count=1):
    import random
    max_num = VK().Wall().get(owner_id=group_id)['count']
    if max_num > count:
        post_result = ''
        for i in range(count):
            num = random.randint(1, max_num)
            post = str(i+1) + '. '
            post += VK().Wall().get(owner_id=group_id, count=1, offset=num)['items'][0]['text']
            if '#' in post:
                post = post[0:post.find('#') - 1]
            post += '\n\n'
            post_result += post
        return post_result


def get_random_album(group_id):
    import random
    item = VK().Video().get_albums(owner_id=group_id, count=50, offset=0, need_system=1)['items']
    return random.choice(item)['id']


def get_random_wall_video(group_id, count=1):
    import random
    while True:
        album = get_random_album(group_id)
        max_num = VK().Video().get(owner_id=group_id, album_id=album, count=0)['count']
        if max_num > count:
            attachment_count = 0
            attachment_result = ''
            while True:
                num = random.randint(1, max_num)
                video = VK().Video().get(owner_id=group_id, album_id=album, count=1, offset=num)
                if len(video['items']) > 0:
                    if 'id' in video['items'][0]:
                        attachment = 'video' + str(video['items'][0]['owner_id']) + '_' + str(video['items'][0]['id'])
                        attachment_result += attachment + ','
                        attachment_count += 1
                if attachment_count >= count:
                    break
            return attachment_result


def get_random_wall_gif(group_id, count=1):
    import random
    max_num = VK().Wall().get(owner_id=group_id)['count']
    doc_result = ''
    if max_num > count:
        for _ in range(count):
            num = random.randint(1, max_num)
            post = VK().Wall().get(owner_id=group_id, count=1, offset=num)['items'][0]['attachments'][0]['doc']
            _str = "doc" + str(post['owner_id']) + '_' + str(post['id']) + '_' + str(post['access_key'])
            doc_result += _str + ','
    return doc_result


def get_random_wall_music(group_id, count=1):
    import random
    music_result = ''
    music_count = 0
    while True:
        max_num = VK().Wall().get(owner_id=group_id)['count']
        num = random.randint(1, max_num)
        post = VK().Wall().get(owner_id=group_id, count=count, offset=num)['items']
        if 'attachments' in post[0]:
            for attachment in post[0]['attachments']:
                if 'audio' in attachment:
                    if attachment['type'] == 'audio':
                        _str = "audio" + str(attachment['audio']['owner_id']) + '_' + str(attachment['audio']['id'])
                        music_count += 1
                        music_result += _str + ','
                        if music_count >= count:
                            return music_result


def debug():
    VK().Messages().send(message='Плагин находится в режиме дебага, только админ имеет доступ.')


def job():
    VK().Messages().send(message='Плагин не работает.')


def non():
    VK().Messages().send(message='Недостаточно прав.')


def what():
    VK().Messages().send(message='Команды не существует.')


def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def image(image_name=None):
    server = VK().Photos().get_messages_upload_server()['upload_url']
    response = requests.post(server, files={'photo': open(image_name, 'rb')}).text
    r = json.loads(response)
    u = VK().Photos().save_messages_photo(server=r['server'], photo=r['photo'], _hash=r['hash'])[0]
    _str = 'photo' + str(u['owner_id']) + '_' + str(u['id']) + '_' + u['access_key']
    return _str


def doc(doc_name=None):
    server = VK().Docs().get_messages_upload_server('doc')['upload_url']
    response = requests.post(server, files={'file': open(doc_name, 'rb')}).text
    r = json.loads(response)['file']
    u = VK().Docs().save(file=r)[0]
    _str = 'doc' + str(u['owner_id']) + '_' + str(u['id'])
    return _str


def audio_message(audio_name=None):
    server = VK().Docs().get_upload_server(_type='audio_message')['upload_url']
    response = requests.post(server, files={'file': open(audio_name, 'rb')}).text
    r = json.loads(response)['file']
    u = VK().Docs().save(file=r)[0]
    _str = 'doc' + str(u['owner_id']) + '_' + str(u['id'])
    return _str


def timeout(func=None, time=None, exception='End of time.', args=()):
    p = Process(target=func, args=args)
    p.start()
    p.join(time)
    if p.is_alive():
        p.terminate()
        raise Exception(exception)
    return True
