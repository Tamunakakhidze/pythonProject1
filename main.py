import requests
import json
import sqlite3

# connection to database using sqlite3 module
# მონაცემთა ბაზასთან დაკავშირება sqlite3 მოდულის გამოყენებით
conn = sqlite3.connect('asteroids_db.sqlite')
cursor = conn.cursor()

# requests module's few functions and attributes ( get(), status_code, header, text)
# request მოდულის  ფუნქციები და ატრიბუტები

url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY'
resp = requests.get(url)
print(resp)
print(resp.headers)
print(resp.status_code)
print(resp.text)

# json format data in a json file in a structured form (using the json module function)
# json ფორმატის მონაცემი json ფაილში სტრუქტურული სახით (json მოდულის ფუნქციის  გამოყენებით


res = resp.json()
resp_json = json.dumps(res, indent=4)
print(resp_json)
with open('asteroids.json', 'w') as file:
    json.dump(res, file, indent=4)

#  json/dict ობიექტთან სამუშაო ფუნქციების გამოყენება და API-ს მეშვეობით ზოგიერთ ინფორმაციაზე წვდომა
#  using of json/dict functions and getting some useful information using  Nasa asteroids API

url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY'
resp = requests.get(url)
r = json.loads(resp.text)
rr = resp.json()
print(type(r))
data = r['element_count']
print('asteroids near earth: ', data)
astr1_id = rr['near_earth_objects']['2015-09-08'][0]['id']
print('1st id:', astr1_id)

# რელაციური მონაცემთა ბაზის შექმნა
# Creating relative database
rr = resp.json()
list = []

# აღწერა: 2015-09-08 ლისტში მოვძებნე ასტეროიდის აიდი, სახელი, Boolean მნიშვნელობა რომელიც აჩვენებს საშიშია თუ არა ეს
# ასტეროიდი და მისი აბსოლუტური მაგნიტუდა. შემდეგ მიღებული ცვლადებისგან შევქმენი tuple ტიპის ობიექტი და ეს ობიექტი
# დავამატე წინასწარ შექმნილ სიაში. შევქმენი შესაბამისი სვეტები და ინსერტში გადავეცი for ციკლში წარმოდგენილი სია.

for each in rr['near_earth_objects']['2015-09-08']:
    asteroid_id = each['id']
    name = each['name']
    hazardous_or_not = each['is_potentially_hazardous_asteroid']
    abs_magn = each['absolute_magnitude_h']
    tupl_row = (asteroid_id, name, hazardous_or_not, abs_magn)
    list.append(tupl_row)
print(list)

cursor.execute('''CREATE TABLE if not exists asteroids
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                asteroid INTEGER,
                name VARCHAR(50),
                potentially_hazardous NUMERIC,
                absolute_magnitude_h NUMERIC
                )''')

cursor.executemany(
    'INSERT INTO asteroids (asteroid, name, potentially_hazardous, absolute_magnitude_h) VALUES (?, ?, ?, ?)', list)
conn.commit()

