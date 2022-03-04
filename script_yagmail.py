from cmath import e
from json.tool import main
import yagmail

from dotenv import dotenv_values, load_dotenv
import os

load_dotenv()
RECEIPT = os.getenv("ORIGEN")
DESTINY = os.getenv("DESTINY")
PASSWD = os.getenv("PASS")

try:
    yag = yagmail.SMTP(user=RECEIPT, password=PASSWD)
    body = "Hello there from Yagmail"
    filename = "pdf/sample.pdf"

  #  yag = RECEIPT
    yag.send(
    to=DESTINY,
    subject="Yagmail test with attachment",
    contents=body, 
    attachments=filename,
    )
    print("Email sent successfully")
except Exception as e:
    print(e)