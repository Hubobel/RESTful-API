# -*- coding: utf-8 -*-
import bs4 as bs
import requests
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

ergebniss=''

def Nachricht(sub='I am ROOT',body='this comes from Hubobel'):
    fromaddr = 'schneeschieben@web.de'
    toaddr = 'carsten.richter@soka-bau.de'
    bccs = toaddr

    pwd = 'PL19zPL19z'
    acc = 'carsten.richter77@gmail.com'

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = sub

    msg.attach(MIMEText(body, 'plain'))



    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(acc, pwd)
    text = msg.as_string()
    server.sendmail(fromaddr, bccs, text)
    server.quit()
    return

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

Nachricht(filosophie,filosophie)