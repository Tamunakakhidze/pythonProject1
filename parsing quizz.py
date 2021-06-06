import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

payload = {'limit': 0}
language = {'Accept-Language': 'en-US'}
url = "https://myanimelist.net/topanime.php"
resp = requests.get(url, params=payload)
file = open('top.animes.csv', 'w', newline='\n')
f = csv.writer(file)
f.writerow(['Rank', 'Name', 'Score'])

while payload['limit'] < 250:
    response = requests.get(url, params=payload, headers=language)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    block = soup.find('table', class_='top-ranking-table')
    animes = block.find_all('tr', class_='ranking-list')

    for i in animes:

        rank = i.td.span.text
        name = i.h3.a.text
        name = name.replace('△', "")
        name = name.replace('Ψ', '')
        name = name.replace('☆', '')
        name = name.replace('★', '')
        name = name.replace('°', '')
        name = name.replace('ä', '')
        rate = i.find('div', class_="js-top-ranking-score-col di-ib al").text
        print(rate)
        f.writerow([rank, name, rate])
    payload['limit'] += 50
    sleep(randint(5, 10))


