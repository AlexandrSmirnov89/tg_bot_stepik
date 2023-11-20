import requests
import time
import token_my_bot


TOKEN = token_my_bot.token
URL_TG = 'https://api.telegram.org/bot'
URL_API_CAT = 'https://api.thecatapi.com/v1/images/search'
ERROR_TEXT = 'эта киса куда-то делясь('

offset = -2
counter = 0

while counter < 120:
    print(counter)

    updates = requests.get(f'{URL_TG}{TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for update in updates['result']:
            offset = update['update_id']
            chat_id = update['message']['from']['id']
            cat_response = requests.get(URL_API_CAT)
            if cat_response.status_code == 200:
                url_pic = cat_response.json()[0]['url']
                print(url_pic)
                requests.get(f'{URL_TG}{TOKEN}/sendPhoto?chat_id={chat_id}&photo={url_pic}')
            else:
                requests.get(f'{URL_TG}{TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
