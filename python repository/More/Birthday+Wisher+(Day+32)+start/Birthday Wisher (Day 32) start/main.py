import smtplib
import datetime as dt
import random as ram

MYEMAIL= "testingsingh25@gmail.com"
PASSWORD = "iqdf zdvl jfen prad"
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt","r") as quotes:
        all_qoutes = quotes.readlines()
        daily_qoutes = ram.choice(all_qoutes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MYEMAIL,password= PASSWORD)
        connection.sendmail(
            from_addr= MYEMAIL,
            to_addrs="prabhleenreet18@gmail.com"
            ,msg = f"Subject:Motivation for the day \n\n{daily_qoutes}")

