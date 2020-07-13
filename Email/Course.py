import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

#greet the server (587 is for encryption)

smtp_object.ehlo()
smtp_starttls() # not required if you use ssl
#do not put e-mail or password use them from another file

import getpass

password = getpass.getpass('Password please:') #secured way to pass a password

email = getpass.getpass("Email:")
password = getpass.getpass('Password:')
smtp_object.login(email, password)

#then enter the address gmail and the app password generated from the gamil app password web-app

#now we send an e-mail

from_address = email
to_address = email
subject = input('Enter the subject line:')
message = input('Enter the body message:')
msg = "Subject:" +subject+'\n'+message

smtp_object.sendmail(from_address, to_address, msg)

#receiving email

import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')

import getpass
email=getpass.getpass("Email:")
password = getpass.getpass('Password:')

M.login(email, password)
M.list()

M.select('inbox')

typ, data = M.search(None, 'BEFORE 01-Nov-2000')
typ
email_id=data[0]

result, email_data = M.fetch(email_id, 'RFC822')

raw_email = email_data [0][1]
raw_email_string = raw_email.decode('utf-8')

import email

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)

