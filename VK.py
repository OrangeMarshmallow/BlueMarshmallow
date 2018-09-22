import vk_api
from Settings import BotSettings as var
from Log import Log
import time

vk = vk_api.VkApi(login=var.login, password=var.password)
vk.auth()


class VK(object):
    def __init__(self):
        self.vk = vk

    def exec(self, method, parameters):
        time.sleep(var.sleep_time)
        return self.vk.method(method, parameters)

    class Messages(object):
        def __init__(self):
            self.chatID = var.chatID
            self.chatPeer = var.chatPeer
            self.parameters = dict()
            self.method = ''

        def send(self, message=None, lat=None, long=None, attachment=None, forward_messages=None):
            self.method = 'messages.send'
            self.parameters = {'peer_id': self.chatPeer, 'chat_id': self.chatID}
            if message:
                self.parameters['message'] = message
            if lat:
                self.parameters['lat'] = lat
            if long:
                self.parameters['long'] = long
            if attachment:
                self.parameters['attachment'] = attachment
            if forward_messages:
                self.parameters['forward_messages'] = forward_messages
            try:
                if var.listen:
                    return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def get_history(self, count=None, offset=None, start_message_id=None, fields=None, rev=None):
            self.method = 'messages.getHistory'
            self.parameters['peer_id'] = self.chatPeer

            if not count is None:
                self.parameters['count'] = count
            else:
                self.parameters['count'] = 5

            if offset:
                self.parameters['offset'] = offset

            if fields:
                self.parameters['fields'] = fields

            if rev:
                self.parameters['rev'] = rev

            if start_message_id:
                self.parameters['start_message_id'] = start_message_id

            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def remove_chat_user(self, user_id=None):
            try:
                self.method = 'messages.removeChatUser'
                self.parameters['chat_id'] = self.chatID
                self.parameters['user_id'] = user_id
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def set_chat_photo(self, file=None):
            try:
                self.method = 'messages.setChatPhoto'
                if file:
                    self.parameters['file'] = file
                else:
                    self.parameters['file'] = var.photo
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def edit_chat(self, title=None):
            try:
                self.method = 'messages.editChat'
                self.parameters['chat_id'] = self.chatID
                if title:
                    self.parameters['title'] = title
                else:
                    self.parameters['title'] = var.title
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def add_chat_user(self, user_id=None):
            self.method = 'messages.addChatUser'
            self.parameters['chat_id'] = self.chatID
            if user_id:
                self.parameters['user_id'] = user_id
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def edit(self, message=None, message_id=None, lat=None, long=None, attachment=None):
            self.method = 'messages.edit'
            self.parameters = {'peer_id': self.chatPeer}
            if message:
                self.parameters['message'] = message
            if lat:
                self.parameters['lat'] = lat
            if long:
                self.parameters['long'] = long
            if attachment:
                self.parameters['attachment'] = attachment
            if message_id:
                self.parameters['message_id'] = message_id
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def get_by_id(self, message_ids=None):
            self.method = 'messages.getById'
            self.parameters['message_ids'] = message_ids
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def get_chat(self, chat_id=None, fields=None):
            self.method = 'messages.getChat'
            self.parameters['chat_id'] = self.chatID
            if chat_id:
                self.parameters['chat_id'] = chat_id
            if fields:
                self.parameters['fields'] = fields
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def get_invite_link(self, reset=None):
            self.method = 'messages.getInviteLink'
            self.parameters['peer_id'] = self.chatPeer
            if reset:
                self.parameters['reset'] = reset
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def pin(self, message_id=None):
            self.method = 'messages.pin'
            self.parameters['peer_id'] = self.chatPeer
            if message_id:
                self.parameters['message_id'] = message_id
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def unpin(self, group_id=None):
            self.method = 'messages.pin'
            self.parameters['peer_id'] = self.chatPeer
            if group_id:
                self.parameters['group_id'] = group_id
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

    class Users(object):
        def __init__(self):
            self.parameters = dict()
            self.method = ''

        def get(self, user_ids=None, fields=None, name_case=None):
            self.method = 'users.get'
            if user_ids:
                self.parameters['user_ids'] = user_ids
            if fields:
                self.parameters['fields'] = fields
            if name_case:
                self.parameters['name_case'] = name_case
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def get_followers(self):
            self.method = 'users.getFollowers'
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def get_nearby(self, latitude=None, longitude=None, radius=None, fields=None):
            self.method = 'users.getNearby'
            if latitude:
                self.parameters['latitude'] = latitude
            if longitude:
                self.parameters['longitude'] = longitude
            if radius:
                self.parameters['radius'] = radius
            if fields:
                self.parameters['fields'] = fields
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

    class Friends(object):
        def __init__(self):
            self.parameters = dict()
            self.method = ''

        def get(self, user_id=None):
            self.method = 'friends.get'
            if user_id:
                self.parameters['user_id'] = user_id
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def add(self, user_id=None):
            self.method = 'friends.add'
            if user_id:
                self.parameters['user_id'] = user_id
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def get_requests(self):
            self.method = 'friends.getRequests'
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

    class Photos(object):
        def __init__(self):
            self.parameters = dict()
            self.method = ''

        def get(self, owner_id=None, album_id=None, count=None, offset=None):
            self.method = 'photos.get'
            if owner_id:
                self.parameters['owner_id'] = owner_id
            if album_id:
                self.parameters['album_id'] = album_id
            if count:
                self.parameters['count'] = count
            if offset:
                self.parameters['offset'] = offset
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def get_messages_upload_server(self):
            self.method = 'photos.getMessagesUploadServer'
            self.parameters['peer_id'] = 2000000001
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def save_messages_photo(self, server=None, photo=None, _hash=None):
            self.method = 'photos.saveMessagesPhoto'
            if server:
                self.parameters['server'] = server
            if photo:
                self.parameters['photo'] = photo
            if _hash:
                self.parameters['hash'] = _hash
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

    class Wall(object):
        def __init__(self):
            self.parameters = dict()
            self.method = ''

        def get(self, owner_id=None, count=None, offset=None):
            self.method = 'wall.get'
            if owner_id:
                self.parameters['owner_id'] = owner_id
            if count:
                self.parameters['count'] = count
            if offset:
                self.parameters['offset'] = offset
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

    class Video(object):
        def __init__(self):
            self.parameters = dict()
            self.method = ''

        def get(self, owner_id=None, album_id=None, count=None, offset=None):
            self.method = 'video.get'
            if owner_id:
                self.parameters['owner_id'] = owner_id
            if album_id:
                self.parameters['album_id'] = album_id
            if count:
                self.parameters['count'] = count
            if offset:
                self.parameters['offset'] = offset
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def get_albums(self, owner_id=None, count=None, offset=None, need_system=None):
            self.method = 'video.getAlbums'
            if owner_id:
                self.parameters['owner_id'] = owner_id
            if need_system:
                self.parameters['need_system'] = need_system
            if count:
                self.parameters['count'] = count
            if offset:
                self.parameters['offset'] = offset
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

    class Groups(object):
        def __init__(self):
            self.parameters = dict()
            self.method = ''

        def get_by_id(self, group_ids=None):
            self.method = 'groups.getById'
            if group_ids:
                self.parameters['group_ids'] = group_ids
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

    class Account(object):
        def __init__(self):
            self.parameters = dict()
            self.method = ''

        def set_online(self):
            self.method = 'account.setOnline'
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def set_offline(self):
            self.method = 'account.setOffline'
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)

    class Docs(object):
        def __init__(self):
            self.parameters = dict()
            self.method = ''

        def get_upload_server(self, _type=None):
            self.method = 'docs.getUploadServer'
            if _type:
                self.parameters['type'] = _type
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def get_messages_upload_server(self, _type):
            self.method = 'docs.getMessagesUploadServer'
            self.parameters['peer_id'] = var.chatPeer
            if _type:
                self.parameters['type'] = _type
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False

        def save(self, file=None):
            self.method = 'docs.save'
            if file:
                self.parameters['file'] = file
            try:
                return VK().exec(self.method, self.parameters)
            except Exception as e:
                Log.show_error(e)
                return False
