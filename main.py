import requests 
import json
from api_keys import *


stock_api_endpoint = "https://www.alphavantage.co/query"

params = {"function" : "TIME_SERIES_DAILY_ADJUSTED",
          "symbol" : "TSLA",
          "apikey" : STOCK_API_KEY}

response = requests.get(stock_api_endpoint, params= params)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]

data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

print(yesterday_closing_price)
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)
