import random
import string
import requests

url = input("Enter Your Webhook: ")
answer = int(input("How many would you like to scrape?: "))
for x in range(answer):

    result_str = ''.join(random.sample(string.ascii_lowercase, 6))
    results = "https://prnt.sc/" + result_str

    data = {
    "content" : results,
    "avatar_url" : "https://virtuooza.com/wp-content/uploads/2018/06/lightshot-virtuooza2.png",
    "username" : "Prnt.sc Scraper"
    }

    result = requests.post(url, json=data)