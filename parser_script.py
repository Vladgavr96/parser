import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import sqlite3

site_url = "https://azbykamebeli.ru/catalog/0000057/"
page = 1
all_items_urls = []

#создаем базу и таблицу
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS products 
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
name text,
articul int,
item_id int,
full_price int,
sale_price int,
status text)""")


'''while True:
    r = requests.get(f'{site_url}?page={page}')
    print(r.url)
    soup = bs(r.text, "html.parser")
    data = soup.find_all('div', class_='item__title h4')
    if not data:
        break
    for i in data:
        all_items_urls.append("https://azbykamebeli.ru" + i.a['href'])
    page += 1
    sleep(3)

clear_data = set(all_items_urls)

with open('urls.txt', 'a') as f:
    for i in clear_data:
        f.write(i + '\n')'''

with open('urls.txt', 'r') as f:
    text = f.read().splitlines()
    for url in text:
        r = requests.get(url)
        soup = bs(r.text, "html.parser")

        # получаем id
        data = soup.find('div', class_='align-self-start')
        articul = data.find_all("span")[0].get_text().split()[1]
        id = data.find_all("span")[1].get_text().split()[1]

        # получаем имя
        name = soup.find('h1')
        print(name)
        # получаем цену со скидкой и без
        store_price_data = soup.find('a', class_='store-price fake-link').get_text().split()[:-1]
        if store_price_data:
            store_price = int(''.join(store_price_data))
        else:
            store_price = None

        online_price_data = soup.find('div', class_='online-price').get_text().split()[:-1]
        if online_price_data:
            online_price = int(float(''.join(online_price_data)))
        else:
            online_price = None

        # стутас доступен\под заказ
        data = soup.find('span', class_='d-inline-block badge-pre-order')
        if data:
            status = data.get_text()
        else:
            status = 'доступен'
        print(status)

        params = (str(name), articul, id, store_price, online_price, str(status))
        cursor.execute(f"INSERT INTO products Values(NULL,?,?,?,?,?,?)", params)

conn.commit()







