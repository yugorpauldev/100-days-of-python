##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib


files = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
# 1. Update the birthdays.csv
birthday = pd.read_csv("birthdays.csv")

birthday_dict = birthday.to_dict('records')

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

def send_email(selected_quote,email):
    my_email = "nhantumboyugor@gmail.com"
    password = "hikm cfad cypw matp"


    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=email, msg= f"Subject:Hey my Love\n\nHope you love the quote\n {selected_quote}")
    connection.close()

for item in birthday_dict:
        if item['month'] == month:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
            letter_option = random.choice(files)
            letter = open(letter_option, "r").read()
            new_letter = letter.replace("[NAME]",item['name'])
# 4. Send the letter generated in step 3 to that person's email address.
            send_email(new_letter,item['email'])









