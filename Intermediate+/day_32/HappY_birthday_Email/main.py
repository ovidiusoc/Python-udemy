import datetime as dt
import smtplib
import random

my_email = "@gmail.com"
password = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


# import smtplib
#
# my_email = "@gmail.com"
# password = ""
# second_email = "@yahoo.com"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=second_email,
#         msg="Subject:Hello\n\nThis is the content of the message"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# # now.year
# day_of_week = now.weekday()
# print(now.year)
#
# date_of_birth = dt.datetime(year=1997, month=2, day=26, hour=8)
#
# print(date_of_birth)