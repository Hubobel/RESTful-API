import bs4 as bs
import requests


requests.packages.urllib3.disable_warnings()
sauce = requests.get('https://www.swr3.de/wraps/fun/filosofie/neu.php?id=11', verify=False)
soup = bs.BeautifulSoup(sauce.content,'lxml')


Vers=(soup.find("strong"))


print(Vers.text)