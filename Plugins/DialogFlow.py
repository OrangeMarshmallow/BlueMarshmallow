from Plugins.Base import BasePlugin as base
from Settings import BotSettings as var
import requests
import random
import json


class DialogFLow(base):
    def __init__(self):
        super().__init__()
        self.name = 'Диалог с искуственным интеллектом'
        self.description = 'Позволяет разговаривать с ботом'
        self.words = ["ответь"]

    def func(self):
        try:
            if len(self.text) > 0:
                client_access_token = 'ac51402912e54eb6b443657eb980b097'
                base_url = "https://api.dialogflow.com/v1/query"
                base_version = "20170712"
                current_id = var.mainID
                user_id = self.user
                headers = {
                    "Authorization": f"Bearer {client_access_token}",
                }
                body = {
                    "lang": "ru",
                    "contexts": ["chat"],
                    "query": self.text,
                    "sessionId": str(current_id) + "_" + str(user_id),
                }
                params = {
                    "v": base_version
                }
                response = requests.post(url=base_url, json=body, headers=headers, params=params).text
                response = json.loads(response)
                try:
                    m = [
                        "Давай попробуем сначала",
                        "Нихуя непонятно",
                        "Шота непонятно",
                        "Это ты мне?",
                        "Я не понял",
                        "Повтори",
                    ]
                    if 'messages' in response['result']['fulfillment']:
                        answer = response['result']['fulfillment']['messages'][0]['speech']
                        if len(answer) > 0:
                            self.result['message'] = answer
                        else:
                            self.result['message'] = random.choice(m)
                    else:
                        self.result['message'] = random.choice(m)
                except Exception as e:
                    self.result['message'] = 'Error: ' + str(e)
            else:
                self.result['message'] = 'Я не отвечаю на пустые сообщения.'
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
