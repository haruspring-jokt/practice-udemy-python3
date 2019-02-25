import dbm

with dbm.open('chche', 'c') as db:
    db['key1'] = 'value1'
    db['key2'] = 'value2'

with dbm.open('chche', 'r') as db:
    print(db.get('key1'))
