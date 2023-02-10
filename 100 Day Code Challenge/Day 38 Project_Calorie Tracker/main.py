import requests
import datetime as dt
import os

APP_ID = os.environ.get("NUTRITION_APP_ID")
API_KEY = os.environ.get("NUTRITION_API_KEY")
Sheety_Auth_Token = os.environ.get("Sheety_Auth_Token")
nutrition_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/950c7cea0946ec0d803709bba291dec8/calorieTracker/sheet1"
print(APP_ID)
print(API_KEY)
print(Sheety_Auth_Token)


def get_time():
    date_time = dt.datetime.now()
    date_today = date_time.strftime("%d/%m/%Y")
    time_today = date_time.strftime("%H:%M:%S")
    return date_today, time_today


prof = {
    "query": input("What exercises did you do today? "),
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 182,
    "age": 28,
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

response = requests.post(url=nutrition_url, json=prof, headers=headers)
response.raise_for_status()

data = response.json()
date, time = get_time()


for exercise in data["exercises"]:
    sheety_header = {
        "Content-Type": "application/json",
        "Authorization": Sheety_Auth_Token,
    }
    sheet_params = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }

    response_sheety = requests.post(url=sheety_url, json=sheet_params, headers=sheety_header)
    response_sheety.raise_for_status()
