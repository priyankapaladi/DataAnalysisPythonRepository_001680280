# Get data for python
import requests
from requests_oauthlib import OAuth1
import os, json
from time import sleep

pageStr = '1'

while True:
    # Try not to hard code.
    url ='https://api.stackexchange.com/2.2/questions?page='+pageStr+'&pagesize=100&order=desc&sort=activity&site=stackoverflow&key=f49Nam3UjMJmLs2KHr1jcg(('
    response = requests.get(url)
    response = response.json()
    with open(pageStr+'.json', 'w') as f:
        json.dump(response, f)
    page = int(pageStr) + 1
    # Seems unnecessary.
    pageStr = str(page)
    if page == 2500:
        break
print(page)
