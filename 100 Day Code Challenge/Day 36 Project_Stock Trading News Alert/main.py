import requests
import os
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API = os.environ.get('ALPHA_VANTAGE_API_KEY')
NEWS_API = os.environ.get('NEWS_API')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={ALPHA_API}'
response = requests.get(url=stock_url)
response.raise_for_status()
data = response.json()

today = dt.date.today()
yesterday = str(today-dt.timedelta(days=2))
day_before_yesterday = str(today-dt.timedelta(days=3))
yesterday_close = float(data["Time Series (Daily)"][yesterday]['4. close'])
day_before_yesterday_close = float(data["Time Series (Daily)"][day_before_yesterday]['4. close'])
percentage = ((yesterday_close - day_before_yesterday_close)/day_before_yesterday_close)*100

if percentage >= 0:
    per = round(abs(percentage), 2)
    per_sign = f"🔺{per}%"
else:
    per = round(abs(percentage), 2)
    per_sign = f"🔻{per}%"

news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}%20Inc&from={day_before_yesterday}" \
           f"&sortBy=popularity&apiKey={NEWS_API}"
news_response = requests.get(url=news_url)
all_news = news_response.json()
relevent_news = [all_news['articles'][i] for i in range(3)]
headline_list = [relevent_news[i]['title'] for i in range(3)]
brief_list = [relevent_news[i]['description'].replace("\n", " ") for i in range(3)]
msg_list = []
new_line = "\n"

for i in range(3):
    msg = f"TSLA: {per_sign}{new_line}Headline: {headline_list[i]}{new_line}Brief: {brief_list[i]}"
    msg_list.append(msg)


if per >= 2:
    for msg in msg_list:
        message = client.messages.create(
            body=msg,
            from_="+17739067810",
            to="+8801815423827"
            )
        print(message.status)
