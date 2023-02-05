##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import random
import datetime as dt
import smtplib


def letter_opener(num):
    with open(f"letter_templates/letter_{num}.txt") as file:
        letter = file.readlines()
    return letter

my_email = "indiabravohotel@gmail.com"
password = "vkalwjzifjzqmnwz"
reciepients_email = "indiabravohotel@yahoo.com"


letter_list = [letter_opener(num) for num in range(1, 4)]
birthday_df = pandas.read_csv("birthdays.csv")
birthday_list = birthday_df.to_dict(orient="records")
now = dt.datetime.now()
today = (now.day, now.month)
for day in birthday_list:
    if today == (day['day'], day['month']):
        name = day['name']
        random_letter = random.choice(letter_list)
        random_letter[0] = random_letter[0].replace("[NAME]", name)
        final_letter = ''
        for line in random_letter:
            final_letter += line
        print(final_letter)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=reciepients_email,
                                msg=f"Subject:Happy Birthday!\n\n{final_letter}")
