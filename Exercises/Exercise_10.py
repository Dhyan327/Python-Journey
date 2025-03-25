# In this part I will do "Exercise 10 Solution"
# Exercise :->
'''  Use the NewsAPI and the requests module to fetch the daily news related to different topics. 
    Go to: https://newsapi.org/ and explore the various options to build you application.
'''

# Solution :~~>

import requests
import json

api_key = 'f33cf2a2d13a4889b088174918e8f58d'
query = input("What type of news are you interested in: ")
url = f'https://newsapi.org/v2/everything?language=en&q={query}&from=2024-07-04&sortBy=publishedAt&apiKey={api_key}'

r = requests.get(url)
news = json.loads(r.text)
# print(news)

for index, article in enumerate(news["articles"], start=1):
    if index == 6:
        break
    print(article["title"])
    print(article["description"])
    print("--------------------------------------------------------------------------------------------------------------------")