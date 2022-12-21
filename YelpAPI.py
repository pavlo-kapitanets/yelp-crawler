import requests
import json
import config

API_KEY = config.API_KEY
ENDPOINT = "https://api.yelp.com/v3/businesses/"
HEADERS = {"accept": "application/json", "Authorization": f"bearer {API_KEY}"}


def get_biz(business_id: str) -> any:
    url = ENDPOINT + business_id
    response = requests.get(url=url, headers=HEADERS)
    return json.loads(response.text)
