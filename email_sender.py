import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # similar to os.path


html = Template(Path('index.html').read_text())

email = EmailMessage()
email["from"] = 'sender name' # replace with your info
email["to"] = "<to email address>" # replace with your info
email["subject"] = "You won a million dollars"

email.set_content(html.substitute(name='TinTin'), "html")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<YourEmail@gmail.com>', '<password>') # replace with your info and do not recommit
    smtp.send_message(email)
    print('all good boss')