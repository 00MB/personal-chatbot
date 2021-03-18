def send_email(user, time):
    EMAIL_ADDRESS = "test@gmail.com" #Replace with os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = "pass"
    text = f"Your time has been confirmed for {time}"

    msg = EmailMessage()
    msg['Subject'] = "AutoBookMe - Your confirmed time"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = user.email
    msg.set_content(text)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)