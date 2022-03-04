# email-tool-fiesta
In requirements you can see the versions

## Packages 
You can ommit this and install all requirements.txt
- requests
```bash
    pip install requests
```
- beautifulsoup4
```bash
    pip install beautifulsoup4
```

## About emails
- Create an virtualenv
- Install requirements
```bash
    pip install requirements.txt
```
- Create the .env file to add values: 
```bash
ORIGEN=your@mail.com
DESTINY=destiny@mail.com
PASS=your_pass
```
- Create some pdf folder to add a file

- You can use .env for the examples sending email to only one recipient 
- Also Create a file emails.csv to use in the example to send tu multiple recipients, with the headers:
```bash
name,email,message
name1,email@mail.com,message1
name2,email@mail.com,message2
```