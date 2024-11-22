import requests
from bs4 import BeautifulSoup as bs
from pprint import pp

URL = 'https://www.cdn.geeksforgeeks.org/data-structures/'
alaska = 'https://education.alaska.gov/DOE_Rolodex/SchoolCalendar/DistrictAndSchoolInfo/DistrictDetails'
r = requests.get(alaska)

soup = bs(r.content, 'html5lib')

print(soup.prettify())