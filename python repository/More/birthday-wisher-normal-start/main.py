from typing import Tuple, Any

import pandas as pd
import datetime as dt
import random
import smtplib

MYEMAIL= "testingsingh25@gmail.com"
PASSWORD = "iqdf zdvl jfen prad"

now = dt.datetime.now()
today_tuple = (now.month,now.day)
data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open (file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MYEMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MYEMAIL,
            to_addrs=birthday_person["email"],
            msg = f"Subject: Happy Birthday!! "
            f"\n\n {content}")





