import smtplib
from email.message import EmailMessage

def send_email(counter):
    msg = EmailMessage()
    msg.set_content(f'Today, {counter} users used the Tarot app.')
    msg['Subject'] = 'Daily User Count'
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'hammoud.comms@gmail.com'

    # Establish a connection to the Gmail server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_app_specific_password')
    server.send_message(msg)
    server.quit()

# Read the counter and send the email
with open('counter.txt', 'r') as f:
    counter = int(f.read())
send_email(counter)

# Reset the counter for the next day
with open('counter.txt', 'w') as f:
    f.write('0')
