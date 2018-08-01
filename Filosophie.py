import pymysql
import bs4 as bs
import requests

connection = pymysql.connect(db="hubobel",
                       user="hubobel",
                       passwd="polier2003",
                       host='10.0.1.59',charset='utf8')
cursor = connection.cursor()



requests.packages.urllib3.disable_warnings()
sauce = requests.get('https://www.swr3.de/wraps/fun/filosofie/neu.php?id=1117', verify=False)
soup = bs.BeautifulSoup(sauce.text, 'lxml')


for i in soup.find_all('meta'):
    print(i)
    print(i.get('content'))