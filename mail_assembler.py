#vlpmdxcmijxmdlme

import os
import smtplib
import imghdr
from email.message import EmailMessage
EMAIL_ADDRESS = 'rafaelz14@gmail.com'
EMAIL_PASSWORD = ''


msg = EmailMessage()
msg['Subject'] = 'Menu de la semana! ÑomÑom!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'lauracarolina50@gmail.com'

with open('menu.xlsx', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
msg.add_attachment(file_data, maintype='application',
                   subtype='xlsx', filename=file_name)
#maintype='application', subtype='pdf', filename='example.pdf'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
