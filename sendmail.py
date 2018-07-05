#! /usr/bin/python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd

# me == my email address
# to == recipient's email address
me = "<email to be used to send email>"
to = "<same email as me/ email above>"  #just a workaround for hiding recipients in the email
my_password = '<password>'
recipients = list()

# READING THE CSV FILE USING PANDAS
file_name = 'tobesent.csv' #CSV filename having the Email column

df = pd.read_csv(file_name)
emails = df.Email #Column to be picked up

for email in emails:
	recipients.append(email)

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = to #", ".join(to)



html = open('geekyvisuals.html', 'r').read()  #	HTML file to be used as email template.
text = open('geekyvisuals.html', 'r').read()  # simple text file can also be used though


# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
server.login(me, my_password)
server.sendmail(me, [to]+recipients, msg.as_string())
server.quit()