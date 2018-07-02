import requests
from bs4 import BeautifulSoup as bs

# https://www.tab.com.au/sports/betting/Soccer/competitions/2018%20World%20Cup%20Matches
# https://www.chorus.co.nz/
# https://shop.countdown.co.nz/shop/browse/meat
# http://dataquestio.github.io/web-scraping-pages/simple.html
r = requests.get('https://portal.chorus.co.nz/chorus-ssp-web/pages/WorkQueue/WorkQueue')
a = r.text
# a = bs(r.content, 'lxml')
# a = r.content
c = a.replace(u"\u2013","'")
b = c.replace(u"\u2019","'")
d = b.replace(u"\xa9","'")
# e = bs(d, 'lxml')
print(d)