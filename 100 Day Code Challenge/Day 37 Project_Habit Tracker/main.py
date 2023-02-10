import requests
import datetime as dt

TOKEN = "hjk2h43h42hk1h"
USER = "isbat"
code_time = input("How many minutes have you coded today?")
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = "https://pixe.la/v1/users/isbat/graphs"
pixel_posting_endpoint = "https://pixe.la/v1/users/isbat/graphs/graph1"


def get_today():
    today = str(dt.date.today())
    today_str = today.replace("-", '')
    return today_str


header = {
    'X-USER-TOKEN': TOKEN
}
pixel_post_params = {
    'date': get_today(),
    'quantity': code_time,
}

response = requests.post(url=pixel_posting_endpoint, json=pixel_post_params, headers=header)
print(response.text)


