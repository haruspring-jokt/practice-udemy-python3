import requests

r = requests.get(
    'http://127.0.0.1:5000/employee/haruspring'
)
print(r.text)

r = requests.post(
    'http://127.0.0.1:5000/employee', data={'name': 'haruspring'}
)
print(r.text)

r = requests.put(
    'http://127.0.0.1:5000/employee', data={'name': 'haruspring', 'new_name': 'h0534'}
)
print(r.text)

r = requests.delete(
    'http://127.0.0.1:5000/employee', data={'name': 'haruspring'}
)
print(r.text)
