# -*- coding: utf-8 -*-
import bs4 as bs
import requests
import random

ergebniss=''


requests.packages.urllib3.disable_warnings()
sauce = requests.get('https://www.swr3.de/wraps/fun/filosofie/neu.php?id=11', verify=False)
soup = bs.BeautifulSoup(sauce.text, 'lxml')

for i in soup.find_all('div'):
    ergebniss=ergebniss+str(i)

start=(ergebniss.find('href="/wraps/fun/filosofie/neu.php?id=12"> weiter &gt; </a>   <a class="linkred" href='))
anzahl=int(ergebniss[start+119:start+123])
ran = random.randint(1, anzahl)
url='https://www.swr3.de/wraps/fun/filosofie/neu.php?id='+str(ran)

sauce = requests.get(url, verify=False)
soup = bs.BeautifulSoup(sauce.content,'lxml')
for i in soup.find_all('strong'):
    filosophie=(i.text)
print(filosophie)
