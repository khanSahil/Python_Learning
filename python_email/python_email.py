# To send email with Python, we need to manually
# go through th steps of connecting to an email
# server, confirming the connection, setting the protocol,
# logging on and sending the email.

# Fortunately, Python has a built-in library smtplib
# makes these steps simple function call.

# Each email provider has their own SMTP server.

# We will go over this process with Gmail account.
# For Gmail users, you will need to generate an app
# password instead of your normal password.

# This let Gmail know that the python script attempting
# to access your account is authorized by you.

import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587) # or 465 port number
smtp_object.ehlo()
#print(smtp_object.ehlo())# Can be omitted

smtp_object.starttls() # Encrypt the traffic
print(smtp_object.starttls()) # Can be omitted