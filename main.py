import smtplib
import random
import datetime as dt
import pandas

EMAIL = 'yarden.tulchinsky@gmail.com'
PASSWORD = 'ecib yifv vrbb bjpz'
birthdays_dataframe = pandas.read_csv('birthdays.csv')
birthdays_list = {(row['day'], row['month']): row for (index,row) in birthdays_dataframe.iterrows()}

today = (dt.datetime.now().day, dt.datetime.now().month)

if today in birthdays_list:
    random_letter = random.randint(1,3)

    #get a random letter and change it to have the name of the one who has birthday
    with open(f'letter_templates/letter_{random_letter}.txt','r') as letter:
        wish = letter.read()
        new_wish= wish.replace('[NAME]',birthdays_list[today]['name'].title())

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(EMAIL,PASSWORD)
        connection.sendmail(EMAIL,birthdays_list[today]['email'],msg=f'subject:Happy Birthday\n\n{new_wish}')