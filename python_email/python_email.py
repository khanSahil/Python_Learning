import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""
# Gmail SMTP settings
smtp_server = "smtp.gmail.com"
port = 587  # STARTTLS (use 465 with SMTP_SSL if you prefer)
sender_email = "sahilkhan.alld@gmail.com"  # must be your Gmail (or a verified alias)
APP_PASSWORD = " "  # 16-char Google App Password (paste exactly)
receiver_email = "sahilkhan.alld@gmail.com"

# Create the email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email from Python (Gmail App Password)"

body = "Hello, this is a test email sent from Python using a Gmail App Password via STARTTLS!"
msg.attach(MIMEText(body, "plain"))

# Send (STARTTLS on port 587)
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls()          # upgrade connection to TLS
    server.ehlo()
    server.login(sender_email, APP_PASSWORD)  # use App Password, not your normal password
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email sent successfully with STARTTLS + App Password!")
"""

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
print(smtp_object.starttls())

email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your password: ")
print(smtp_object.login(email, password))

from_address = email
to_address = email
subject = input("Enter the subject line: ")
message = input("Enter your message: ")

msg = "Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address, to_address, msg)
print("Email sent successfully!")
