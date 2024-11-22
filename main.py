import requests
from bs4 import BeautifulSoup as bs
from pprint import pp

URL = 'https://www.cdn.geeksforgeeks.org/data-structures/'
r = requests.get(URL)

soup = bs(r.content, 'html5lib')

print(soup.prettify())