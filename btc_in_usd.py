from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import requests
import json
import time
from datetime import datetime

with open('token.json') as token_json:
    data = json.load(token_json)
    token = data['token']

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {'limit':'2'}
headers = {
  'Accepts': 'application/json',
  'symbol': 'BTC',
  'X-CMC_PRO_API_KEY': token,
}

def btc_in_usd():
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        BTC_PRICE_STR = str(data['data'][0]['quote']['USD']['price'])
        BTC_PRICE = float(BTC_PRICE_STR)
        return(BTC_PRICE)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)