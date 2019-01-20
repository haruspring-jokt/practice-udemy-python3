import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%Y-%H%M%S%f'))

today = datetime.date.today()
print(today)
print(now.isoformat())
print(now.strftime('%d/%m/%y'))

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))

print(now)
d = datetime.timedelta(weeks=-1, days=1)
print(now + d)


import time

# print('###')
# time.sleep(3)
# print('###')

# エポックタイム
print(time.time())