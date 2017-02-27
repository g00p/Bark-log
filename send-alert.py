#! /usr/bin/python3

import smtplib
from functions import *

gmail_user = 'barklogalerts@gmail.com'
gmail_password = 'yeR2Xb8JmHbJ'


#create email text

sender = 'gmail_user'
targets = ['michaels138@gmail.com']
subject = get_subject()
body = get_body()
email_text = """\
From: {}
To: {}
Subject: {}

{}
""".format(sender, ", ".join(targets), subject, body)


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sender, targets, email_text)
    server.close()

    print('you did it champ!')

except:
    print('Something broke...')

