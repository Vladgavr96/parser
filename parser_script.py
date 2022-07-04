import requests
from bs4 import BeautifulSoup as bs
from time import sleep

site_url = "https://azbykamebeli.ru/catalog/0000057/"
page = 1
all_items_urls = []

'''while True:
    r = requests.get(f'{site_url}?page={page}')
    print(r.url)
    soup = bs(r.text, "html.parser")
    data = soup.find_all('div', class_='item__title h4')
    if not data:
        break
    with open('urls.txt', 'a') as f:
        for i in data:
            all_items_urls.append("https://azbykamebeli.ru" + i.a['href'])
            f.write("https://azbykamebeli.ru" + i.a['href']+'\n')
    page += 1
    sleep(10)
print(len(all_items_urls))
print(all_items_urls[-1])'''

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
        name = soup.find('h1').get_text()
        print(name)

        # получаем цену со скидкой и без
        store_price_data = soup.find('a', class_='store-price fake-link').get_text().split()[:-1]
        store_price = int(''.join(store_price_data))

        online_price_data = soup.find('div', class_='online-price').get_text().split()[:-1]
        online_price = int(''.join(online_price_data))
        print(online_price)

        # стутас доступен\под заказ
        data = soup.find('span', class_='d-inline-block badge-pre-order')
        if data:
            status = data.get_text()
        else:
            status = 'доступен'
        print(status)
        with open('result.txt', 'a') as result_text:
            result_text.write(name + '\n')
            result_text.write(articul + '\n')
            result_text.write(id + '\n')
            result_text.write(str(store_price) + '\n')
            result_text.write(str(online_price) + '\n')
            result_text.write(status + '\n')
