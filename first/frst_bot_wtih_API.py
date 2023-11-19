import requests
import time
import token_my_bot


TOKEN = token_my_bot.token
URL_TG = 'https://api.telegram.org/bot'
TEXT_MESSAGE = 'ЖОПА'
MAX_COUNT = 100

offset = -2
counter = 0


while counter < MAX_COUNT:
    print(counter)

    updates = requests.get(f'{URL_TG}{TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for update in updates['result']:
            print(update)
            offset = update['update_id']
            chat_id = update['message']['from']['id']
            requests.get(f'{URL_TG}{TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_MESSAGE}')

    time.sleep(1)
    counter += 1
