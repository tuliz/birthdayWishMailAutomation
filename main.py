import smtplib
import random
import datetime as dt
import pandas

EMAIL = 'yarden.tulchinsky@gmail.com'
PASSWORD = 'ecib yifv vrbb bjpz'
birthdays_dataframe = pandas.read_csv('birthdays.csv')
birthdays_list = birthdays_dataframe.to_dict(orient='records')

current_day = dt.datetime.now().day
current_month = dt.datetime.now().month
for birthday in birthdays_list:
    if current_day == birthday['day'] and current_month == birthday['month']:
        random_letter = random.randint(1,3)

        #get a random letter and change it to have the name of the one who has birthday
        with open(f'letter_templates/letter_{random_letter}.txt','r') as letter:
            wish = letter.read()
            new_wish= wish.replace('[NAME]',birthday['name'].title())

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(EMAIL,PASSWORD)
            connection.sendmail(EMAIL,birthday['email'],msg=f'subject:Happy Birthday\n\n{new_wish}')