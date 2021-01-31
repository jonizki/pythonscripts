import smtplib
import time

email_address = 'own_email'
password = 'own_email_password'

with smtplib.SMTP('SMTP.office365.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_address, password)

    subject = 'Hello'
    body = 'test'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email_address, 'receiver_email', msg)
    time.sleep(5)
