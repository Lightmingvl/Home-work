from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'http://www.accuweather.com/uk/ua/lviv/324561/april-weather/324561?monyr=4/1/2016'
response = urlopen(url)
html = response.read()


selector = 'div.info div.cond'
soup = BeautifulSoup(html, "html.parser")
bills = soup.select(selector)

bills

for l in bills:
    	if re.match(u".*(дощ|сніг)", l.text): print(l.text)