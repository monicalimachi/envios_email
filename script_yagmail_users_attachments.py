from cmath import e
from dataclasses import fields
from json.tool import main
import time
import yagmail
import csv
from dotenv import dotenv_values, load_dotenv
import os

load_dotenv()
RECEIPT = os.getenv("ORIGEN")
DESTINY = os.getenv("DESTINY")
PASSWD = os.getenv("PASS")

wait=20

yag = yagmail.SMTP(user=RECEIPT, password=PASSWD)
file = open('emails.csv')

try:
    with open("emails.csv", "r") as csvfile:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
         #for line in headers:
        for name, email, message in csv_reader:
            yag.send(email, subject = name, contents = message) 
            print(f"Email enviado a {name} con {email}")
            time.sleep(wait)
    print("Los envios han finalizado")

except Exception as e:
    print(e)
