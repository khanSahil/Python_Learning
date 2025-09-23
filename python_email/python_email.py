import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
#print(smtp_object.starttls())

email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
#print(smtp_object.login(email, password))

#from_address = email
#to_address = email
#subject = input("Enter the subject line: ")
#message = input("Enter your message: ")

#msg = "Subject: "+subject+'\n'+message

#smtp_object.sendmail(from_address, to_address, msg)
#print("Email sent successfully!")


import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login(email, password)
#print(M.list())
M.select("inbox") # connect to inbox.

typ, data = M.search(None, 'SUBJECT "ChikuLovesBall"')
email_id = data[0]

result, email_data = M.fetch(email_id, '(RFC822)')
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

import email
email_message = email.message_from_string(raw_email_string)
print(email_message)