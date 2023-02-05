import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = 'indiabravohotel@gmail.com'
MY_LAT = 23.116142
MY_LONG = 91.989549
password = "vkalwjzifjzqmnwz"


def is_iss_near():
    if ((iss_location[0]-5) < MY_LONG < (iss_location[0]+5)) and ((iss_location[1]-5) < MY_LAT < (iss_location[1]+5)):
        return True
    else:
        return False


def is_nighttime():
    if not(sunset >= time_now >= sunrise):
        return True
    else:
        return False


while True:
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    iss_location = (float(data["iss_position"]['longitude']), float(data["iss_position"]['latitude']))
    print(iss_location)

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise_utc = int(sun_data['results']['sunrise'].split('T')[1].split(":")[0])
    sunset_utc = int(sun_data['results']['sunset'].split('T')[1].split(":")[0])
    sunrise = (sunrise_utc+6) % 24
    sunset = (sunset_utc+6) % 24
    time_now = datetime.now().hour

    if is_nighttime() and is_iss_near():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=password)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg="Subject:ISS is near\n\n"
                                    "If you go out now then you might see the International Space Station")

    time.sleep(60)
