import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

payload = {'page': 1}
language = {'Accept-Language': 'ge-GEO'}
url = 'https://www.myauto.ge/ka/s/00/0/33/1625/00/00/00/00/porsche-panamera?stype=0&marka=33&model=1625&category_id=m0&page=2'
responce = requests.get(url, params=payload, headers=language)
file = open('cars.csv', 'w', newline='\n')
f = csv.writer(file)
print(responce.text)
f.writerow(['Name', 'Year', 'Price'])

while payload['page'] < 6:
    response = requests.get(url, params=payload, headers=language)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    block = soup.find('div', class_='search-lists-container')
    movies = block.find_all('div', class_='current-item')
    for i in movies:
        name = i.h4.a.text
        year = i.div.p.text
        price = i.find('div', class_='car-list-price')
        print(price)
        f.writerow([name, year, price])
    payload['page'] += 1
    sleep(randint(5, 10))
