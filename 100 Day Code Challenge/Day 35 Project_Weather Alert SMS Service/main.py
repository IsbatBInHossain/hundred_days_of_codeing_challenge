import requests
from twilio.rest import Client
import os

API_KEY = "54801adf635195560d16b19c66c3f628"
MY_LAT = 23.116142
MY_LONG = 91.989549
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily,alert'
}
response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
id_list = []

for i in range(11):
    id_num = weather_data['hourly'][i]['weather'][0]["id"]
    id_list.append(id_num//100)


def weather_checker():
    if 2 in id_list:
        return "There's going to be a thunderstorm. Be careful and bring an Umbrella."
    elif 5 in id_list:
        return "It is going to rain today. Be sure to bring an Umbrella."
    elif 3 in id_list:
        return "It is going to be drizzling today. Be sure to bring an Umbrella."
    elif 6 in id_list:
        return "It might snow today"
    else:
        return 0


if weather_checker() != 0:
    message = client.messages.create(
      body=f"{weather_checker()}",
      from_="+17739067810",
      to="+8801815423827"
    )
    print(message.status)
