import bs4 as bs
import requests
import random

#requests.packages.urllib3.disable_warnings()
sauce = requests.get('https://www.swr3.de/wraps/fun/filosofie/neu.php?id=11', verify=False)
encodedText = sauce.text.encode("utf-8")
soup = bs.BeautifulSoup(encodedText, 'html')
print(encodedText)
#print(soup)

print(soup.find_all("tr"))

text=soup.get_text()
print(text.decode("utf-8"))