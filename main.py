import requests 
import json
from api_keys import *
from twilio.rest import Client

stock_api_endpoint = "https://www.alphavantage.co/query"
news_api_endpoint = "https://newsapi.org/v2/everything"

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


difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

percentage = (difference/float(yesterday_closing_price)) * 100

print(percentage)

if percentage > 1:

    params_2 = {"apiKey" : NEWS_API_KEY,
                "q" : "Tesla Inc"}

    response_2 = requests.get("https://newsapi.org/v2/everything", params= params_2)
    response_2.raise_for_status()

    data_2 = response_2.json()["articles"]

    three_articles = data_2[:3]

    formatted_articles = [f"Headline : {article['title']}. \nBrief : {article['description']}" for article in three_articles]

    print(formatted_articles)

