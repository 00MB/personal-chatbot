import smtplib #Emails
from email.message import EmailMessage
from datetime import datetime

def send_email(EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_RECIEVER):

    text = "You have a new conversation waiting!"
    msg = EmailMessage()
    msg['Subject'] = f"Michael, new conversation at {datetime.now()}"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_RECIEVER
    msg.set_content(text)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("email sent")