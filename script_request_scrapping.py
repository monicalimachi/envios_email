from email import contentmanager
import requests                                 #Http requests
from bs4 import BeautifulSoup                   # Web Scrapping
import smtplib                                  # Send email
from email.mime.multipart import MIMEMultipart  #Email body
from email.mime.text import MIMEText            # Email body
import datetime

from dotenv import dotenv_values, load_dotenv
import os

load_dotenv()
RECEIPT = os.getenv("ORIGEN")
DESTINY = os.getenv("DESTINY")
PASSWD = os.getenv("PASS")


now = datetime.datetime.now()

content = ''        #Email content placeholder, global var


#Extrayendo titulos de noticias

def extract_news(url):
    print('Extrayendo nuevas noticias')
    cnt= ''
    cnt += ('<b> Bolivia:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content                      #This var is local
    soup = BeautifulSoup(content,'html.parser')
    for i, tag in enumerate(soup.find_all('h3', attrs={'class':'entry-title td-module-title'})):
        cnt += ((str(i+1)+'::'+tag.text + "\n"+'<br>') if tag.text!='More' else '')

    return(cnt)

cnt = extract_news('https://jornada.com.bo/')
content+=cnt
content += ('<br>--------<br>')
content += ('<br><br>End of message')
print('Construyendo el Email .... ')

#Update your emails
SERVER = 'smtp.gmail.com'   # "your smtp server"

PORT = 587                  # port number
FROM = RECEIPT                   # from .env email id
TO = DESTINY                     # from .env EMAIL ID'S, LIST
PASS = PASSWD                   # from .env your email id's password

#fp = open(file_name, 'rb')

#Create a text/plain message
#msg = MIMEText('')
msg=MIMEMultipart()

#msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
msg['Subject']='Top News Stories HN [Automated Email]'+' '+ str(now.day)+'-'+ str(now.month)+ '-'+ str(now.year)

msg['From'] = RECEIPT
msg['To'] = DESTINY

msg.attach(MIMEText(content, 'html'))

#fp.close()

print('Initiating Server ...')

try:
    server = smtplib.SMTP(SERVER, PORT)
    #server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    #server.ehlo
    server.login(FROM, PASS)
    server.sendmail(FROM, TO, msg.as_string())
    print('Email sent....')
except Exception as e:
    print(e)

finally:
    server.quit()
