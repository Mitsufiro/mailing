import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
load_dotenv('.env')

def send_email(message):
    sender = 'lyashenk.ilya@gmail.com'
    password = os.environ['EMAIL_PASSWORD']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = 'HELLOOOO'
        server.sendmail(sender, 'moshka119@gmail.com', msg.as_string())
        return 'Message was send successfully'
    except Exception as ex:
        return f'{ex} \n Check your email or password'


def main():
    message = input('Type your message: ')
    print(send_email(message=message))


if __name__ == '__main__':
    main()
