# Emails ejemplos de automatizacion
En requirements.txt podras ver las bibliotecas y versiones que se necesitan en estos ejemplos.

## Iniciando 

- Crea el virtualenv
- Despues de descargar el contenido de git, debes comenzar instalando requirements.txt
```bash
    pip install -r requirements.txt
```
- Crear el archivo .env para adicionar valores de conexion del email para el envio de emails: 
```bash
ORIGEN=your@mail.com
DESTINY=destiny@mail.com
PASS=your_pass
```
- Generando passwords para apps, al utilizar Gmail: https://towardsdatascience.com/automate-sending-emails-with-gmail-in-python-449cc0c3c317


## Primer script: Utilizando scraping
- Crear en la direccion: pdf/any.pdf
```bash
python script_request_scrapping.py
```

## Segundo script: Utilizando un archivo csv
A TOMAR NOTA:
- Puedes usar .env para los ejemplos para enviar a solo un destinatario tambien 
- Para multiples destinatarios crea el archivo emails.csv, en este ejemplo enviaras a multiples destinatarios pero con diferentes valores (incluye la cabecera).
```bash
name,email,message
name1,email@mail.com,message1
name2,email@mail.com,message2
```
```bash
script_yagmail_users_attachments.py
```

## Tercer Script Crear algun pdf para adicionar a un archivo
```bash
python script_request_scrapping.py
```