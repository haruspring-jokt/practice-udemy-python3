from email import message
from email.mime import multipart
from email.mime import text
import smtplib

# このままではgoogleには安全度が低いと見なされている
# 参考: https://qiita.com/oppasiri330/items/58d42cfb556209c77896

smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = 'xxxxxxxxxxxxxxxx'
to_email = 'h0534jokt@gmail.com'
username = 'xxxxxxxxxxxx'
# Gmailの場合、passwordにはアプリ パスワードを用いる
password = 'xxxxxxxxxxxx'

# msg = message.EmailMessage()
msg = multipart.MIMEMultipart()
# msg.set_content('Test email')
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email
msg.attach(text.MIMEText('Test email', 'plain'))

with open('127_email_attachment.py', 'r', encoding='utf-8') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment', filename='lesson.txt'
    )
    msg.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
