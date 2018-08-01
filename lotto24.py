import bs4 as bs
import requests
import time

requests.packages.urllib3.disable_warnings()
sauce=requests.get('https://m.lotto.de/de/ergebnisse/eurojackpot/eurojackpot-zahlen.html',verify=False)
soup = bs.BeautifulSoup(sauce.text,'lxml')


source= soup.find_all('div',class_='ball')
print(soup)
