# To get search term
# Authorize and get the search term!
import requests
from requests_oauthlib import OAuth1
import os, json
from time import sleep



url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('E5eeHHPrKm0N8qkHhH1BOkSu6', 'iLkXetVRI93Xt32KJfY44CUfau1BgH4BHSotaDLHloaykLOmTR',
                  '744995423308374017-ic5GQxFdUxYjgpFJSbAQ1rRaJluz4nJ', 'hZl4AAiu62CalzpY8BeJfX2wJXezROk0WsEhms9KxXQ4w')
requests.get(url, auth=auth)


searchWord = input("Please enter a search term: ")
filepath = searchWord.replace(" ","").lower() 
searchWord = searchWord.replace(" ", "%20")
print("This is the search term: " + searchWord)
print("Path:" + filepath)
