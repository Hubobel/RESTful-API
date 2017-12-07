import bs4 as bs
import requests
import time

requests.packages.urllib3.disable_warnings()
sauce=requests.get('https://www.eurojackpot.org/gewinnzahlen/',verify=False)
soup = bs.BeautifulSoup(sauce.text,'lxml')


zahlen=[]
ergebniss=[]
ZahlenEuro = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Eurozahl1': '', 'Eurozahl2': ''}
a=1
datum= soup.find_all('time')
tag=[]
for i in datum:
    tag.append(i.text)
for li in soup.find_all('li'):
    zahlen.append(li.text)
for i in zahlen[0:7]:
    ergebniss.append(int(i))
ergebniss.append(tag[1])
while a!=6:
    ZahlenEuro['Z'+str(a)]=ergebniss[a-1]
    a=a+1
ZahlenEuro['Datum']=ergebniss[7]
ZahlenEuro['Eurozahl1']=ergebniss[5]
ZahlenEuro['Eurozahl2']=ergebniss[6]

requests.packages.urllib3.disable_warnings()
sauce=requests.get('https://www.lotto24.de/webshop/product/lottonormal/result',verify=False)
soup = bs.BeautifulSoup(sauce.text,'lxml')

#print(soup.prettify())
Lottozahlen = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Z6': '', 'Superzahl': '',
                     'Spiel77': '', 'Super6': ''}
daten=soup.find_all('div',class_="winning-numbers__number")
zahlen=[]
for i in daten:
    zahlen.append(int(i.text))
a=1
while a!=7:
    Lottozahlen['Z'+str(a)]=zahlen[a-1]
    a=a+1
Spiel77=''
Super6=''
zahlen77=[]
daten=soup.find_all('div',class_="winning-numbers__number--additional")
for i in daten:
    zahlen77.append(int(i.text))
spiel77=zahlen77[0:7]
super6=zahlen77[-6:]
for i in spiel77:
    Spiel77=Spiel77+str(i)
for i in super6:
    Super6=Super6+str(i)

daten=soup.find_all('h2',class_="strong hidden-xs")
for i in daten:
    date=i.text
    date=date.replace('  ','')
    date = date.replace('\n', '')

Lottozahlen['Superzahl']=zahlen[6]
Lottozahlen['Spiel77']=Spiel77
Lottozahlen['Super6']=Super6
Lottozahlen['Datum']=date
print(Lottozahlen)
print(ZahlenEuro)