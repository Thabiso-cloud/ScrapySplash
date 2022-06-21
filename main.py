import requests
from bs4 import BeautifulSoup
url = 'https://www.amazon.com/s?k=canon+m50+mark+ii&sprefix=canon+m%2Caps%2C511&ref=nb_sb_ss_ts-doa-p_1_7'

r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2})

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.title.text)