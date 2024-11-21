import requests
URL = 'https://www.cdn.geeksforgeeks.org/data-structures/'
r = requests.get(URL)
print(r.content)