import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

payload = {'groups': 'oscar_winner', 'limit': 0}
language = {'Accept-Language': 'en-US'}
url = "https://myanimelist.net/topanime.php?limit=0"
file = open('Oscar-winner-movies.csv', 'w', newline='\n')
f = csv.writer(file)
f.writerow(['Name', 'Year', 'Rating'])

while payload['start'] < 250:
    response = requests.get(url, params=payload, headers=language)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    block = soup.find('div', class_='lister-list')
    movies = block.find_all('div', class_='lister-item')
    for i in movies:
        name = i.h3.a.text
        year = i.find('span', class_='lister-item-year').text
        year = year.replace('(', "")
        year = year.replace(')', "")
        year = year.replace('I ', "")
        year = year.replace('II ', "")
        rate = i.strong.text
        print(rate)
        f.writerow([name, year, rate])
    payload['start'] += 50
    sleep(randint(5, 10))
