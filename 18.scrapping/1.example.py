import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.pythonscraping.com/pages/page3.html')
print(data)
print(data.text)

soup = BeautifulSoup(data.text, 'html.parser')
gift = soup.select('#giftList > tr')
my_gift = gift[1:]
for g in my_gift:
    td = g.select('td')
    print(len(td))
    print(f"Title: {td[0].text.strip()}\nPrice: {td[2].text.strip()}\nImg:{td[3].img['src']}")