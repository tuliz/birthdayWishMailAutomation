import smtplib
import random
import datetime as dt
import pandas

birthdays_dataframe = pandas.read_csv('birthdays.csv')
birthdays_list = birthdays_dataframe.to_dict(orient='records')

current_day = dt.datetime.now().day
current_month = dt.datetime.now().month
for birthday in birthdays_list:
    if current_day == birthday['day'] and current_month == birthday['month']:
        print('its today')