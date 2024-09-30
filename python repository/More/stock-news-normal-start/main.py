import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
TWILIO_SID = "AC11488ef80359bb1f23ae58b1f18ac70b"
TWILIO_AUTH = "d7682ab2bc7ded2660c48b6a2b54cb84"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "SS4YJ0ZJXMPGOD4K"
NEWS_API_KEY = "4e0ce6103fde4e17b5e49cac283b3afb"
 ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey" : STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT,stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"Yesterday Stock closing price : {yesterday_closing_price}")


day_before_yesterday_data = data_list[1]
day_before_yesterday_stock = day_before_yesterday_data["4. close"]
print(f"Day before yesterday closing price: {day_before_yesterday_stock}")

stock_price_difference = float(day_before_yesterday_stock) - float(yesterday_closing_price)
up_down = None
if stock_price_difference > 0:
    up_down = "📈⬆️"
else:
    up_down = "📉🔽"

print(f"The stock difference is : {stock_price_difference}")

percentage_difference = round((stock_price_difference/float(yesterday_closing_price)) *100)
print(f'The stock has changes by  {percentage_difference} %')


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if abs(percentage_difference) > 1:
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,
        }
    new_response  = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = new_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    formated_article = [f"{STOCK_NAME}: {up_down} {percentage_difference}% \n Headline: {articles['title']}. \nBreif:{article['description']}" for article in three_articles]
    client = Client(TWILIO_SID,TWILIO_SID)
    for articles in formated_article:
        message = client.messages.create(
            body = articles,
            from_ = "+12407248717",
            to = "+919315688647"

        )


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

