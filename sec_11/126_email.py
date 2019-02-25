from email import message
import smtplib


# このままではgoogleには安全度が低いと見なされている
# 参考: https://qiita.com/oppasiri330/items/58d42cfb556209c77896

smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = 'xxxxxxxxxxx'
to_email = 'h0534jokt@gmail.com'
username = 'xxxxxxxxxxx'
password = 'xxxxxxxxxxx'

msg = message.EmailMessage()
msg.set_content('Test email')
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
