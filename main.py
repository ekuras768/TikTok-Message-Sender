from TikTokApi import TikTokApi
from config import username, password, friends
import time

api = TikTokApi.get_instance()

api.login(username, password)

def send_message(user_id, message):
    api.send_message(user_id, message)

while True:
    for friend in friends:
        send_message(friend, '.')
        print(f"Сообщение отправлено {friend}")
    time.sleep(86400)
