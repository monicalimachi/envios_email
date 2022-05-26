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
    body = "<H1>Hola desde este ejemplo</H1>\n Mi nombre es: <b>Juana</b>\n Mi edad es: <b>25</b>\n Mi email es: <b>"
    filename = "pdf/php-ejemplos.pdf"

  #  yag = RECEIPT
    yag.send(
    to=DESTINY,
    subject="Testeando envio de archivos PDF con Yagmail",
    contents=body, 
    attachments=filename,
    )
    print("Email enviado exitosamente")
except Exception as e:
    print(e)