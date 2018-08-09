import requests

url_zitat = 'http://api.hubobel.de/tv'
resp_zitat = requests.get(url_zitat)
data_zitat = resp_zitat.json()

for i in data_zitat:
    if i != 'Senderliste':
        #print('Auf '+(i)+' läuft gerade "'+data_zitat[i]['Titel']+'" ('+data_zitat[i]['Uhrzeit']+')')
        print((i)+' '+data_zitat[i]['Titel']+' ('+data_zitat[i]['Uhrzeit']+')')
