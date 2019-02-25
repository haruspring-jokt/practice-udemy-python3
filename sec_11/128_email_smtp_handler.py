import logging.handlers

smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = 'xxxxxxxxxxxxx'
to_email = 'h0534jokt@gmail.com'
username = 'xxxxxxxxxxxxx'
# Gmailの場合、passwordにはアプリ パスワードを用いる
password = 'xxxxxxxxxxxxx'

logger = logging.getLogger('email')

# critical以上の場合はメールを送信するようなハンドラーを設定する
logger.setLevel(logging.CRITICAL)

logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port),
    from_email,
    to_email,
    subject='Admin test log',
    credentials=(username, password),
    secure=(None, None, None),
    timeout=20
))

logger.info('test')
logger.critical('critical')
